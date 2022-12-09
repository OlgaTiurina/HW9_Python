def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Hello")

def abv(update, context):
    text = update.message.text.split()
    list = []
    for elements in text:
        if 'абв' not in elements:
            list.append(elements)
    context.bot.send_message(update.effective_chat.id, ' '.join(list))