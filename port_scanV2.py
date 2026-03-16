import socket
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

VERSION = "2.0"

print(r"""
██████╗  ██████╗ ██████╗ ████████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ ██╗   ██╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝     ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗██║   ██║╚════██╗
██████╔╝██║   ██║██████╔╝   ██║        ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝██║   ██║ █████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║        ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔═══╝ 
██║     ╚██████╔╝██║  ██║   ██║        ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║ ╚████╔╝ ███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝
""")

print("PORT SCANNER")
print("Tool by Harsh Mahajan")
print("Version:", VERSION)
print("Scan Range: 1-1024\n")

target = input("Enter IP or Domain: ")

try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Could not resolve domain.")
    exit()

print("\nScanning Target:", ip)
print("Starting scan...\n")

open_ports = []
scanned_ports = 0
total_ports = 1024
lock = threading.Lock()

start_time = time.time()


def scan_port(port):
    global scanned_ports

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip, port))

    with lock:
        scanned_ports += 1

        if result == 0:
            open_ports.append(port)

        progress = scanned_ports / total_ports
        bar_length = 25
        filled = int(bar_length * progress)
        bar = "#" * filled + "." * (bar_length - filled)
        percent = int(progress * 100)

        print(f"\rProgress: {bar} {percent}%", end="", flush=True)

    s.close()


with ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1, 1025):
        executor.submit(scan_port, port)

end_time = time.time()

print("\n\nScan complete.\n")

open_ports.sort()

print("Open Ports")
print("----------")

for port in open_ports:
    print(port)

scan_time = round(end_time - start_time, 2)
print(f"\nScan completed in {scan_time} seconds.")

# Ask user if they want to export results
save = input("\nExport results to Desktop? (y/n): ").lower()

if save == "y":
    desktop = Path.home() / "Desktop"
    filename = f"{target}_ports.txt"
    file_path = desktop / filename

    with open(file_path, "w") as f:
        f.write("Port Scanner v2\n")
        f.write("Tool by Harsh Mahajan\n\n")
        f.write(f"Target: {target}\n")
        f.write(f"IP: {ip}\n\n")
        f.write("Open Ports\n")
        f.write("----------\n")

        for port in open_ports:
            f.write(str(port) + "\n")

        f.write(f"\nScan time: {scan_time} seconds\n")

    print(f"\nResults saved to: {file_path}")
