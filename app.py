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

        <!-- Vulnerability Scan Results Section -->
        <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden mb-8">
            <div class="bg-slate-50 px-6 py-4 border-b border-slate-200">
                <h2 class="font-bold text-slate-700"><i class="fas fa-bug mr-2 text-rose-500"></i>Latest Vulnerability Scan Report (Trivy)</h2>
            </div>
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-slate-50 text-slate-500 text-xs uppercase tracking-wider border-b border-slate-200">
                            <th class="px-6 py-4 font-semibold">Vulnerability ID</th>
                            <th class="px-6 py-4 font-semibold">Package</th>
                            <th class="px-6 py-4 font-semibold">Severity</th>
                            <th class="px-6 py-4 font-semibold">Status</th>
                            <th class="px-6 py-4 font-semibold">Fixed Version</th>
                        </tr>
                    </thead>
                    <tbody class="text-sm text-slate-700 divide-y divide-slate-100">
                        {% for vuln in vulnerabilities %}
                        <tr class="hover:bg-slate-50 transition-colors">
                            <td class="px-6 py-4 font-mono text-xs text-indigo-600 font-semibold">{{ vuln.id }}</td>
                            <td class="px-6 py-4">{{ vuln.pkg }}</td>
                            <td class="px-6 py-4">
                                {% if vuln.severity == 'CRITICAL' %}
                                <span class="bg-rose-100 text-rose-700 px-2 py-1 rounded text-[10px] font-bold uppercase ring-1 ring-rose-200">{{ vuln.severity }}</span>
                                {% elif vuln.severity == 'HIGH' %}
                                <span class="bg-orange-100 text-orange-700 px-2 py-1 rounded text-[10px] font-bold uppercase ring-1 ring-orange-200">{{ vuln.severity }}</span>
                                {% else %}
                                <span class="bg-amber-100 text-amber-700 px-2 py-1 rounded text-[10px] font-bold uppercase ring-1 ring-amber-200">{{ vuln.severity }}</span>
                                {% endif %}
                            </td>
                            <td class="px-6 py-4">
                                <span class="flex items-center">
                                    <span class="h-1.5 w-1.5 rounded-full bg-emerald-500 mr-2"></span>
                                    Verified
                                </span>
                            </td>
                            <td class="px-6 py-4 text-slate-400 italic">{{ vuln.fixed }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
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
    # Mock vulnerability data to demonstrate the presentational form
    vulnerabilities = [
        {"id": "CVE-2024-45337", "pkg": "golang.org/x/crypto", "severity": "CRITICAL", "fixed": "0.31.0"},
        {"id": "CVE-2025-22869", "pkg": "google.golang.org/grpc", "severity": "HIGH", "fixed": "1.58.3"},
        {"id": "CVE-2023-24538", "pkg": "stdlib/html/template", "severity": "CRITICAL", "fixed": "1.20.3"},
        {"id": "CVE-2022-41722", "pkg": "path/filepath", "severity": "HIGH", "fixed": "1.19.6"},
        {"id": "CVE-2023-45288", "pkg": "net/http", "severity": "HIGH", "fixed": "1.22.2"}
    ]

    data = {
        "hostname": socket.gethostname(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": os.getenv("FLASK_ENV", "Production (Cloud)"),
        "vulnerabilities": vulnerabilities
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
