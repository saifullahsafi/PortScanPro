RISK_LEVELS = {
    21: ("MEDIUM", "FTP may transmit data without encryption."),
    22: ("LOW", "SSH is commonly used for secure remote access."),
    23: ("HIGH", "Telnet transmits data without encryption."),
    25: ("MEDIUM", "SMTP service is exposed."),
    53: ("LOW", "DNS service is exposed."),
    80: ("INFO", "HTTP service is exposed without HTTPS encryption."),
    110: ("MEDIUM", "POP3 may transmit email without encryption."),
    139: ("HIGH", "NetBIOS service is exposed."),
    143: ("MEDIUM", "IMAP service is exposed."),
    443: ("INFO", "HTTPS service is exposed."),
    445: ("HIGH", "SMB service is exposed."),
    3306: ("HIGH", "MySQL database service is exposed."),
    3389: ("HIGH", "RDP remote access service is exposed."),
    5432: ("HIGH", "PostgreSQL database service is exposed."),
    8080: ("MEDIUM", "HTTP proxy/web service is exposed.")
}


def analyze_risk(port):
    return RISK_LEVELS.get(
        port,
        ("INFO", "Open port detected. Review the service configuration.")
    )


if __name__ == "__main__":
    for port in [22, 80, 135, 445, 3306]:
        risk, description = analyze_risk(port)

        print(f"Port {port}: {risk}")
        print(description)
        print()