from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from config import BOT_TOKEN
from src.controller.button import button_callback
from src.controller.message import handle_message
from src.controller.document import handle_document

from src.view.start import start
from src.controller.sendmess import sendmess

from src.parsing.shed import run_scheduler
from src.parsing.parse import parsing

from src.parsing.timechk import time_check

sendmess("Бот запущен")

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CallbackQueryHandler(button_callback))

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    document_handler = MessageHandler(filters.Document.PDF, handle_document)
    application.add_handler(document_handler)

    message_handler = MessageHandler(filters.TEXT, handle_message)
    application.add_handler(message_handler)


    application.run_polling()
