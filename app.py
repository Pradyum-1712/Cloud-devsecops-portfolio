from flask import Flask, jsonify, render_template_string
import os
import socket
from datetime import datetime

app = Flask(__name__)

# Professional Dashboard Template using Tailwind CSS
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud DevSecOps Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; }
        .glass-card { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); }
    </style>
</head>
<body class="bg-slate-50 min-h-screen">
    <!-- Navbar -->
    <nav class="bg-indigo-700 text-white p-4 shadow-lg">
        <div class="container mx-auto flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <i class="fas fa-shield-halved text-2xl"></i>
                <span class="font-bold text-xl tracking-tight">SecureCloud Ops</span>
            </div>
            <div class="hidden md:flex space-x-6">
                <span class="text-indigo-100"><i class="fas fa-server mr-2"></i>{{ hostname }}</span>
                <span class="text-indigo-100"><i class="fas fa-clock mr-2"></i>{{ time }}</span>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <!-- Status Card -->
            <div class="glass-card p-6 rounded-2xl shadow-sm border border-slate-200">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-slate-500 font-semibold uppercase text-xs tracking-wider">Environment Status</h3>
                    <span class="bg-emerald-100 text-emerald-700 px-3 py-1 rounded-full text-xs font-bold uppercase">Active</span>
                </div>
                <p class="text-2xl font-bold text-slate-800">{{ environment }}</p>
            </div>
            
            <!-- Security Score Card -->
            <div class="glass-card p-6 rounded-2xl shadow-sm border border-slate-200">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-slate-500 font-semibold uppercase text-xs tracking-wider">Security Posture</h3>
                    <i class="fas fa-shield-check text-indigo-500"></i>
                </div>
                <p class="text-2xl font-bold text-slate-800 tracking-tight">Hardened (Alpine)</p>
            </div>

            <!-- Version Card -->
            <div class="glass-card p-6 rounded-2xl shadow-sm border border-slate-200">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-slate-500 font-semibold uppercase text-xs tracking-wider">Pipeline Version</h3>
                    <i class="fas fa-code-branch text-slate-400"></i>
                </div>
                <p class="text-2xl font-bold text-slate-800">v1.2.0-secure</p>
            </div>
        </div>

        <!-- System Details Section -->
        <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
            <div class="bg-slate-50 px-6 py-4 border-b border-slate-200 flex justify-between items-center">
                <h2 class="font-bold text-slate-700">Audit Logs & System Metadata</h2>
                <button class="text-indigo-600 hover:text-indigo-800 text-sm font-semibold" onclick="location.reload()">Refresh Data</button>
            </div>
            <div class="p-6">
                <div class="space-y-4">
                    <div class="flex justify-between items-center py-2 border-b border-slate-100">
                        <span class="text-slate-500 text-sm">Deployment Container ID</span>
                        <code class="bg-slate-100 px-2 py-1 rounded text-xs text-indigo-600 font-mono">{{ hostname }}</code>
                    </div>
                    <div class="flex justify-between items-center py-2 border-b border-slate-100">
                        <span class="text-slate-500 text-sm">Security Scanner</span>
                        <span class="text-sm font-semibold text-slate-700">Trivy (Enabled)</span>
                    </div>
                    <div class="flex justify-between items-center py-2 border-b border-slate-100">
                        <span class="text-slate-500 text-sm">Base Image Architecture</span>
                        <span class="text-sm font-semibold text-slate-700">Linux/Alpine-Python-3.12</span>
                    </div>
                    <div class="flex justify-between items-center py-2 border-b border-slate-100">
                        <span class="text-slate-500 text-sm">API Connectivity</span>
                        <span class="text-sm font-semibold text-emerald-600">Established</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <footer class="mt-12 text-center text-slate-400 text-sm">
            <p>&copy; 2025 Pradyum Cloud DevSecOps Portfolio. Automated with GitHub Actions & Terraform.</p>
        </footer>
    </main>
</body>
</html>
"""

@app.route('/')
def home():
    # Gather some "real" data from the container
    data = {
        "hostname": socket.gethostname(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": os.getenv("FLASK_ENV", "Production (Cloud)"),
    }
    return render_template_string(DASHBOARD_HTML, **data)

@app.route('/health')
def health():
    return jsonify({"status": "Healthy", "code": 200}), 200

@app.route('/api/v1/meta')
def api_meta():
    return jsonify({
        "status": "Secure",
        "message": "DevSecOps Portfolio API",
        "container_id": socket.gethostname()
    })

if __name__ == '__main__':
    # Changed port to 5001 to avoid conflicts with macOS AirPlay (which uses 5000)
    app.run(host='0.0.0.0', port=5001)
