RISK_LEVELS = {
    21: ("MEDIUM", "FTP may transmit data without encryption."),
    22: ("LOW", "SSH provides secure remote administration."),
    23: ("HIGH", "Telnet transmits data without encryption."),
    25: ("MEDIUM", "SMTP service is exposed."),
    53: ("LOW", "DNS service is exposed."),
    80: ("INFO", "HTTP service is exposed without HTTPS encryption."),
    110: ("MEDIUM", "POP3 may transmit email without encryption."),
    139: ("HIGH", "NetBIOS service is exposed."),
    143: ("MEDIUM", "IMAP may transmit email without encryption."),
    443: ("INFO", "HTTPS service is exposed."),
    445: ("HIGH", "SMB service is exposed."),
    3306: ("HIGH", "MySQL database service is exposed."),
    3389: ("HIGH", "RDP remote access service is exposed."),
    5432: ("HIGH", "PostgreSQL database service is exposed."),
    8080: ("MEDIUM", "HTTP proxy/web service is exposed.")
}


SERVICE_RISKS = {
    "telnet": (
        "HIGH",
        "Telnet is an unencrypted remote-access service."
    ),

    "ftp": (
        "MEDIUM",
        "FTP may transmit credentials and data without encryption."
    ),

    "microsoft-ds": (
        "HIGH",
        "SMB service is exposed and should be properly secured."
    ),

    "netbios": (
        "HIGH",
        "NetBIOS service is exposed."
    ),

    "msrpc": (
        "MEDIUM",
        "Microsoft RPC service is exposed."
    ),

    "vmware-auth": (
        "MEDIUM",
        "VMware authentication service is exposed."
    ),

    "tcpwrapped": (
        "INFO",
        "The service restricts Nmap's probing."
    )
}


def analyze_risk(port, service=""):

    service_name = service.lower()

    for service_key, risk_data in SERVICE_RISKS.items():

        if service_key in service_name:
            return risk_data

    return RISK_LEVELS.get(
        port,
        (
            "INFO",
            "Open port detected. Review the service configuration."
        )
    )