#!/usr/init/env python3
# -*- coding: utf-8 -*-
"""
PHANTOM THE SYSTEM - Local Vulnerable Lab (weaker_app.py)
Developer: Commander Phantom
Description: Local Flask web server designed with intentional endpoints for testing Phantom Scanner.
"""

from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template with intentional vulnerabilities and security header omissions for testing
HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Phantom Local Lab - Vulnerable Target</title>
    <style>
        body { background-color: #0b0f19; color: #00f3ff; font-family: monospace; padding: 40px; }
        h1 { color: #ffffff; text-shadow: 0 0 10px #00f3ff; }
        .box { border: 1px solid #0077b6; padding: 20px; margin-top: 20px; border-radius: 8px; }
        a { color: #00f3ff; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>[ PHANTOM LOCAL VULNERABLE LAB ]</h1>
    <p>Target status: Active & Ready for Audit, Commander.</p>

    <div class="box">
        <h3>Available Endpoints for Testing:</h3>
        <ul>
            <li><a href="/greet?name=Phantom">/greet?name=Phantom</a> (Reflected Input Endpoint)</li>
            <li><a href="/admin">/admin</a> (Restricted Area Simulation)</li>
            <li><a href="/leak">/leak</a> (Information Disclosure Simulation)</li>
        </ul>
    </div>

    <div class="box">
        <h3>Test Greeting Form:</h3>
        <form action="/greet" method="GET">
            <input type="text" name="name" placeholder="Enter name or XSS payload..." style="padding: 8px; width: 300px; background: #000; color: #fff; border: 1px solid #00f3ff;">
            <button type="submit" style="padding: 8px 15px; background: #0077b6; color: #fff; border: none; cursor: pointer;">Send</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HOME_TEMPLATE)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    # Intentionally reflecting input without escaping to simulate XSS test target
    return f"""
    <h3 style="font-family: monospace; background: #0b0f19; color: #00f3ff; padding: 20px;">
        Hello, {name}! [Phantom Lab Endpoint]
    </h3>
    <br><a href="/" style="color: #00f3ff; font-family: monospace;">&larr; Back to Lab Home</a>
    """

@app.route('/admin')
def admin():
    return "<h3 style='font-family:monospace; color:#ff0055;'>[!] Access Denied: Admin privileges required.</h3>"

@app.route('/leak')
def leak():
    return "<h3 style='font-family:monospace; color:#ffcc00;'>[!] Server Info: Flask/3.0.0 running on Werkzeug Development Server.</h3>"

if __name__ == '__main__':
    print("\n[*] Starting Phantom Local Vulnerable Lab on http://127.0.0.1:5000 ...")
    app.run(host='0.0.0.0', port=5000, debug=False)


