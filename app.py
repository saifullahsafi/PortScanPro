from flask import Flask, render_template, request

from scanner.target_validator import validate_target
from scanner.service_detector import detect_services
from scanner.risk_analyzer import analyze_risk

from database.database import initialize_database, get_connection
from reports.report_generator import generate_report


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    results = []
    error = None

    if request.method == "POST":

        target = request.form["target"]

        start_port = int(request.form["start_port"])
        end_port = int(request.form["end_port"])

        target_ip = validate_target(target)

        if not target_ip:

            error = "Invalid target."

        elif start_port > end_port:

            error = "Start port must be less than end port."

        else:

            try:

                scanned_services = detect_services(
                    target_ip,
                    start_port,
                    end_port
                )

                connection = get_connection()

                cursor = connection.execute(
                    """
                    INSERT INTO scans
                    (target, start_port, end_port)
                    VALUES (?, ?, ?)
                    """,
                    (
                        target_ip,
                        start_port,
                        end_port
                    )
                )

                scan_id = cursor.lastrowid

                for result in scanned_services:

                    port = result["port"]
                    service = result["service"]

                    risk, description = analyze_risk(port, service)

                    results.append({
                        "port": port,
                        "service": service,
                        "risk": risk,
                        "description": description
                    })

                    connection.execute(
                        """
                        INSERT INTO scan_results
                        (scan_id, port, service, risk, description)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (
                            scan_id,
                            port,
                            service,
                            risk,
                            description
                        )
                    )

                connection.commit()
                connection.close()

            except Exception as e:

                error = f"Nmap scan error: {str(e)}"

    return render_template(
        "index.html",
        results=results,
        error=error
    )


@app.route("/history")
def history():

    connection = get_connection()

    scans = connection.execute(
        "SELECT * FROM scans ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return render_template(
        "history.html",
        scans=scans
    )


@app.route("/scan/<int:scan_id>")
def scan_details(scan_id):

    connection = get_connection()

    scan = connection.execute(
        "SELECT * FROM scans WHERE id = ?",
        (scan_id,)
    ).fetchone()

    results = connection.execute(
        "SELECT * FROM scan_results WHERE scan_id = ?",
        (scan_id,)
    ).fetchall()

    connection.close()

    if not scan:
        return "Scan not found", 404

    return render_template(
        "scan_details.html",
        scan=scan,
        results=results
    )


@app.route("/report/<int:scan_id>")
def report(scan_id):

    connection = get_connection()

    scan = connection.execute(
        "SELECT * FROM scans WHERE id = ?",
        (scan_id,)
    ).fetchone()

    results = connection.execute(
        "SELECT * FROM scan_results WHERE scan_id = ?",
        (scan_id,)
    ).fetchall()

    connection.close()

    if not scan:
        return "Scan not found", 404

    filename = f"reports/scan_{scan_id}.pdf"

    generate_report(
        scan,
        results,
        filename
    )

    return filename


if __name__ == "__main__":

    initialize_database()

    app.run(debug=False)