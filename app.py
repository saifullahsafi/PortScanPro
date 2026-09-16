from flask import Flask, render_template, request

from scanner.target_validator import validate_target
from scanner.port_scanner import scan_ports
from scanner.service_detector import detect_service
from scanner.risk_analyzer import analyze_risk


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
        else:
            scanned_ports = scan_ports(
                target_ip,
                start_port,
                end_port
            )

            for result in scanned_ports:
                if result["status"] == "open":
                    port = result["port"]
                    service = detect_service(target_ip, port)
                    risk, description = analyze_risk(port)

                    results.append({
                        "port": port,
                        "service": service,
                        "risk": risk,
                        "description": description
                    })

    return render_template(
        "index.html",
        results=results,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)