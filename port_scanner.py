import socket

target = input("192.168.18.20: ")

print(f"\nScanning {target}...\n")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)

    result = s.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print(f"Port {port} ({service}) is OPEN")

    s.close()

print("\nScan Completed!")
