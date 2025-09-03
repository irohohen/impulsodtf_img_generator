# image_generator.py

from PIL import Image, ImageDraw, ImageFont
import api_services as svc
import json
import rotatedtext as rt
import datetime

def create_rate_image(ves: float, usd: float, eur: float) -> str:

    try:
        # Cargar la imagen de plantilla
        img = Image.open("image_generator_stuff/template.png").convert("RGBA")
        #draw = ImageDraw.Draw(img)

        # --- Configuración de fuentes y texto ---
        try:
            font_title = ImageFont.truetype("image_generator_stuff/arial.ttf", 35)
            font_rate = ImageFont.truetype("image_generator_stuff/arial.ttf", 35)
        except IOError:
            print("Fuente 'arial.ttf' no encontrada. Usando fuente por defecto.")
            font_title = ImageFont.load_default()
            font_rate = ImageFont.load_default()

        # --- Formatear los textos que se van a dibujar ---
        ves_text = f"{ves:,.2f}"
        usd_text = f"{usd:,.2f}"
        eur_text = f"{eur:,.2f}"

        # --- Cargar coordenadas y ángulos desde el archivo JSON ---
        try:
            with open("templatecords.json", "r") as f:
                coords = json.load(f)
        except FileNotFoundError:
            print("Archivo 'templatecords.json' no encontrado. Usando coordenadas por defecto.")
            coords = {
                "ves": [380, 520],
                "usd": [400, 635],
                "eur": [420, 760],
                "ves_angle": 0,
                "usd_angle": 0,
                "eur_angle": 0
            }
        ves_pos = tuple(coords.get("ves", (380, 520)))
        usd_pos = tuple(coords.get("usd", (400, 635)))
        eur_pos = tuple(coords.get("eur", (420, 760)))
        ves_angle = coords.get("ves_angle", 0)
        usd_angle = coords.get("usd_angle", 0)
        eur_angle = coords.get("eur_angle", 0)

        # --- Dibuja el texto en la imagen ---
        # ¡IMPORTANTE! Ajusta estas coordenadas (x, y) para tu imagen.
        # Recuerda que debes rotar las letras en el editor de imágenes.

        rt.draw_rotated_text(img, ves_text, ves_pos, ves_angle, font_rate, "white")
        rt.draw_rotated_text(img, usd_text, usd_pos, usd_angle, font_rate, "white")
        rt.draw_rotated_text(img, eur_text, eur_pos, eur_angle, font_rate, "black")

        # --- Dibuja la fecha actual ---
        #current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        #date_text = f"Fecha: {current_date}"
        #draw.text((50, 50), date_text, font=font_title, fill="white")

        # --- Guarda la imagen generada ---
        output_path = "output.png"
        img.save(output_path, "PNG")

        return output_path

    except FileNotFoundError as e:
        print(f"Error: Archivo no encontrado: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error al generar la imagen: {e}")
        import traceback
        traceback.print_exc()
        return None


# --- BLOQUE PARA PRUEBAS DIRECTAS ---
if __name__ == "__main__":
    print("▶️ Ejecutando image_generator.py en modo de prueba...")

    # Simula datos para la prueba
    precio = 6
    _,_,tasa_usdt = svc.get_binance_p2p_prices("buy")

    ves = precio * tasa_usdt
    usd = ves / svc.get_bcv_rate()
    eur = ves / svc.get_bcv_rate("eur")

    # Llama a la función principal
    output_file = create_rate_image(ves, usd, eur)

    if output_file:
        print(f"✅ ¡Prueba exitosa! Imagen guardada como '{output_file}'.")
        print("Revisa el archivo para ajustar posiciones, colores y fuentes.")
    else:
        print("❌ La prueba falló. Revisa los mensajes de error de arriba.")
