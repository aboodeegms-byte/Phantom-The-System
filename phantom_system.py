#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANTOM THE SYSTEM - Main Command Center
Developer: Commander Phantom
Style: Black & Neon Blue CLI Interface
"""

import os
import sys
import subprocess
import time

# Neon Blue & Black Theme Color Codes
NEON_BLUE = "\033[38;2;0;243;255m"
DARK_BLUE = "\033[38;2;0;119;182m"
BG_BLACK = "\033[48;2;10;10;12m"
BOLD = "\033[1m"
RESET = "\033[0m"
WHITE = "\033[97m"
GRAY = "\033[90m"

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    clear_screen()
    banner = f"""{BG_BLACK}{NEON_BLUE}{BOLD}
    ===============================================================
     ____  _   _    _    _  _____ ___  __  __   ____  _  __   __
    |  _ \| | | |  / \  | \|_   _/ _ \|  \/  | / ___|| | \ \ / /
    | |_) | |_| | / _ \ | .` || || | | | |\/| | \___ \| |  \ V / 
    |  __/|  _  |/ ___ \| |\ || || |_| | |  | |  ___) | |___| |  
    |_|   |_| |_/_/   \_\_| \_||_| \___/|_|  |_| |____/|_____|_|  
                                                                   
                  [ COMMANDER PHANTOM SYSTEM v1.0.0 ]               
    ===============================================================
    {RESET}"""
    print(banner)

def main_menu():
    while True:
        print_banner()
        print(f"{DARK_BLUE}[+] Select Operations Module:{RESET}\n")
        print(f" {NEON_BLUE}[1]{RESET} {WHITE}Vulnerability Scanner (XSS & Injection){RESET}")
        print(f" {NEON_BLUE}[2]{RESET} {WHITE}Port Scanner (Fast TCP Target Audit){RESET}")
        print(f" {NEON_BLUE}[3]{RESET} {WHITE}Launch Local Vulnerable Lab (Flask Server){RESET}")
        print(f" {NEON_BLUE}[4]{RESET} {WHITE}Phantom Co-Pilot Terminal Assistant{RESET}")
        print(f" {NEON_BLUE}[0]{RESET} {GRAY}Exit Operations{RESET}\n")
        
        choice = input(f"{NEON_BLUE}{BOLD}PHANTOM-CLI > {RESET}").strip()
        
        if choice == '1':
            print(f"\n{DARK_BLUE}[*] Launching Phantom Scanner...{RESET}")
            subprocess.run([sys.executable, "phantom_scanner.py"])
            input(f"\n{GRAY}Press Enter to return to main menu...{RESET}")
        elif choice == '2':
            print(f"\n{DARK_BLUE}[*] Launching Port Scanner...{RESET}")
            subprocess.run([sys.executable, "phantom_ports.py"])
            input(f"\n{GRAY}Press Enter to return to main menu...{RESET}")
        elif choice == '3':
            print(f"\n{DARK_BLUE}[*] Launching Weaker App Lab...{RESET}")
            subprocess.run([sys.executable, "weaker_app.py"])
            input(f"\n{GRAY}Press Enter to return to main menu...{RESET}")
        elif choice == '4':
            print(f"\n{NEON_BLUE}[+] Phantom Co-Pilot Active. Type 'exit' to return.{RESET}")
            while True:
                cmd = input(f"{DARK_BLUE}Co-Pilot > {RESET}").strip()
                if cmd.lower() == 'exit':
                    break
                print(f"{GRAY}[Assistant] Command logged/processed: {cmd}{RESET}")
        elif choice == '0':
            print(f"\n{NEON_BLUE}[*] Shutting down Phantom System... Stay Secure!{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{WHITE}[!] Invalid selection, try again.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()

