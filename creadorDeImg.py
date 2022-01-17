from os import sep
from conf import FONTS_DIR, FONDOS_LUNES, FONDOS_MARTES, FONDOS_MIERCOLES
from PIL import Image, ImageDraw, ImageFont
import os
# get an image

lunes_1 = os.path.join(FONDOS_LUNES,'fondoLunes_1.png')
martes_1 = os.path.join(FONDOS_MARTES,'fondoMartes_1.png')
miercoles_1 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_1.png')

lunes_2 = os.path.join(FONDOS_LUNES,'fondoLunes_2.png')
martes_2 = os.path.join(FONDOS_MARTES,'fondoMartes_2.png')
miercoles_2 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_2.png')

lunes_3 = os.path.join(FONDOS_LUNES,'fondoLunes_3.png')
martes_3 = os.path.join(FONDOS_MARTES,'fondoMartes_3.png')
miercoles_3 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_3.png')

lunes_4 = os.path.join(FONDOS_LUNES,'fondoLunes_4.png')
martes_4 = os.path.join(FONDOS_MARTES,'fondoMartes_4.png')
miercoles_4 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_4.png')

lunes_5 = os.path.join(FONDOS_LUNES,'fondoLunes_5.png')
martes_5 = os.path.join(FONDOS_MARTES,'fondoMartes_5.png')
miercoles_5 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_5.png')

dirfntB = os.path.join(FONTS_DIR,'Bebas Neue Pro Bold.otf')
dirfntR = os.path.join(FONTS_DIR,'Bebas Neue Pro Regular.otf')


def imagen_1(dia, titulo, numeroC):
    base = ""
    if dia == "Lunes-Jueves":
        base = Image.open(lunes_1).convert('RGBA')
    if dia == "Martes-Viernes":
        base = Image.open(martes_1).convert('RGBA')
    if dia == "Miercoles-Sábado":
        base = Image.open(miercoles_1).convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fntB = ImageFont.truetype(dirfntB, 101)
    fntR = ImageFont.truetype(dirfntR, 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)


    numeroPalabras = 0
    diaC = dia
    separado = titulo.split()
    orange = (241,90,36,255)
    white = (255,255,255,255)
    color = ""
    if diaC == "Viernes":
        color = orange
    else:
        color = white

    for i in separado:
        numeroPalabras += 1


    numeroCaracteres = len(titulo)


    if numeroPalabras == 1:
        
        d.text((926.5078/1.3,359.4723/1.2), separado[0], font=fntB, fill=color)

    if numeroPalabras == 2:

        # Titulo de cuatro letras
        d.text((926.5078/1.3,359.4723/1.37), separado[0], font=fntB, fill=color)
        d.text((926.5078/1.3,359.4723), separado[1], font=fntB, fill=color)
    if numeroPalabras == 3:

        # Titulo de cuatro letras
        d.text((926.5078/1.3,359.4723/1.37), separado[0]+" "+separado[1], font=fntB, fill=color)
        d.text((926.5078/1.3,359.4723), separado[2], font=fntB, fill=color)

    if numeroPalabras == 4:

        # Titulo de cuatro letras
        d.text((926.5078/1.3,359.4723/1.37), separado[0]+" "+separado[1], font=fntB, fill=color)
        d.text((926.5078/1.3,359.4723), separado[2]+" "+separado[3], font=fntB, fill=color)

    if numeroPalabras == 5:
        fntB = ImageFont.truetype(dirfntB, 90)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 16:
            d.text((926.5078/1.3,359.4723/1.3), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723),separado[3]+" "+separado[4], font=fntB, fill=color)
        else: 
            d.text((926.5078/1.3,359.4723/1.3), separado[0]+" "+separado[1], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723),separado[2]+" "+separado[3]+" "+separado[4], font=fntB, fill=color)


    if numeroPalabras == 6:
        fntB = ImageFont.truetype(dirfntB, 81)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 16:
            d.text((926.5078/1.3,359.4723/1.3), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
        else: 
            d.text((926.5078/1.3,359.4723/1.3), separado[0]+" "+separado[1], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723),separado[2]+" "+separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)


    if numeroPalabras == 7:
        fntB = ImageFont.truetype(dirfntB, 76)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((926.5078/1.3,359.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723/1.085),separado[3]+" "+separado[4], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723*1.12),separado[5] +" "+separado[6], font=fntB, fill=color)
        else: 
            d.text((926.5078/1.3,359.4723/1.3), separado[0]+" "+separado[1], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723),separado[2]+" "+separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)

    if numeroPalabras == 8:
        fntB = ImageFont.truetype(dirfntB, 76)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((926.5078/1.3,359.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723/1.085),separado[3]+" "+separado[4], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723*1.12),separado[5] +" "+separado[6]+" "+separado[7], font=fntB, fill=color)
        else: 
            d.text((926.5078/1.3,359.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723/1.085),separado[3]+" "+separado[4], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723*1.12),separado[5] +" "+separado[6]+" "+separado[7], font=fntB, fill=color)

    if numeroPalabras == 9:
        fntB = ImageFont.truetype(dirfntB, 76)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((926.5078/1.3,359.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723/1.085),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723*1.12),separado[6]+" "+separado[7]+" "+separado[8], font=fntB, fill=color)

    if numeroPalabras == 10:
        fntB = ImageFont.truetype(dirfntB, 76)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((926.5078/1.3,359.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723/1.085),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
            d.text((926.5078/1.3,359.4723*1.12),separado[6]+" "+separado[7]+" "+separado[8]+" "+separado[9], font=fntB, fill=color)

    if diaC == "Lunes" or diaC == "Jueves":
            d.text((926.5078*1.019/1.3,359.4723*1.48), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 0,255))
    if diaC == "Martes":
        d.text((926.5078*1.019/1.3,359.4723*1.48), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 255,255))
    if diaC == "Miercoles" or diaC == "Sabado":
        d.text((926.5078*1.019/1.3,359.4723*1.48), "REFLEXIÓN #"+numeroC, font=fntR, fill=(255, 255, 0,255))
    if diaC == "Viernes":
        d.text((926.5078*1.019/1.3,359.4723*1.48), "REFLEXIÓN #"+numeroC, font=fntR, fill=(96, 56, 19,255))


    out = Image.alpha_composite(base, txt)

    out.show()

    return out
