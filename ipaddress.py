import socket
hostname = socket.gethostname()
ipadder = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP Address: {ipadder}")
