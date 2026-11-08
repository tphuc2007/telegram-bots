from telegram import InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

WEBAPP_URL = "https://tphuc2007.github.io/cyberminer-app/"

# LINK KÊNH THÔNG BÁO VÀ NHÓM TRAO ĐỔI CỦA BẠN
CHANNEL_URL = "https://t.me/thongbaocyberminer"
GROUP_URL = "https://t.me/thongbaocyberpet"

# TOKEN BOT CHÍNH CỦA BẠN (@khobauminer_ads_bot)
BOT_TOKEN = "9183289863:AAGo4CdGesu65qGtFGU5tz72tGiT_2ldDqQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.set_chat_menu_button(
        chat_id=update.effective_chat.id,
        menu_button=MenuButtonWebApp(
            text="🎮 CHƠI GAME",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )

    welcome_text = (
        "⚡️ **CHÀO MỪNG ĐẾN VỚI CYBERMINER IDLE!**\n\n"
        "Nâng cấp Dàn Máy Đào Laser khai thác token PET nhận quà tặng uy tín 100% (1 PET = 7 VNĐ, 0đ phí)!\n\n"
        "🛡 **QUY ĐỊNH BẢO MẬT & MỜI BẠN BÈ:**\n"
        "• Người được mời phải xem đủ 100 quảng cáo thì người mời mới nhận được +500 Vàng.\n"
        "• Nghiêm cấm tạo tài khoản ảo, dùng tool cheat, hack dữ liệu. Hệ thống AI quét tự động sẽ KHÓA TÀI KHOẢN VĨNH VIỄN và tịch thu toàn bộ số dư!\n\n"
        "📢 Kênh thông báo: @thongbaocyberminer\n"
        "💬 Nhóm trao đổi: @thongbaocyberpet\n\n"
        "⚡️ Bấm nút bên dưới hoặc nút MENU ở góc dưới để mở game:"
    )
    
    keyboard = [
        [
            InlineKeyboardButton(
                text="🎮 PLAY (CHƠI NGAY)", 
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 KÊNH THÔNG BÁO CHÍNH THỨC", 
                url=CHANNEL_URL
            )
        ],
        [
            InlineKeyboardButton(
                text="💬 NHÓM TRAO ĐỔI CỘNG ĐỒNG", 
                url=GROUP_URL
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot 1 (@khobauminer_ads_bot) đang chạy mượt mà...")
    app.run_polling()