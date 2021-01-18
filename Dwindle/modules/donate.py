import telegram
def donate(update, context):
    keyboard = [
        [
            telegram.InlineKeyboardButton("Contribute",
                                          url="https://github.com/RabbitFored"),
            telegram.InlineKeyboardButton("Paypal Us",url="https://paypal.me/donateostrich"),
        ],
    ]

    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Thank you for your wish to contribute. I hope you enjoyed using our services. Make a small donation/contribute to let this project alive." , reply_markup=reply_markup)
