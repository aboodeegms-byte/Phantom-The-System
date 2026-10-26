import os
import sys

def banner():
    print("""
\033[1;36m=========================================================
      🛡️ PHANTOM THE SYSTEM - ADVANCED FRAMEWORK 🛡️
      Cybersecurity Operations Center (Level 5)
=========================================================\033[0m
""")

def smart_ai_commander(command):
    cmd = command.lower().strip()
    print(f"\n[🤖 PHANTOM CO-PILOT] Analyzing command: '{command}'...")
    
    if "scan" in cmd or "vulnerability" in cmd:
        print("[+] Match found: Running Phantom Scanner...")
        os.system("python phantom_scanner.py")
    elif "port" in cmd or "ports" in cmd:
        print("[+] Match found: Running Port Scanner...")
        os.system("python phantom_ports.py")
    elif "lab" in cmd or "server" in cmd:
        print("[+] Match found: Starting Vulnerable Lab...")
        os.system("python vulnerable_app.py")
    elif "info" in cmd or "system" in cmd:
        print("[+] Match found: Checking Termux packages...")
        os.system("pkg list-installed | wc -l")
    elif "exit" in cmd or "quit" in cmd:
        print("\n\033[1;31m[!] Shutting down Phantom The System.. Stay secure, Commander! 🚀\033[0m")
        sys.exit()
    else:
        print("[-] Unknown command! Try typing: 'scan', 'ports', 'lab', 'info', or 'exit'.")

def main_menu():
    while True:
        banner()
        print("\033[1;32m[ Main Operations - Commander Phantom ]\033[0m")
        print("1. 🔍 Run Vulnerability Scanner (Phantom Scanner v2.0)")
        print("2. 🌐 Run Port Scanner (Phantom Ports v1.0)")
        print("3. 🧪 Run Vulnerable Lab Environment (Phantom Lab)")
        print("4. 🤖 Launch PHANTOM CO-PILOT (AI Smart Terminal)")
        print("5. 🛠️ System & Termux Packages Management")
        print("0. 🚪 Exit System")
        
        choice = input("\n[?] Enter choice OR type direct command (e.g., 'ports'): ")
        
        if choice == '1':
            os.system("python phantom_scanner.py")
            input("\n[ Press Enter to return ]")
        elif choice == '2':
            os.system("python phantom_ports.py")
            input("\n[ Press Enter to return ]")
        elif choice == '3':
            os.system("python vulnerable_app.py")
            input("\n[ Press Enter to return ]")
        elif choice == '4':
            user_input = input("\n[🤖 PHANTOM CO-PILOT] Enter your command, Commander: ")
            smart_ai_commander(user_input)
            input("\n[ Press Enter to return ]")
        elif choice == '5':
            os.system("pkg list-installed | wc -l")
            input("\n[ Press Enter to return ]")
        elif choice == '0':
            print("\n\033[1;31m[!] Shutting down.. Stay secure, Commander! 🚀\033[0m")
            sys.exit()
        else:
            smart_ai_commander(choice)
            input("\n[ Press Enter to return ]")

if __name__ == "__main__":
    main_menu()


