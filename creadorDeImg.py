from os import sep
from conf import FONTS_DIR, FONDOS_LUNES, FONDOS_MARTES, FONDOS_MIERCOLES
from PIL import Image, ImageDraw, ImageFont
import os
# get an image

lunes_1 = os.path.join(FONDOS_LUNES,'Lunes-Jueves.png')
martes_1 = os.path.join(FONDOS_MARTES,'Martes-Viernes.png')
miercoles_1 = os.path.join(FONDOS_MIERCOLES,'Miercoles-Sabado.png')

dirfntB = os.path.join(FONTS_DIR,'Bison-Bold(PersonalUse).ttf')
dirfntR = os.path.join(FONTS_DIR,'Bison-DemiBold.ttf')


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
    fntR = ImageFont.truetype(dirfntR, 44)
    # get a drawing context
    d = ImageDraw.Draw(txt)


    numeroPalabras = 0
    diaC = dia
    separado = titulo.split()
    white = (255,255,255,255)
    color = ""

    if dia=="Lunes-Jueves":
        color=(76,76,76,255)
    else:
        color=white


    for i in separado:
        numeroPalabras += 1


    numeroCaracteres = len(titulo)


    if numeroPalabras == 1:
        
        d.text((165.5078/1.3,394.4723/1.28), separado[0], font=fntB, fill=color)

    if numeroPalabras == 2:

        
        d.text((165.5078/1.3,394.4723/1.56), separado[0], font=fntB, fill=color)
        d.text((165.5078/1.3,394.4723), separado[1], font=fntB, fill=color)
    if numeroPalabras == 3:

        
        d.text((165.5078/1.3,394.4723/1.56), separado[0]+" "+separado[1], font=fntB, fill=color)
        d.text((165.5078/1.3,394.4723), separado[2], font=fntB, fill=color)

    if numeroPalabras == 4:

        
        d.text((165.5078/1.3,394.4723/1.56), separado[0]+" "+separado[1], font=fntB, fill=color)
        d.text((165.5078/1.3,394.4723), separado[2]+" "+separado[3], font=fntB, fill=color)

    if numeroPalabras == 5:
        fntB = ImageFont.truetype(dirfntB, 161)
        #if len(separado[0])+len(separado[1])+len(separado[2]) <= 16:
        d.text((165.5078/1.3,394.4723/1.56), separado[0]+" "+separado[1], font=fntB, fill=color)
        d.text((165.5078/1.3,394.4723),separado[2]+" "+separado[3], font=fntB, fill=color)
        d.text((165.5078/1.3,394.4723*1.365),separado[4], font=fntB, fill=color)
        #else:
        #d.text((165.5078/1.3,394.4723/1.56), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
        #d.text((165.5078/1.3,394.4723),separado[3]+" "+separado[4], font=fntB, fill=color)


    if numeroPalabras == 6:
        fntB = ImageFont.truetype(dirfntB, 157)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 16:
            d.text((165.5078/1.3,394.4723/1.7387), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
        #    d.text((165.5078/1.3,394.4723*1.27),separado[5], font=fntB, fill=color)
        #else: 
        #    d.text((165.5078/1.3,394.4723/1.56), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
        #    d.text((165.5078/1.3,394.4723/1),separado[3]+" "+separado[4], font=fntB, fill=color)
        #    d.text((165.5078/1.3,394.4723*1.27),separado[5], font=fntB, fill=color)


    if numeroPalabras == 7:
        fntB = ImageFont.truetype(dirfntB, 157)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((165.5078/1.3,394.4723/1.7387), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.27),separado[5] +" "+separado[6], font=fntB, fill=color)
        #else: 
        #    d.text((165.5078/1.3,394.4723/1.3), separado[0]+" "+separado[1], font=fntB, fill=color)
        #    d.text((165.5078/1.3,394.4723),separado[2]+" "+separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
        #    d.text((165.5078/1.3,394.4723),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)

    if numeroPalabras == 8:
        fntB = ImageFont.truetype(dirfntB, 157)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((165.5078/1.3,394.4723/1.7387), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.27),separado[5] +" "+separado[6], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.6173),separado[7], font=fntB, fill=color)
        #else: 
        #    d.text((165.5078/1.3,394.4723/1.7387), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
        #    d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4], font=fntB, fill=color)
        #    d.text((165.5078/1.3,394.4723*1.27),separado[5] +" "+separado[6]+" "+separado[7], font=fntB, fill=color)

    if numeroPalabras == 9:
        fntB = ImageFont.truetype(dirfntB, 157)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((165.5078/1.3,394.4723/1.7387), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.27),separado[6]+" "+separado[7]+" "+separado[8], font=fntB, fill=color)

    if numeroPalabras == 10:
        fntB = ImageFont.truetype(dirfntB, 157)
        if len(separado[0])+len(separado[1])+len(separado[2]) <= 18:
            d.text((165.5078/1.3,394.4723/1.7387), separado[0]+" "+separado[1]+" "+separado[2], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723/1.085),separado[3]+" "+separado[4]+" "+separado[5], font=fntB, fill=color)
            d.text((165.5078/1.3,394.4723*1.27),separado[6]+" "+separado[7]+" "+separado[8]+" "+separado[9], font=fntB, fill=color)

    if diaC == "Lunes-Jueves":
        d.text((165.5078*2.45,394.4723*2.123),numeroC, font=fntR, fill=(76, 76, 76,255))
    if diaC == "Martes-Viernes":
        d.text((165.5078*2.5,394.4723*2.123),numeroC, font=fntR, fill=(105, 57, 23,255))
    if diaC == "Miercoles-Sábado":
        d.text((165.5078*2.59,394.4723*2.123),numeroC, font=fntR, fill=(115, 45, 145, 255))


    out = Image.alpha_composite(base, txt)

    out.show()

    return out
