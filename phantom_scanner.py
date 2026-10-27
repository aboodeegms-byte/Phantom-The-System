#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANTOM THE SYSTEM - Vulnerability Scanner Module
Developer: Commander Phantom
Description: Advanced Security Headers & Target Audit Scanner
"""

import sys
import urllib.request
import urllib.parse
import urllib.error

# Neon Blue & Dark Theme Color Codes
NEON_BLUE = "\033[38;2;0;243;255m"
DARK_BLUE = "\033[38;2;0;119;182m"
RESET = "\033[0m"
WHITE = "\033[97m"
GRAY = "\033[90m"

def scanner_banner():
    print(f"\n{NEON_BLUE}====================================================")
    print(f"       PHANTOM VULNERABILITY SCANNER [v2.0]         ")
    print(f"===================================================={RESET}\n")

def scan_target():
    scanner_banner()
    target = input(f"{DARK_BLUE}Enter target URL (e.g., http://testphp.vulnweb.com): {RESET}").strip()
    
    if not target:
        print(f"{WHITE}[!] Error: Target URL cannot be empty.{RESET}")
        return

    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target

    print(f"\n{NEON_BLUE}[*] Initializing scan sequence for target:{RESET} {WHITE}{target}{RESET}")
    print(f"{GRAY}[*] Analyzing HTTP Response & Security Headers...{RESET}\n")

    try:
        req = urllib.request.Request(
            target, 
            headers={'User-Agent': 'Phantom-Security-Scanner/2.0'}
        )
        with urllib.request.urlopen(req, timeout=7) as response:
            status = response.getcode()
            headers = response.info()

            print(f"{NEON_BLUE}[+] Connection Successful! Status Code: {status}{RESET}\n")
            print(f"{DARK_BLUE}--- Security Headers Audit ---{RESET}")

            sec_headers = [
                'Content-Security-Policy', 
                'X-Frame-Options', 
                'X-XSS-Protection', 
                'X-Content-Type-Options',
                'Strict-Transport-Security'
            ]

            for header in sec_headers:
                if header in headers:
                    print(f" {NEON_BLUE}[SECURE]{RESET} {header}: {headers[header]}")
                else:
                    print(f" {GRAY}[VULN/MISSING]{RESET} {header}: Not Configured")

            print(f"\n{NEON_BLUE}[+] Target scan completed successfully.{RESET}")

    except urllib.error.HTTPError as e:
        print(f"\n{WHITE}[!] HTTP Error encountered: {e.code} - {e.reason}{RESET}")
    except urllib.error.URLError as e:
        print(f"\n{WHITE}[!] Connection Failed: {e.reason}{RESET}")
    except Exception as e:
        print(f"\n{WHITE}[!] An unexpected error occurred: {e}{RESET}")

if __name__ == "__main__":
    scan_target()

