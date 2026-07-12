import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

logs = [
    f"{datetime.now()}|ORDER|INFO|Order Created\n",
    f"{datetime.now()}|PAYMENT|INFO|Payment Successful\n",
    f"{datetime.now()}|INVENTORY|ERROR|Item Out of Stock\n",
    f"{datetime.now()}|DELIVERY|INFO|Shipment Assigned\n"
]

for log in logs:
    client.send(log.encode())

client.close()