from reportlab.pdfgen import canvas


def generate_report(scan, results, filename):
    pdf = canvas.Canvas(filename)

    pdf.setTitle("PortScan Pro Report")

    y = 800

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, y, "PortScan Pro Security Report")

    y -= 40

    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, y, f"Target: {scan['target']}")
    y -= 20
    pdf.drawString(
        50,
        y,
        f"Port Range: {scan['start_port']} - {scan['end_port']}"
    )

    y -= 40

    for result in results:

        pdf.drawString(
            50,
            y,
            f"Port: {result['port']} | "
            f"Service: {result['service']} | "
            f"Risk: {result['risk']}"
        )

        y -= 20

        pdf.drawString(
            70,
            y,
            result["description"]
        )

        y -= 30

        if y < 50:
            pdf.showPage()
            y = 800

    pdf.save()