import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# توکن از Railway یا محیط سرور خونده میشه
TOKEN = os.getenv("BOT_TOKEN")

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋\nمن ربات رایگان تو هستم 🤖")

# اجرای برنامه
def main():
    if not TOKEN:
        raise ValueError("❌ توکن ربات (BOT_TOKEN) پیدا نشد. حتماً توی Railway ست کن.")

    app = Application.builder().token(TOKEN).build()

    # هندلر برای دستور /start
    app.add_handler(CommandHandler("start", start))

    print("✅ ربات روشن شد و منتظر پیام‌هاست...")
    app.run_polling()

if __name__ == "__main__":
    main()
