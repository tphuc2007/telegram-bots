import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Web Server giả lập để Render quét cổng HTTP không bị timeout
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot 1 Online")

def run_health_check():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    server.serve_forever()

threading.Thread(target=run_health_check, daemon=True).start()

# --- NỘI DUNG CODE BOT GIỮ NGUYÊN BÊN DƯỚI ---
WEBAPP_URL = "https://tphuc2007.github.io/cyberminer-app/"
