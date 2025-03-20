from telegram.ext import Updater, CommandHandler, MessageHandler, filters, Application, ConversationHandler
from telegram import Update
from config import get_token
import handlers


def main():
    TOKEN = get_token()

    dp = Application.builder().token(TOKEN).build()
    
    dp.add_handler(CommandHandler('start', handlers.start))
    dp.add_handler(MessageHandler(filters.TEXT & filters.REPLY, handlers.reply_to_user))

    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.forward_to_admin))

    dp.run_polling(allowed_updates=Update.ALL_TYPES, timeout=10)

if __name__ == '__main__':
    main()
