#https://github.com/0x428a2f98/rndstring-telegram-bot
#@rndstring_bot //work in progress

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext

def start(update: Updater, context: CallbackContext) -> None:
        update.message.reply_text("bot start()")

def main() -> None:
    updater = Updater("")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
        main()