from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update
import config


async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    msg = await update.message.reply_text(
        text=f"""Assalomu aleykum {user.full_name}. Ushbu bot yordamida siz adminga xabar yo'llashingiz mumkin.""",
    )


async def replying_bot(update: Update, context: CallbackContext):
    user = update.message.from_user
    admin_id = config.get_chatid()
    chat_id = user.id
    text = update.message.text
    username = f"@{user.username}" if user.username else f"{user.full_name} (ID: {chat_id})"

    await context.bot.send_message(chat_id=admin_id, text=f"📩 Yangi xabar: {text}\n👤 Foydalanuvchi: {username}")

    await update.message.reply_text(text="✅ Sizning xabaringiz muvaffaqiyatli yuborildi")

async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text('Amalyot bajarilmadi!')
    return ConversationHandler.END