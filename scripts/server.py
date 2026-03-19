#!/usr/bin/env python3
"""Minimal HTTP server for the UI design system configuration dashboard."""

import sys
import os
import json
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

SCRIPT_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8432

server_instance = None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # suppress logs

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            html_path = os.path.join(SCRIPT_DIR, "dashboard.html")
            try:
                with open(html_path, "r") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"dashboard.html not found")
        elif self.path == "/api/config":
            config_path = os.path.join(SCRIPT_DIR, "config.json")
            if os.path.exists(config_path):
                with open(config_path, "r") as f:
                    data = f.read()
            else:
                data = "{}"
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/apply":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                result = subprocess.run(
                    [sys.executable, os.path.join(SCRIPT_DIR, "generate.py")],
                    input=body,
                    capture_output=True,
                    cwd=os.path.dirname(SCRIPT_DIR),
                )
                if result.returncode == 0:
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"ok": True, "message": result.stdout.decode()}).encode())
                    # Shut down after successful apply
                    import threading
                    threading.Thread(target=server_instance.shutdown, daemon=True).start()
                else:
                    self.send_response(500)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"ok": False, "message": result.stderr.decode()}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "message": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server_instance = HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Dashboard running at http://localhost:{PORT}")
    try:
        server_instance.serve_forever()
    except KeyboardInterrupt:
        pass
    server_instance.server_close()
