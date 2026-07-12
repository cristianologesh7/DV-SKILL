import socket
import threading
import pickle
import re

HOST = "127.0.0.1"
PORT = 5000

pattern = re.compile(r"(.+)\|(.+)\|(.+)\|(.+)")

def save_binary(level, record):
    filename = level + ".bin"

    with open(filename, "ab") as file:
        pickle.dump(record, file)

def client_handler(conn, addr):
    print("Connected:", addr)

    buffer = ""

    while True:
        data = conn.recv(1024)

        if not data:
            break

        buffer += data.decode()

        while "\n" in buffer:

            line, buffer = buffer.split("\n", 1)

            match = pattern.match(line)

            if match:

                record = {
                    "Timestamp": match.group(1),
                    "Server": match.group(2),
                    "Level": match.group(3),
                    "Message": match.group(4)
                }

                save_binary(record["Level"], record)

                print(record)

            else:
                print("Invalid Log:", line)

    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Harvest Server Running...")

while True:
    conn, addr = server.accept()

    thread = threading.Thread(target=client_handler, args=(conn, addr))
    thread.start()