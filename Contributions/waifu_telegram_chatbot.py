import os 
from telegram import *
import requests
from telegram.ext import *
import json
from keep_alive import keep_alive

async def start(update : Update , context : ContextTypes.DEFAULT_TYPE): 
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username

    with open ('database.json' , 'r') as f:
        temp = json.load(f)
    append_data = {}
    # append_data['user_no.'] = 
    append_data['chat_id'] = chat_id
    append_data['first_name'] = first_name
    append_data['last_name'] = last_name
    append_data['username'] = username
    temp.append(append_data)
    with open ('database.json' , 'w') as f:
        json.dump(temp ,f,indent=4)

    await update.message.reply_text("hi")

async def report(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hi")

async def chatbot(update : Update , context : ContextTypes.DEFAULT_TYPE):
        chat_id = update.message.chat_id
        first_name = update.message.chat.first_name
        last_name = update.message.chat.last_name
        username = update.message.chat.username
        msg = str(update.message.text).lower()
        
        try:
                url = "https://waifu.p.rapidapi.com/path"
                
                querystring = {"user_id":update.message.chat_id,"message":msg,"from_name":first_name,"to_name":"Girl","situation":"Girl loves Boy.","translate_from":"auto","translate_to":"auto"}
                
                payload = {}
                
                headers = {
                                "content-type": "application/json",
                                "X-RapidAPI-Key": "c70123babemsh2932eadbeea0a71p1ff4eejsn61d92adbe37c",
                                "X-RapidAPI-Host": "waifu.p.rapidapi.com"
                }
                # Try Getting Responses From API > 
                
                response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
                await context.bot.send_message(chat_id=update.effective_chat.id, text= response.text)

                    
            
    # If All Code Generates Error >                
        except Exception as e:
            await update.message.reply_text(e)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    key = os.environ['api_key']
    application = ApplicationBuilder().token(key).build()
    
    start_handler = CommandHandler('start', start)
    report_handler = CommandHandler('report', report)
    chatbot_handler = MessageHandler(filters.TEXT, chatbot)

        
    
    application.add_handler(start_handler)
    application.add_handler(report_handler)
    application.add_handler(chatbot_handler)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    keep_alive()
    application.run_polling()
    
    


