#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANTOM THE SYSTEM - Web Vulnerability & Header Scanner with Auto-Logging & Validation
Developer: Commander Phantom
Description: Scans target URLs for basic security headers and XSS, saving reports automatically.
"""

import urllib.request
import urllib.parse
import urllib.error
import datetime

NEON_BLUE = "\033[38;2;0;243;255m"
DARK_BLUE = "\033[38;2;0;119;182m"
RESET = "\033[0m"
WHITE = "\033[97m"
GRAY = "\033[90m"

def scan_target():
    print(f"\n{NEON_BLUE}====================================================")
    print(f"     PHANTOM WEB SCANNER + AUTO-LOGGING SYSTEM      ")
    print(f"===================================================={RESET}\n")

    target = input(f"{DARK_BLUE}[?] Enter target URL (e.g. http://127.0.0.1:5000): {RESET}").strip()

    # If no input or invalid url format, default or prompt
    if not target:
        target = "http://127.0.0.1:5000"
        print(f"{GRAY}[*] No URL provided. Defaulting to local lab: {target}{RESET}")
    elif not target.startswith("http://") and not target.startswith("https://"):
        print(f"{WHITE}[!] Invalid URL format! It must start with http:// or https://{RESET}")
        print(f"{GRAY}[*] Auto-correcting by prepending http://{RESET}")
        target = "http://" + target

    report_lines = []
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines.append(f"--- PHANTOM SECURITY SCAN REPORT ---")
    report_lines.append(f"Target: {target}")
    report_lines.append(f"Time: {timestamp}\n")

    print(f"\n{GRAY}[*] Scanning target headers for {target}...{RESET}")
    try:
        req = urllib.request.Request(target, headers={'User-Agent': 'PhantomScanner/1.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            headers = response.info()
            status_msg = f"[+] Response Status: {response.status} {response.reason}"
            print(f"\n{WHITE}{status_msg}{RESET}")
            report_lines.append(status_msg)

            report_lines.append("[+] Security Headers Check:")
            print(f"{WHITE}[+] Security Headers Check:{RESET}")
            sec_headers = ['X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy', 'Server']
            for h in sec_headers:
                if h in headers:
                    line = f"  - {h}: {headers[h]}"
                    print(line)
                    report_lines.append(line)
                else:
                    line = f"  - [!] Missing Header: {h}"
                    print(f"{NEON_BLUE}{line}{RESET}")
                    report_lines.append(line)

            # Basic XSS Parameter Check simulation
            test_payload = "<script>alert(1)</script>"
            test_url = f"{target}/greet?name={urllib.parse.quote(test_payload)}"
            print(f"\n{GRAY}[*] Testing XSS reflection payload on endpoint...{RESET}")
            test_req = urllib.request.Request(test_url, headers={'User-Agent': 'PhantomScanner/1.0'})
            with urllib.request.urlopen(test_req, timeout=5) as test_resp:
                body = test_resp.read().decode('utf-8', errors='ignore')
                if test_payload in body:
                    xss_msg = "[+] Vulnerability Found: Reflected XSS detected at endpoint!"
                    print(f"{NEON_BLUE}{xss_msg}{RESET}")
                    report_lines.append(xss_msg)
                else:
                    xss_msg = "[-] Payload not reflected directly in standard output."
                    print(f"{GRAY}{xss_msg}{RESET}")
                    report_lines.append(xss_msg)

    except urllib.error.URLError as e:
        err_msg = f"[!] Connection Error: {e.reason}. Make sure weaker_app.py is running!"
        print(f"\n{WHITE}{err_msg}{RESET}")
        report_lines.append(err_msg)
    except Exception as e:
        err_msg = f"[!] An error occurred: {e}"
        print(f"\n{WHITE}{err_msg}{RESET}")
        report_lines.append(err_msg)

    # Auto-save report to file
    filename = "phantom_report.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n".join(report_lines) + "\n" + "="*40 + "\n")

    print(f"\n{NEON_BLUE}[*] Scan report successfully saved to: {filename}{RESET}\n")

if __name__ == "__main__":
    scan_target()


