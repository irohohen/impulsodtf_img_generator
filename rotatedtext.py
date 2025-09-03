from PIL import Image, ImageDraw, ImageFont

def draw_rotated_text(base_img, text, position, angle, font, fill):
    """
    Dibuja texto rotado sobre una imagen base.

    Args:
        base_img (PIL.Image.Image): Imagen sobre la que se dibuja el texto.
        text (str): Texto a dibujar.
        position (tuple): Coordenadas (x, y) donde colocar el texto.
        angle (float): Ángulo de rotación en grados.
        font (PIL.ImageFont.ImageFont): Fuente del texto.
        fill (str or tuple): Color del texto.

    Returns:
        None. Modifica la imagen base directamente.
    """
    # Crear imagen temporal para el texto
    temp_img = Image.new('RGBA', base_img.size, (255, 255, 255, 0))
    temp_draw = ImageDraw.Draw(temp_img)
    temp_draw.text(position, text, font=font, fill=fill)
    # Rotar la imagen temporal
    rotated = temp_img.rotate(angle, resample=Image.BICUBIC)
    # Combinar la imagen rotada con la base
    base_img.alpha_composite(rotated)