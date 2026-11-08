from telegram import InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# LINK WEBAPP ADSTERRA TRÊN GITHUB PAGES CỦA BẠN
WEBAPP_URL = "https://tphuc2007.github.io/cyberminer-app/adsterra.html"

CHANNEL_URL = "https://t.me/thongbaocyberminer"
GROUP_URL = "https://t.me/thongbaocyberpet"

# TOKEN BOT 2 CỦA BẠN
BOT_TOKEN = "9156740956:AAHpmGvpI03l_rWdM_Rn8EzZkw3jVfzzmts"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.set_chat_menu_button(
        chat_id=update.effective_chat.id,
        menu_button=MenuButtonWebApp(
            text="🎮 CHƠI GAME",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )

    welcome_text = (
        "⚡️ **CHÀO MỪNG ĐẾN VỚI CYBERMINER IDLE (SERVER ADSTERRA)!**\n\n"
        "Nâng cấp Dàn Máy Đào Laser khai thác token PET nhận quà tặng (1 PET = 7 VNĐ, 0đ phí)!\n\n"
        "📢 Kênh thông báo: @thongbaocyberminer\n"
        "💬 Nhóm trao đổi: @thongbaocyberpet\n\n"
        "⚡️ Bấm nút bên dưới hoặc nút MENU ở góc dưới để mở game:"
    )
    
    keyboard = [
        [
            InlineKeyboardButton(
                text="🎮 PLAY ADSTERRA SERVER", 
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
    print("Bot 2 (Adsterra) đang chạy mượt mà...")
    app.run_polling()