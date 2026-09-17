import nmap


def detect_services(target, start_port, end_port):

    scanner = nmap.PortScanner()

    port_range = f"{start_port}-{end_port}"

    print(f"Nmap scanning: {target} ports {port_range}")
    
    scanner.scan(
        target,
        port_range,
        arguments="-sV --version-light"
    )

    results = []

    for host in scanner.all_hosts():

        if "tcp" not in scanner[host]:
            continue

        for port in scanner[host]["tcp"]:

            port_info = scanner[host]["tcp"][port]

            if port_info["state"] == "open":

                service = port_info.get("name", "Unknown")
                product = port_info.get("product", "")
                version = port_info.get("version", "")

                service_details = service

                if product:
                    service_details += f" ({product}"

                    if version:
                        service_details += f" {version}"

                    service_details += ")"

                results.append({
                    "port": port,
                    "service": service_details
                })

    return results