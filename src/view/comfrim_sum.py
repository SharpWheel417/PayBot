from telegram import Update
from telegram.ext import ContextTypes

from src.model.data import mess
from src.model.variables import v
from src.styles.buttons import admin_first

from config import ADMIN

## Пользователь согласен с условиями
async def yes(ids, sum, morning: bool, update: Update, context: ContextTypes.DEFAULT_TYPE):

    txt=mess("await_admin")

    if not morning:
        txt_admin = mess("order_request").format(
            ids=ids,
            username="@"+str(update.effective_user.username),
            sum=sum,
        )
        for i in ADMIN:
            await context.bot.send_message(chat_id=i, text=txt_admin, reply_markup=admin_first)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)



async def no(update: Update, context: ContextTypes.DEFAULT_TYPE):

    txt = mess("no")

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)