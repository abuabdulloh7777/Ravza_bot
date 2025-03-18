# add_rights_handler.py

from contact_control_handler import add_contact_rights
from config import ADMIN_ID

async def give_rights(update, context):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Siz admin emassiz.")
        return

    try:
        user_id = int(context.args[0])
        count = int(context.args[1])
        add_contact_rights(user_id, count)
        await update.message.reply_text(f"✅ {user_id} foydalanuvchiga {count} ta huquq berildi.")
    except:
        await update.message.reply_text("❗ Format noto‘g‘ri: /giverights user_id soni\nMasalan: /giverights 123456789 5")
