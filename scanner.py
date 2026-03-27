import socket
import threading

target = input("Enter target IP: ")

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    if s.connect_ex((target, port)) == 0:
        print(f"Port {port} is open")

    s.close()

threads = []

for port in range(1, 1025):
    t = threading.Thread(target=scan, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
