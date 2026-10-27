import sys
import socket

NEON_BLUE = "\033[38;2;0;243;255m"
DARK_BLUE = "\033[38;2;0;119;182m"
RESET = "\033[0m"
WHITE = "\033[97m"
GRAY = "\033[90m"

print(f"\n{NEON_BLUE}=== PHANTOM PORT SCANNER ==={RESET}\n")
target = input(f"{DARK_BLUE}Enter target IP (e.g. 127.0.0.1): {RESET}").strip()

ports = [21, 22, 80, 443, 3306, 8080]
for p in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((target, p)) == 0:
        print(f" {NEON_BLUE}[OPEN]{RESET} Port {p}")
    else:
        print(f" {GRAY}[CLOSED]{RESET} Port {p}")
    s.close()
print(f"\n{NEON_BLUE}[+] Scan Finished!{RESET}")

