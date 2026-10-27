#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANTOM THE SYSTEM - Fast TCP Port Scanner (`phantom_ports.py`)
Developer: Commander Phantom
Description: Scans common target ports for active services and logs results automatically.
"""

import socket
import datetime
import sys

NEON_BLUE = "\033[38;2;0;243;255m"
DARK_BLUE = "\033[38;2;0;119;182m"
RESET = "\033[0m"
WHITE = "\033[97m"
GRAY = "\033[90m"

def scan_ports():
    print(f"\n{NEON_BLUE}====================================================")
    print(f"       PHANTOM FAST TCP PORT AUDIT MODULE           ")
    print(f"===================================================={RESET}\n")
    
    target_input = input(f"{DARK_BLUE}[?] Enter target IP or domain (Default: 127.0.0.1): {RESET}").strip()
    if not target_input:
        target = "127.0.0.1"
    else:
        target = target_input
        
    print(f"\n{GRAY}[*] Target acquired: {target}{RESET}")
    print(f"{GRAY}[*] Scanning common tactical ports (21, 22, 80, 443, 3306, 5000, 8080)...{RESET}\n")
    
    # Common ports to check
    ports_to_check = [21, 22, 80, 443, 3306, 5000, 8080]
    
    report_lines = []
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines.append(f"--- PHANTOM PORT SCAN REPORT ---")
    report_lines.append(f"Target: {target}")
    report_lines.append(f"Time: {timestamp}")
    
    open_ports_found = False
    
    for port in ports_to_check:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            result = s.connect_ex((target, port))
            if result == 0:
                service_msg = f"[+] Port {port}: OPEN"
                print(f"{WHITE}{service_msg}{RESET}")
                report_lines.append(service_msg)
                open_ports_found = True
            else:
                print(f"{GRAY}[-] Port {port}: Closed{RESET}")
            s.close()
        except KeyboardInterrupt:
            print(f"\n{WHITE}[!] Scan aborted by user.{RESET}")
            sys.exit()
        except socket.gaierror:
            print(f"\n{WHITE}[!] Error: Hostname could not be resolved.{RESET}")
            report_lines.append(f"[!] Error: Hostname could not be resolved.")
            break
        except socket.error:
            print(f"\n{WHITE}[!] Could not connect to server.{RESET}")
            report_lines.append(f"[!] Could not connect to server.")
            break

    if not open_ports_found:
        report_lines.append("[-] No open ports detected among targeted list.")

    # Auto-save report to shared log file
    filename = "phantom_report.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n".join(report_lines) + "\n" + "="*40 + "\n")
        
    print(f"\n{NEON_BLUE}[*] Port scan report successfully saved to: {filename}{RESET}\n")

if __name__ == "__main__":
    scan_ports()

