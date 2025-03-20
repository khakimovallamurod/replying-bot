from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update
import config

async def start(update: Update, context: CallbackContext):
    """Botni boshlash komandasi"""
    await update.message.reply_text("Assalomu alaykum! Adminga xabar yuborish uchun matn yozing.")

async def forward_to_admin(update: Update, context: CallbackContext):
    """Foydalanuvchi yozgan xabarni adminga forward qilish"""
    user = update.message.from_user
    admin_id = config.get_chatid()  # Admin ID ni olish
    
    # Xabarni forward qilish
    forwarded_message = await context.bot.forward_message(
        chat_id=admin_id,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

    # Forward qilingan xabar ID sini foydalanuvchi ID bilan bog‘lash
    context.bot_data[forwarded_message.message_id] = update.message.chat_id

    await update.message.reply_text("✅ Xabaringiz adminga yuborildi.")

async def reply_to_user(update: Update, context: CallbackContext):
    """Admin xabarga reply berganda, foydalanuvchiga jo‘natish"""
    if not update.message.reply_to_message:
        await update.message.reply_text("❌ Javob berish uchun foydalanuvchining xabariga reply qiling!")
        return

    # Admin reply qilgan forward qilingan xabarni olish
    replied_message = update.message.reply_to_message
    user_id = context.bot_data.get(replied_message.message_id)

    if not user_id:
        await update.message.reply_text("❌ Ushbu xabarning foydalanuvchisi topilmadi!")
        return

    # Adminning javobi
    admin_text = update.message.text

    # Userga xabar yuborish
    await context.bot.send_message(
        chat_id=user_id,
        text=f"📩 Admin javobi:\n{admin_text}"
    )

    await update.message.reply_text("✅ Javob foydalanuvchiga yuborildi!")
