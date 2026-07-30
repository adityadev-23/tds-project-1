import json
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_data = {
        "answer": {"result": "completed"},
        "log_url": "https://raw.githubusercontent.com/adityadev-23/tds-project-1/main/run.jsonl"
    }
    await update.message.reply_text(json.dumps(response_data))

if __name__ == '__main__':
    app = ApplicationBuilder().token("8971876859:AAEtZGp3XW44Jxes8jifRUQ6Age2vXf_njo").build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
