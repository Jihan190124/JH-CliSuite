# modules/device_scanner.py

import socket
import ipaddress
import threading
from queue import Queue
from colorama import Fore, init

init(autoreset=True)

# Common ports to scan
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

def is_port_open(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def scan_host(ip):
    open_ports = []
    for port in COMMON_PORTS:
        if is_port_open(ip, port):
            open_ports.append(port)
    return open_ports

def worker(ip_queue, results):
    while not ip_queue.empty():
        ip = ip_queue.get()
        ports = scan_host(ip)
        if ports:
            results.append((ip, ports))

def run():
    print(Fore.CYAN + "\n📡 Device & Port Scanner by Jihan\n")
    base_ip = input(Fore.YELLOW + "Enter subnet (e.g., 192.168.1.0/24): ").strip()
    if not base_ip:
        base_ip = "192.168.29.0/24"

    try:
        network = ipaddress.IPv4Network(base_ip, strict=False)
        ip_queue = Queue()
        results = []

        for ip in network.hosts():
            ip_queue.put(str(ip))

        threads = []
        for _ in range(100):  # 100 threads for speed
            t = threading.Thread(target=worker, args=(ip_queue, results))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        if results:
            print(Fore.GREEN + f"\n📍 Devices found on {base_ip}:\n")
            for ip, ports in results:
                print(Fore.MAGENTA + f"{ip} - Open ports: {', '.join(map(str, ports))}")
        else:
            print(Fore.RED + "[!] No active devices or open ports found.")

    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")
