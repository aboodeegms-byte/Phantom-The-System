import socket
import sys

BANNER = """
=========================================
    🛡️ PHANTOM PORT SCANNER - v1.0 🛡️
    أداة فحص البوابات السريعة
=========================================
"""

def scan_ports(target_ip):
    print(BANNER)
    print(f"[*] جاري فحص البوابات الأساسية للهدف: {target_ip}\n")
    
    # قائمة بأهم البوابات الشائعة للاختبار
    ports_to_scan = [21, 22, 80, 443, 3306, 5000, 8080]
    
    for port in ports_to_scan:
        try:
            # إنشاء اتصال Socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"[+] البوابة (Port {port}) مفتوحة ومتاحة 🟢")
            else:
                print(f"[-] البوابة (Port {port}) مغلقة 🔴")
                
            s.close()
        except socket.error:
            print(f"[-] تعذر الاتصال بالهدف.")
            break
            
    print("\n[+] انتهى فحص البوابات بنجاح يا قائد!")

if __name__ == "__main__":
    target = "127.0.0.1"
    scan_ports(target)

