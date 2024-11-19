import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)

# .env faylini yuklab olish
load_dotenv()

# TOKENni .env faylidan olish
TOKEN = os.getenv("TOKEN")


# Start funksiyasi
async def start(update: Update, context: CallbackContext) -> None:
    # Kirganda tanishtiruv xabari
    welcome_message = (
        "👋 Assalomu alaykum! Bu English With Begov o'quv markazining rasmiy support boti. "
        "Bu yerdan savollaringizga javob olishingiz mumkin. "
        "Agar yordam kerak bo'lsa, bemalol yozing! 😊\n\n"
        "Savolingizni yuboring va biz sizga tez orada javob qaytaramiz! 💬"
    )
    await update.message.reply_text(welcome_message)


# Savol qabul qilish funksiyasi
async def receive_question(update: Update, context: CallbackContext) -> None:
    # Savol qabul qilinganda tasdiq xabari
    confirmation_message = (
        "📩 Sizning savolingizni qabul qildim! 🕐 Tez orada javob olasiz. "
        "Agar qo'shimcha savolingiz bo'lsa, yozishda davom etishingiz mumkin. 😊"
    )
    await update.message.reply_text(confirmation_message)


def main() -> None:
    # Application yaratish
    application = Application.builder().token(TOKEN).build()

    # Handlerlarni qo'shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, receive_question)
    )

    # Botni ishga tushurish
    application.run_polling()

    return {
        "statusCode": 200,
        "body": "Bot ishlamoqda!"
    }

if __name__ == "__main__":
    main()