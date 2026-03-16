
# Port Scanner v2

A fast multi-threaded TCP port scanner written in Python.
This tool scans ports **1–1024** of a target IP address or domain and reports which ports are open.

---

## Author

**Harsh Mahajan**
Handle: **Dankharsh**

---

## Features

* Multi-threaded port scanning for faster results
* Scans ports **1–1024**
* Accepts **IP address or domain name**
* Real-time **single-line progress bar**
* Displays **sorted open ports**
* Measures **scan execution time**
* Optional export of results to **Desktop (.txt file)**
* Works on **Windows and Linux**

---

## How It Works

The scanner attempts a **TCP connection** to each port using Python's socket library.
If the connection succeeds, the port is considered **open**.

Threading is used to scan multiple ports simultaneously, which greatly improves scanning speed compared to sequential scanning.

---

## Installation

Make sure Python 3 is installed.

Clone the repository:

```
https://github.com/dank-harsh/port-scanner-v2.git
```

Navigate to the project directory:

```
cd port-scanner
```

No external libraries are required.

---

## Usage

Run the scanner:

```
python port_scanner.py
```

Enter the target domain or IP when prompted.

Example:

```
Enter IP or Domain: scanme.nmap.org
```

---

## Example Output

```
PORT SCANNER
Tool by Harsh Mahajan
Version: 2.0
Scan Range: 1-1024

Enter IP or Domain: scanme.nmap.org

Progress: ######################## 100%

Open Ports
----------
22
80

Scan completed in 4.2 seconds
```

---

## Export Results

After scanning, the tool asks whether you want to export the results.

```
Export results to Desktop? (y/n):
```

If you select **y**, a text report will be created on your Desktop.

Example file:

```
scanme.nmap.org_ports.txt
```

Contents:

```
Port Scanner v2
Tool by Harsh Mahajan

Target: scanme.nmap.org
IP: 45.33.32.156

Open Ports
----------
22
80
```

---

## Safe Testing Targets

For testing your scanner safely, you can use:

```
scanme.nmap.org
127.0.0.1
localhost
```

---

## Disclaimer

This tool is created **for educational purposes and authorized security testing only**.

Do **not** scan systems without permission.

Unauthorized scanning may violate network policies or laws.

---

## Version

Current Version: **2.0**

Future improvements may include:

* Service detection (HTTP, SSH, FTP)
* Custom port ranges
* Faster scanning algorithms
* JSON/CSV report export
