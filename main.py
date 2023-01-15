import os
from dotenv import load_dotenv
from telegram.ext import *
from telegram.ext import Filters

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOTNAME = '@nani_tabetai_bot'

def start_command(update, context):
    update.message.reply_text("ayy let's get this started")

def handle_response(text: str) -> str:
    if 'hello' in text:
        return 'Hey there!'
    
    return 'unrecognised command man, idgi'

def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    print(f'User ({update.message.chat.id}) says: "{text} in: {message_type}')

    if message_type == 'group':
        if BOTNAME in text:
            new_text = text.replace(BOTNAME, '').strip()
            response = handle_response(new_text)
        else:
            response = handle_response(text)

    update.message.reply_text(response)

def error(update, context):
    print(f'Update {update} caused error: {context.error}')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    #commands
    dp.add_handler(CommandHandler('start', start_command))

    #messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    #run bot
    updater.start_polling()
    updater.idle()

#run main method
if __name__=='__main__':
    main()