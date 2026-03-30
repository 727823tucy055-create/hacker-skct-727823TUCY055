# student_name: VISHWANTH
# roll_number: 727823TUCY055
# project_name: Honeypot Deployment
# date: 2026-03-30

import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 2222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Honeypot running on port 2222...")

while True:
    client, addr = server.accept()
    print(f"[ALERT] Connection from {addr}")

    with open("logs/honeypot.log", "a") as f:
        f.write(f"{datetime.now()} - Connection from {addr}\n")

    try:
        # Fake SSH banner
        client.send(b"SSH-2.0-OpenSSH_7.4\r\n")
        
        # Keep connection alive a bit
        data = client.recv(1024)

    except:
        pass

    client.close()
