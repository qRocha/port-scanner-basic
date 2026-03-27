import socket
import threading

target = input("Enter target IP: ")

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        if s.connect_ex((target, port)) == 0:
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "No banner"

            print(f"Port {port} is open | Service: {banner}")

        s.close()

    except:
        pass

threads = []

for port in range(1, 1025
