import socket


def scan_port(target, port, timeout=0.1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((target, port))

        sock.close()

        if result == 0:
            return "open"
        else:
            return "closed"

    except socket.error:
        return "error"


def scan_ports(target, start_port, end_port):
    results = []

    for port in range(start_port, end_port + 1):
        status = scan_port(target, port)

        results.append({
            "port": port,
            "status": status
        })

    return results
if __name__ == "__main__":
    target = "127.0.0.1"

    results = scan_ports(target, 1, 500)

    for result in results:
        if result["status"] == "open":
            print(f"Port {result['port']} is OPEN")