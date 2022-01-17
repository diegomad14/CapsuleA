from os import sep
from conf import FONTS_DIR, FONDOS_LUNES, FONDOS_MARTES, FONDOS_MIERCOLES
from PIL import Image, ImageDraw, ImageFont
import os
# get an image

lunes_1 = os.path.join(FONDOS_LUNES,'Lunes-Jueves.png')
martes_1 = os.path.join(FONDOS_MARTES,'Martes-Viernes.png')
miercoles_1 = os.path.join(FONDOS_MIERCOLES,'Miercoles-Sabado.png')

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
    fntB = ImageFont.truetype(dirfntB, 161)
    fntR = ImageFont.truetype(dirfntR, 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)


    numeroPalabras = 0
    diaC = dia
    separado = titulo.split()
    purple = (241,90,36,255)
    white = (255,255,255,255)
    color = ""

    if dia == "Miercoles-Sábado":
        color = white
    else:
        color = "#4c4c4c"

    for i in separado:
        numeroPalabras += 1


    numeroCaracteres = len(titulo)


    if numeroPalabras == 1:
        
        d.text((165.5078/1.3,394.4723/1.28), separado[0], font=fntB, fill=color)

    if numeroPalabras == 2:

        
        d.text((165.5078/1.3,394.4723/1.32), separado[0], font=fntB, fill=color)
        d.text((165.5078/1.3,394.4723), separado[1], font=fntB, fill=color)
    if numeroPalabras == 3:

        
        d.text((165.5078/1.3,394.4723/1.59), separado[0]+" "+separado[1], font=fntB, fill=color)
        d.text((165.5078/1.3,394.4723), separado[2], font=fntB, fill=color)

    if numeroPalabras == 4:

        
        d.text((165.5078/1.3,394.4723/1.37), separado[0]+" "+separado[1], font=fntB, fill=color)
        d.text((165.5078/1.3,394.4723), separado[2]+" "+separado[3], font=fntB, fill=color)

    if numeroPalabras == 5:
        fntB = ImageFont.truetype(dirfntB, 111)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 16:
            d.text((165.5078/1.3,394.4723/1.3), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723),separado[3]+" "+separado[4], font=fntB, fill=color)
        else: 
            d.text((165.5078/1.3,394.4723/1.3), separado[0]+" "+separado[1], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723),separado[2]+" "+separado[3]+" "+separado[4], font=fntB, fill=color)


    if numeroPalabras == 6:
        fntB = ImageFont.truetype(dirfntB, 91)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 16:
            d.text((165.5078/1.3,394.4723/1.3), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
        else: 
            d.text((165.5078/1.3,394.4723/1.3), separado[0]+" "+separado[1], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723),separado[2]+" "+separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)


    if numeroPalabras == 7:
        fntB = ImageFont.truetype(dirfntB, 86)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((165.5078/1.3,394.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.12),separado[5] +" "+separado[6], font=fntB, fill=color)
        else: 
            d.text((165.5078/1.3,394.4723/1.3), separado[0]+" "+separado[1], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723),separado[2]+" "+separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)

    if numeroPalabras == 8:
        fntB = ImageFont.truetype(dirfntB, 86)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((165.5078/1.3,394.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.12),separado[5] +" "+separado[6]+" "+separado[7], font=fntB, fill=color)
        else: 
            d.text((165.5078/1.3,394.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.12),separado[5] +" "+separado[6]+" "+separado[7], font=fntB, fill=color)

    if numeroPalabras == 9:
        fntB = ImageFont.truetype(dirfntB, 86)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((165.5078/1.3,394.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.12),separado[6]+" "+separado[7]+" "+separado[8], font=fntB, fill=color)

    if numeroPalabras == 10:
        fntB = ImageFont.truetype(dirfntB, 86)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((165.5078/1.3,394.4723/1.38), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.12),separado[6]+" "+separado[7]+" "+separado[8]+" "+separado[9], font=fntB, fill=color)

    if diaC == "Lunes-Jueves":
            d.text((165.5078*1.019/1.3,394.4723*1.48),numeroC, font=fntR, fill=(76, 76, 76,255))
    if diaC == "Martes-Viernes":
        d.text((165.5078*1.019/1.3,394.4723*1.48),numeroC, font=fntR, fill=(76, 76, 76,255))
    if diaC == "Miercoles-Sábado":
        d.text((165.5078*1.019/1.3,394.4723*1.48),numeroC, font=fntR, fill=(128,0,128, 255))


    out = Image.alpha_composite(base, txt)

    out.show()

    return out

imagen_1("Lunes-Jueves","MI AMIGO JESÚS","10")
