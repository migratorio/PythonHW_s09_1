
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')


app = ApplicationBuilder().token("5981067234:AAGXEB2H2BjCMa_0utWN7ADhmKUss8ihP6I").build()

app.add_handler(CommandHandler("hello", hello))
print('Сервер запустился')

app.run_polling()