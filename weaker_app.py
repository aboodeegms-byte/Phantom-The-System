#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANTOM THE SYSTEM - Local Vulnerable Lab (weaker_app.py)
Developer: Commander Phantom
Description: Local Flask server with safe intentional vulnerabilities for testing.
"""

from flask import Flask, request, render_template_string

app = Flask(__name__)

HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Phantom Vulnerable Lab</title>
    <style>
        body { background-color: #0a0a0c; color: #00f3ff; font-family: monospace; padding: 30px; }
        h1 { color: #00f3ff; text-shadow: 0 0 10px rgba(0,243,255,0.5); }
        input, button { background: #111; color: #00f3ff; border: 1px solid #0077b6; padding: 8px; margin: 5px; }
        button:hover { background: #0077b6; color: #fff; cursor: pointer; }
        .box { border: 1px solid #0077b6; padding: 20px; margin-top: 20px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>[+] PHANTOM LOCAL SECURITY LAB</h1>
    <p>Welcome Commander. This is your safe training target.</p>

    <div class="box">
        <h3>1. Reflected XSS Test Area</h3>
        <form action="/greet" method="GET">
            <label>Enter your name/payload:</label><br>
            <input type="text" name="name" placeholder="Test XSS here...">
            <button type="submit">Send</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HOME_TEMPLATE)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    # Intentional reflection for educational testing
    return render_template_string(f"""
    <body style="background:#0a0a0c; color:#00f3ff; font-family:monospace; padding:30px;">
        <h2>Hello, {{ name }}</h2>
        <a href="/" style="color:#0077b6;">&lt; Back to Lab</a>
    </body>
    """, name=name)

if __name__ == '__main__':
    print("[*] Starting Phantom Weaker Lab on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=False)


