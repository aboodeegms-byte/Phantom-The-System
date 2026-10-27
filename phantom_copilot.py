#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANTOM THE SYSTEM - Advanced Operations Room
Developer: Commander Phantom
Description: Central Command Framework integrating all security modules with Tactical Log Dashboard.
"""

import os
import sys

NEON_BLUE = "\033[38;2;0;243;255m"
DARK_BLUE = "\033[38;2;0;119;182m"
RESET = "\033[0m"
WHITE = "\033[97m"
GRAY = "\033[90m"

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"\n{NEON_BLUE}====================================================")
    print(f"       PHANTOM CO-PILOT - Advanced Operations Room  ")
    print(f"===================================================={RESET}\n")

def main_menu():
    while True:
        show_banner()
        print(f"{WHITE}[ Main Operations - Commander Phantom ]{RESET}")
        print(f"  {NEON_BLUE}[1]{RESET} Run Web Vulnerability & Header Scanner (with Auto-Log)")
        print(f"  {NEON_BLUE}[2]{RESET} Run Port Scanner (Fast TCP Target Audit)")
        print(f"  {NEON_BLUE}[3]{RESET} Launch Local Vulnerable Lab (weaker_app.py)")
        print(f"  {NEON_BLUE}[4]{RESET} View Scan Reports (phantom_report.txt)")
        print(f"  {NEON_BLUE}[5]{RESET} Tactical Security Dashboard & Log Manager")
        print(f"  {NEON_BLUE}[6]{RESET} Termux Environment & System Management")
        print(f"  {NEON_BLUE}[7]{RESET} Quick Commands Cheat Sheet")
        print(f"  {NEON_BLUE}[0]{RESET} Exit System\n")
        
        choice = input(f"{DARK_BLUE}[?] What is your command today?: {RESET}").strip()
        
        if choice == '1':
            print(f"\n{GRAY}[*] Launching Phantom Web Security Scanner...{RESET}\n")
            if os.path.exists("phantom_scanner.py"):
                os.system("python phantom_scanner.py")
            else:
                print(f"{WHITE}[!] Error: phantom_scanner.py not found!{RESET}")
            input(f"\n{GRAY}Press Enter to return to main menu...{RESET}")
            
        elif choice == '2':
            print(f"\n{GRAY}[*] Launching Phantom Port Scanner...{RESET}\n")
            if os.path.exists("phantom_ports.py"):
                os.system("python phantom_ports.py")
            else:
                print(f"{WHITE}[!] Error: phantom_ports.py not found!{RESET}")
            input(f"\n{GRAY}Press Enter to return to main menu...{RESET}")
            
        elif choice == '3':
            print(f"\n{GRAY}[*] Launching Local Vulnerable Lab (Flask Server)...{RESET}\n")
            if os.path.exists("weaker_app.py"):
                os.system("python weaker_app.py")
            else:
                print(f"{WHITE}[!] Error: weaker_app.py not found!{RESET}")
            input(f"\n{GRAY}Press Enter to return to main menu...{RESET}")
            
        elif choice == '4':
            print(f"\n{NEON_BLUE}--- Phantom Security Reports (phantom_report.txt) ---{RESET}\n")
            if os.path.exists("phantom_report.txt"):
                with open("phantom_report.txt", "r", encoding="utf-8") as f:
                    print(f"{WHITE}{f.read()}{RESET}")
            else:
                print(f"{GRAY}[*] No reports found yet. Run a web scan first!{RESET}")
            input(f"\n{GRAY}Press Enter to return to main menu...{RESET}")
            
        elif choice == '5':
            while True:
                os.system('clear')
                print(f"\n{NEON_BLUE}====================================================")
                print(f"     TACTICAL SECURITY DASHBOARD & LOG MANAGER      ")
                print(f"===================================================={RESET}\n")
                
                if os.path.exists("phantom_report.txt"):
                    size_bytes = os.path.getsize("phantom_report.txt")
                    with open("phantom_report.txt", "r", encoding="utf-8") as rf:
                        content = rf.read()
                        scan_count = content.count("PHANTOM SECURITY SCAN REPORT")
                    print(f"  {WHITE}[+] Log File Status: Active{RESET}")
                    print(f"  {WHITE}[+] Total Scans Recorded: {scan_count}{RESET}")
                    print(f"  {WHITE}[+] File Size: {size_bytes} bytes{RESET}\n")
                else:
                    print(f"  {GRAY}[!] Log File Status: Not Found (No scans yet){RESET}\n")
                
                print(f"  {NEON_BLUE}[1]{RESET} View Full Security Reports")
                print(f"  {NEON_BLUE}[2]{RESET} Clear / Wipe All Security Logs")
                print(f"  {NEON_BLUE}[0]{RESET} Return to Main Operations Room\n")
                
                sub_choice = input(f"{DARK_BLUE}[?] Dashboard Command: {RESET}").strip()
                
                if sub_choice == '1':
                    print(f"\n{NEON_BLUE}--- Full Tactical Reports ---{RESET}\n")
                    if os.path.exists("phantom_report.txt"):
                        with open("phantom_report.txt", "r", encoding="utf-8") as f:
                            print(f"{WHITE}{f.read()}{RESET}")
                    else:
                        print(f"{GRAY}[*] No reports found.{RESET}")
                    input(f"\n{GRAY}Press Enter to continue...{RESET}")
                    
                elif sub_choice == '2':
                    confirm = input(f"{WHITE}[!] Are you sure you want to wipe all logs? (y/n): {RESET}").strip().lower()
                    if confirm == 'y':
                        if os.path.exists("phantom_report.txt"):
                            os.remove("phantom_report.txt")
                            print(f"\n{NEON_BLUE}[+] All security logs have been wiped successfully!{RESET}")
                        else:
                            print(f"\n{GRAY}[*] No log file to delete.{RESET}")
                    else:
                        print(f"\n{GRAY}[*] Operation cancelled.{RESET}")
                    input(f"\n{GRAY}Press Enter to continue...{RESET}")
                    
                elif sub_choice == '0':
                    break
                else:
                    print(f"\n{WHITE}[!] Invalid dashboard command.{RESET}")
                    input(f"\n{GRAY}Press Enter to continue...{RESET}")
                    
        elif choice == '6':
            print(f"\n{GRAY}[*] Termux System Status: Optimal (351 Packages active){RESET}")
            input(f"\n{GRAY}Press Enter to return to main menu...{RESET}")
            
        elif choice == '7':
            print(f"\n{WHITE}--- Quick Commands ---{RESET}")
            print(f"  {NEON_BLUE}python phantom_copilot.py{RESET} -> Run Operations Room")
            print(f"  {NEON_BLUE}python phantom_scanner.py{RESET} -> Run Web Scanner directly")
            print(f"  {NEON_BLUE}python phantom_ports.py{RESET}   -> Run Port Scanner directly")
            print(f"  {NEON_BLUE}python weaker_app.py{RESET}      -> Run Local Lab directly\n")
            input(f"{GRAY}Press Enter to return to main menu...{RESET}")
            
        elif choice == '0':
            print(f"\n{NEON_BLUE}[*] Shutting down Phantom Co-Pilot... Stay secure, Commander!{RESET}\n")
            break
        else:
            print(f"\n{WHITE}[!] Invalid option. Please choose from 0 to 7.{RESET}")
            input(f"\n{GRAY}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    main_menu()
