from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# الصفحة الرئيسية لتجربة الأدوار
@app.route('/')
def home():
    return '''
    <html dir="rtl">
    <head><meta charset="utf-8"><title>موقع فأر التجارب</title></head>
    <body style="font-family: Tahoma; background: #111; color: #00ffcc; padding: 20px;">
        <h2>🧪 منصة التدريب والتحصين السيبراني (Phantom Lab)</h2>
        <p>اختر الاختبار الميداني المطلوب:</p>
        <ul>
            <li><a href="/ping" style="color: #ff0055;">1. اختبار حقن الأوامر (Command Injection)</a></li>
            <li><a href="/greet?name=ضيف" style="color: #ff0055;">2. اختبار الحقن البرمجي (Reflected XSS)</a></li>
        </ul>
    </body>
    </html>
    '''

# 1. صفحة ثغرة Command Injection
@app.route('/ping', methods=['GET', 'POST'])
def ping():
    output = ""
    if request.method == 'POST':
        ip = request.form.get('ip')
        # الثغرة المقصودة: تمرير مباشر لمدخلات المستخدم لأمر النظام
        cmd = f"ping -c 2 {ip}"
        output = os.popen(cmd).read()
    
    return f'''
    <html dir="rtl">
    <head><meta charset="utf-8"><title>Command Injection</title></head>
    <body style="font-family: Tahoma; background: #111; color: #00ffcc; padding: 20px;">
        <h3>اختبار فحص الـ Ping (موقع التجارب)</h3>
        <form method="POST">
            أدخل عنوان IP أو أمر إضافي: <input type="text" name="ip" style="background: #222; color: #fff; padding: 5px;">
            <input type="submit" value="تنفيذ" style="background: #ff0055; color: #fff; border: none; padding: 5px 10px;">
        </form>
        <pre style="background: #222; padding: 10px; border: 1px solid #00ffcc;">{output}</pre>
        <br><a href="/" style="color: #fff;">العودة للرئيسية</a>
    </body>
    </html>
    '''

# 2. صفحة ثغرة XSS
@app.route('/greet')
def greet():
    name = request.args.get('name', 'ضيف')
    # الثغرة المقصودة: عرض المدخلات بدون تصفية
    return render_template_string(f'''
    <html dir="rtl">
    <head><meta charset="utf-8"><title>XSS Test</title></head>
    <body style="font-family: Tahoma; background: #111; color: #00ffcc; padding: 20px;">
        <h3>أهلاً بك يا {name}!</h3>
        <p>هذه الصفحة تختبر عرض مدخلات المستخدم مباشرة.</p>
        <br><a href="/" style="color: #fff;">العودة للرئيسية</a>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

