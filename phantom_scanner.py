#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANTOM THE SYSTEM - Web Vulnerability & Header Scanner
Developer: Commander Phantom
Description: Scans target URLs for basic security headers and XSS vulnerabilities.
"""

import urllib.request
import urllib.parse
import urllib.error

NEON_BLUE = "\033[38;2;0;243;255m"
DARK_BLUE = "\033[38;2;0;119;182m"
RESET = "\033[0m"
WHITE = "\033[97m"
GRAY = "\033[90m"

def scan_target():
    print(f"\n{NEON_BLUE}====================================================")
    print(f"         PHANTOM WEB SECURITY SCANNER               ")
    print(f"===================================================={RESET}\n")

    target = input(f"{DARK_BLUE}[?] Enter target URL (e.g. http://127.0.0.1:5000): {RESET}").strip()
    if not target:
        target = "http://127.0.0.1:5000"
        print(f"{GRAY}[*] No URL provided. Defaulting to local lab: {target}{RESET}")

    print(f"\n{GRAY}[*] Scanning target headers for {target}...{RESET}")
    try:
        req = urllib.request.Request(target, headers={'User-Agent': 'PhantomScanner/1.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            headers = response.info()
            print(f"\n{WHITE}[+] Response Status: {response.status} {response.reason}{RESET}")
            print(f"{WHITE}[+] Security Headers Check:{RESET}")

            sec_headers = ['X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy', 'Server']
            for h in sec_headers:
                if h in headers:
                    print(f"  - {h}: {headers[h]}")
                else:
                    print(f"  {NEON_BLUE}- [!] Missing Header: {h}{RESET}")

            # Basic XSS Parameter Check simulation
            test_payload = "<script>alert(1)</script>"
            test_url = f"{target}/greet?name={urllib.parse.quote(test_payload)}"
            print(f"\n{GRAY}[*] Testing XSS reflection payload on endpoint...{RESET}")
            test_req = urllib.request.Request(test_url, headers={'User-Agent': 'PhantomScanner/1.0'})
            with urllib.request.urlopen(test_req, timeout=5) as test_resp:
                body = test_resp.read().decode('utf-8', errors='ignore')
                if test_payload in body:
                    print(f"{NEON_BLUE}[+] Vulnerability Found: Reflected XSS detected at endpoint!{RESET}")
                else:
                    print(f"{GRAY}[-] Payload not reflected directly in standard output.{RESET}")

    except urllib.error.URLError as e:
        print(f"\n{WHITE}[!] Connection Error: {e.reason}. Make sure weaker_app.py is running!{RESET}")
    except Exception as e:
        print(f"\n{WHITE}[!] An error occurred: {e}{RESET}")

if __name__ == "__main__":
    scan_target()

