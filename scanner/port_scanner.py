import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(target, port, timeout=0.2):
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

    with ThreadPoolExecutor(max_workers=100) as executor:

        statuses = executor.map(
            lambda port: scan_port(target, port),
            range(start_port, end_port + 1)
        )

        for port, status in zip(
            range(start_port, end_port + 1),
            statuses
        ):
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