# Python Port Scanner

A simple Python port scanner written in Python.

## Features

- Scans TCP ports (1-1024)
- Detects common services
- Fast and lightweight

## Usage

```bash
python3 port_scanner.py
```

Enter target IP:

```text
192.168.18.20
```

## Example Output

```text
Scanning 192.168.18.20...

Port 135 (epmap) is OPEN
Port 139 (netbios-ssn) is OPEN
Port 445 (microsoft-ds) is OPEN

Scan Completed!
```
