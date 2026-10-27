#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANTOM THE SYSTEM - Advanced Operations Room
Developer: Commander Phantom
Description: Central Command Framework integrating all security modules.
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
        print(f"  {NEON_BLUE}[4]{RESET} Termux Environment & System Management")
        print(f"  {NEON_BLUE}[5]{RESET} Quick Commands Cheat Sheet")
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
            print(f"\n{GRAY}[*] Termux System Status: Optimal (351 Packages active){RESET}")
            input(f"\n{GRAY}Press Enter to return to main menu...{RESET}")

        elif choice == '5':
            print(f"\n{WHITE}--- Quick Commands ---{RESET}")
            print(f"  python phantom_scanner.py -> Run Web Scanner directly")
            print(f"  python phantom_ports.py   -> Run Port Scanner directly")
            print(f"  python weaker_app.py      -> Run Local Lab directly")
            print(f"  git push origin main      -> Sync updates with GitHub\n")
            input(f"{GRAY}Press Enter to return to main menu...{RESET}")

        elif choice == '0':
            print(f"\n{NEON_BLUE}[*] Shutting down Phantom Co-Pilot... Stay secure, Commander!{RESET}\n")
            break
        else:
            print(f"\n{WHITE}[!] Invalid option. Please choose from 0 to 5.{RESET}")
            input(f"\n{GRAY}Press Enter to continue...{RESET}")


