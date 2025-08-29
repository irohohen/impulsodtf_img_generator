 # commands/start_handler.py

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Muestra el mensaje de bienvenida cuando un usuario inicia el bot."""
    user_name = update.effective_user.first_name
    welcome_message = (
        f"👋 Muy Buenos Dias, Tardes o Noches {user_name}!\n\n"
        "Bienvenido a Su Conexión Monetaria.\n\n"
        "Puedes usar los siguientes comandos:\n"
        f"• /start - Bienvenida\n"
        f"• /info - información\n"
        f"• /precio - precio del usdt en Binance y Tasa BCV\n"
        f"• /calc - cuanto valen tus bs en dolares según Tasa BCV y  USDT\n"
        f"• /bs -  cuanto valen tus bs en dolares según Tasa BCV y  USDT\n"
        f"• /usd - cuanto valen tus dolares en bs según Tasa BCV y USDT\n"
        f"• /bcvtousdt - cuanto equivale tus dolares BCV en USDT\n"
        f"• /usdttobcv - cuanto equivale tus USDT en dolares BCV\n\n"
        f"Escribe un comando para comenzar."
    )
    await update.message.reply_text(welcome_message)

# Creamos y exportamos el handler para el comando /start
start_handler = CommandHandler("start", start_command)