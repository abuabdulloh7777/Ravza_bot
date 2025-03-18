# ai_handler.py (AI o‘rniga admin orqali savol-javob)

from config import ADMIN_ID

# Savolni adminga yuborish
async def handle_ai_response(update, context):
    user = update.message.from_user
    question = update.message.text

    # Savolni adminga yuborish
    text = (
        f"📩 Yangi savol kelib tushdi:\n"
        f"👤 @{user.username if user.username else 'NoUsername'}\n"
        f"🆔 ID: {user.id}\n"
        f"❓ Savol: {question}\n\n"
        f"Javob berish uchun quyidagicha yozing:\n"
        f"/javob {user.id} sizning javob matningiz"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=text)
    await update.message.reply_text("📨 Savolingiz yuborildi. Javob tez orada beriladi.")

# Admin javobini foydalanuvchiga yuborish
async def handle_admin_answer(update, context):
    try:
        text = update.message.text
        if not text.startswith("/javob"):
            return

        # /javob 123456 Javob matni
        parts = text.split(" ", 2)
        user_id = int(parts[1])
        answer_text = parts[2]

        await context.bot.send_message(chat_id=user_id, text=f"📬 Sizning savolingizga javob:\n\n{answer_text}")
        await update.message.reply_text("✅ Javob yuborildi.")

    except Exception as e:
        await update.message.reply_text("❗ Xatolik: javob yuborilmadi.")
