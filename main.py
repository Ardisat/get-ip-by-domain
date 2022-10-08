import socket

def get_ip_by_domain(domain: str) -> str:
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror as error:
        return 'Invalid hostname'