import socket


COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP Proxy"
}


def detect_service(target, port):
    if port in COMMON_SERVICES:
        return COMMON_SERVICES[port]

    try:
        service = socket.getservbyport(port, "tcp")
        return service.upper()

    except OSError:
        return "Unknown"


if __name__ == "__main__":
    target = "127.0.0.1"

    for port in [22, 80, 135, 443, 445]:
        service = detect_service(target, port)
        print(f"Port {port}: {service}")