import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- 1. WEB SERVER GIẢ LẬP ĐỂ RENDER THỎA MÃN ĐIỀU KIỆN PORT SCAN ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot 1 Monetag Online")

def run_health_check():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    server.serve_forever()

threading.Thread(target=run_health_check, daemon=True).start()

# --- 2. CẤU HÌNH BOT TELEGRAM MONETAG ---
WEBAPP_URL = "https://tphuc2007.github.io/cyberminer-app/"
CHANNEL_URL = "https://t.me/thongbaocyberminer"
GROUP_URL = "https://t.me/thongbaocyberpet"
BOT_TOKEN = "9183289863:AAgo4CdGesu65qGtFGU5tz72tGiT_2ldDqQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.set_chat_menu_button(
        chat_id=update.effective_chat.id,
        menu_button=MenuButtonWebApp(
            text="🎮 CHƠI GAME",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )
    
    welcome_text = (
        "🎉 **CHÀO MỪNG ĐẾN VỚI CYBERMINER IDLE!**\n\n"
        "Nâng cấp Dàn Máy Đào Laser khai thác token PET nhận quà tặng uy tín 100% (1 PET = 7 VNĐ, 0đ phí)!\n\n"
        "📋 **QUY ĐỊNH BẢO MẬT & MỜI BẠN BÈ:**\n"
        "• Người được mời phải xem đủ 100 quảng cáo thì người mời mới nhận được +500 Vàng.\n"
        "• Nghiêm cấm tạo tài khoản ảo, dùng tool cheat, hack dữ liệu. Hệ thống AI quét tự động sẽ KHÓA TÀI KHOẢN VĨNH VIỄN và tịch thu toàn bộ số dư!\n"
        "• Kênh thông báo: @thongbaocyberminer\n"
        "• Nhóm trao đổi: @thongbaocyberpet\n\n"
        "👇 Bấm nút bên dưới hoặc nút MENU ở góc dưới để mở game:"
    )

    keyboard = [
        [InlineKeyboardButton(text="🎮 PLAY (CHƠI NGAY)", web_app=WebAppInfo(url=WEBAPP_URL))],
        [InlineKeyboardButton(text="📢 KÊNH THÔNG BÁO CHÍNH THỨC", url=CHANNEL_URL)],
        [InlineKeyboardButton(text="💬 NHÓM TRAO ĐỔI CỘNG ĐỒNG", url=GROUP_URL)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot 1 (Monetag) đang chạy mượt mà...")
    app.run_polling()
