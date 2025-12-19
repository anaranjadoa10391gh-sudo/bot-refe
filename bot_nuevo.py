from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ========= CONFIG =========
TOKEN = "8536641039:AAHo2v0gKhMasGsBp6c60I8Mqnv9iM9Hchk"
CHANNEL_ID = -1003540201441
# ==========================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot activo y funcionando")


async def refe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if not msg.reply_to_message:
        await msg.reply_text("❌ Responde a una FOTO")
        return

    replied = msg.reply_to_message

    if not replied.photo:
        await msg.reply_text("❌ Eso no es una foto")
        return

    user = update.effective_user
    username = f"@{user.username}" if user.username else user.full_name

    texto_foto = replied.caption.strip() if replied.caption else "—"

    caption = (
        f"⎾  𝗨𝘀𝗲𝗿 ⌁  {username}\n"
        f"⎿  𝗧𝗲𝘅𝘁 ⌁  {texto_foto}\n"
        f"ㅤ  ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙ ˙"
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("easy", url="https://t.me/+-2yEv5gnV7Q2YTkx"),
            InlineKeyboardButton("kurumi", url="https://t.me/+p8849I9bfhQyNTJh"),
        ]
    ])

    photo_id = replied.photo[-1].file_id

    await context.bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=photo_id,
        caption=caption,
        reply_markup=keyboard
    )

    await msg.reply_text("✅ Enviado al canal")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("refe", refe))
    app.add_handler(MessageHandler(filters.Regex(r"^\.refe"), refe))

    print("🤖 Bot ENCENDIDO")
    app.run_polling()


if __name__ == "__main__":
    main()
