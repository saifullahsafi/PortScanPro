import socket
import ipaddress


def validate_target(target):
    try:
        ipaddress.ip_address(target)
        return target

    except ValueError:
        try:
            ip = socket.gethostbyname(target)
            return ip

        except socket.gaierror:
            return None


if __name__ == "__main__":
    target = input("Enter IP or domain: ")

    result = validate_target(target)

    if result:
        print(f"Valid target: {result}")
    else:
        print("Invalid target")