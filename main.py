# main.py

import logging
from telegram.ext import Application

from config import TELEGRAM_TOKEN
from commands import ALL_HANDLERS # Importamos la lista de manejadores

# Configuración de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    """Inicia y corre el bot, registrando todos los comandos."""

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Añade todos los manejadores de la lista a la aplicación
    for handler in ALL_HANDLERS:
        application.add_handler(handler)

    print("✅ Bot en línea con los siguientes comandos:")
    #for handler in ALL_HANDLERS:
        # .commands es una tupla, tomamos el primero
     #   print(f" -> /{list(handler.commands)[0]}")

    print("\nPresiona Ctrl+C para detener.")

    # Inicia el bot
    application.run_polling()

if __name__ == "__main__":
    main()