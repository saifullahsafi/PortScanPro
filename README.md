PORTSCAN PRO
============

Network Port Scanner & Security Analyzer

DESCRIPTION
-----------
PortScan Pro is a Python Flask-based cybersecurity tool that scans TCP ports, identifies common services, analyzes security risks, stores scan history, and generates PDF security reports.

FEATURES
--------
- TCP port scanning
- IP address and domain validation
- Service detection
- Port risk analysis
- SQLite database
- Scan history
- Detailed scan results
- Risk-level indicators
- PDF security reports
- Responsive web dashboard
- Multi-threaded port scanning

TECHNOLOGIES
------------
- Python 3
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- ReportLab
- Python Socket
- ThreadPoolExecutor

PROJECT STRUCTURE
-----------------
PortScanPro/
|
|-- app.py
|-- requirements.txt
|-- .gitignore
|
|-- scanner/
|   |-- __init__.py
|   |-- port_scanner.py
|   |-- service_detector.py
|   |-- target_validator.py
|   |-- risk_analyzer.py
|
|-- database/
|   |-- __init__.py
|   |-- database.py
|
|-- templates/
|   |-- index.html
|   |-- history.html
|   |-- scan_details.html
|
|-- static/
|   |-- css/
|   |   |-- style.css
|   |-- js/
|       |-- app.js
|
|-- reports/
|   |-- report_generator.py
|
|-- portscan.db
|-- .venv/

INSTALLATION
------------
1. Clone the repository.

2. Create a virtual environment:

   python -m venv .venv

3. Activate the virtual environment.

   Windows:

   .venv\Scripts\activate

4. Install dependencies:

   pip install -r requirements.txt

5. Run the application:

   python app.py

6. Open the application in your browser:

   http://127.0.0.1:5000

USAGE
-----
1. Enter an IP address or domain.
2. Enter the starting port.
3. Enter the ending port.
4. Click START SCAN.
5. View detected open ports and security risks.
6. Open Scan History to view previous scans.
7. Open a Scan ID to view detailed results.
8. Generate a PDF security report.

IMPORTANT
---------
Only scan systems and networks that you own or have explicit permission to test.

AUTHOR
------
Saif Ullah

PROJECT
-------
PortScan Pro

STATUS
------
Completed and functional.
