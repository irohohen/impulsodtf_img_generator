 # commands/image_handler.py

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import image_generator as img
import api_services as svc

async def generar_imagen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Genera una imagen con las tasas de cambio actuales y la envía al usuario."""
    await update.message.reply_text("⏳ Generando imagen con las tasas de cambio actuales...")
    
    # Obtener las tasas de cambio actuales
    #_,_,tasa_usdt = svc.get_binance_p2p_prices("BUY")

    usd =  8  #ves / svc.get_bcv_rate()
    ves =  usd * svc.get_bcv_rate()
    eur = ves / svc.get_bcv_rate("eur")

    tasas = (ves, usd, eur)
    if not tasas:
        await update.message.reply_text("❌ No se pudieron obtener las tasas de cambio en este momento. Por favor, inténtalo de nuevo más tarde.")
        return

    # Generar la imagen con las tasas obtenidas
    ruta_imagen = img.create_rate_image(ves, usd, eur)

    # Enviar la imagen al usuario con la proporcion original
    with open(ruta_imagen,"rb") as foto:
        await update.message.reply_photo(photo=foto, caption="📊 Aquí están las tasas de cambio actuales.")

# Definimos el comando /image

async def image_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await generar_imagen(update, context)

# Creamos y exportamos el handler para el comando /start
image_handler = CommandHandler("image", image_command)