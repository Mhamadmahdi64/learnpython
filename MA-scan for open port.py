import threading
import time
import socket

ip_address = input("Enter IP address to scan open ports: ")

def scan_port(port):
    host_ip = ip_address
    status = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host_ip, port))
        status = True
    except:
        status = False
    finally:
        s.close()
    if status:
        print("Port {} is open".format(port))

start_time = time.time()
threads = []

for i in range(0, 65000):
    thread = threading.Thread(target=scan_port, args=[i])
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

end_time = time.time()
print("Scanning process of all ports took {} seconds".format(end_time - start_time))
