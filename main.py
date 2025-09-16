import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    context.user_data['picking'] = True
    context.user_data['items'] = []
    await update.message.reply_text(
        "Welcome! Enter Group/Project Names one by one:\n"        
        "Send 'done' when you finish entering all names.😊"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user messages during the picking process."""
    if not context.user_data.get('picking', False):
        return
    
    user_input = update.message.text.strip().lstrip('/').capitalize()

    if user_input.lower() == 'chash':
        user_input = 'C#'
    
    if user_input.lower() == 'done':
        items = context.user_data.get('items', [])
        
        if not items:
            await update.message.reply_text("No items were entered.")
        else:
            selected = random.choice(items)
            await update.message.reply_text(
                f"✅<< {selected} >>❤️ is the best for you. 😍\n\n"
                f"All entered names: {', '.join(items)}"
            )        
        # Reset the picking state
        context.user_data['picking'] = False
        context.user_data['items'] = []
    else:
        # Add the item to the list
        context.user_data['items'].append(user_input)
        count = len(context.user_data['items'])
        await update.message.reply_text(f"Added: {user_input}\nTotal items: {count}")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancel the current picking process."""
    if context.user_data.get('picking', False):
        context.user_data['picking'] = False
        context.user_data['items'] = []
        await update.message.reply_text("Picking process cancelled.")
    else:
        await update.message.reply_text("No active picking process to cancel.")

async def handle_cmd(update, context):
     await handle_message(update, context)

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token("8147140785:AAHeUd3OetS0vOGwGd8pQPgjTrHOW3S0tKw").build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))    
    application.add_handler(CommandHandler("cancel", cancel))
    application.add_handler(CommandHandler("flutter", handle_cmd))
    application.add_handler(CommandHandler("done", handle_cmd))
    application.add_handler(CommandHandler("ai", handle_cmd))
    application.add_handler(CommandHandler("uxui", handle_cmd))
    application.add_handler(CommandHandler("laravel", handle_cmd))
    application.add_handler(CommandHandler("python", handle_cmd))
    application.add_handler(CommandHandler("java", handle_cmd))
    application.add_handler(CommandHandler("react", handle_cmd))
    application.add_handler(CommandHandler("chash", handle_cmd))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()