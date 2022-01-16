from os import sep
from conf import FONTS_DIR, FONDOS_LUNES, FONDOS_MARTES, FONDOS_MIERCOLES, FONDOS_JUEVES, FONDOS_VIERNES, FONDOS_SABADO
from PIL import Image, ImageDraw, ImageFont
import os
# get an image

lunes_1 = os.path.join(FONDOS_LUNES,'fondoLunes_1.png')
martes_1 = os.path.join(FONDOS_MARTES,'fondoMartes_1.png')
miercoles_1 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_1.png')
jueves_1 = os.path.join(FONDOS_JUEVES,'fondoJueves_1.png')
viernes_1 = os.path.join(FONDOS_VIERNES,'fondoViernes_1.png')
sabado_1 = os.path.join(FONDOS_SABADO,'fondoSabado_1.png')

lunes_2 = os.path.join(FONDOS_LUNES,'fondoLunes_2.png')
martes_2 = os.path.join(FONDOS_MARTES,'fondoMartes_2.png')
miercoles_2 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_2.png')
jueves_2 = os.path.join(FONDOS_JUEVES,'fondoJueves_2.png')
viernes_2 = os.path.join(FONDOS_VIERNES,'fondoViernes_2.png')
sabado_2 = os.path.join(FONDOS_SABADO,'fondoSabado_2.png')

lunes_3 = os.path.join(FONDOS_LUNES,'fondoLunes_3.png')
martes_3 = os.path.join(FONDOS_MARTES,'fondoMartes_3.png')
miercoles_3 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_3.png')
jueves_3 = os.path.join(FONDOS_JUEVES,'fondoJueves_3.png')
viernes_3 = os.path.join(FONDOS_VIERNES,'fondoViernes_3.png')
sabado_3 = os.path.join(FONDOS_SABADO,'fondoSabado_3.png')

lunes_4 = os.path.join(FONDOS_LUNES,'fondoLunes_4.png')
martes_4 = os.path.join(FONDOS_MARTES,'fondoMartes_4.png')
miercoles_4 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_4.png')
jueves_4 = os.path.join(FONDOS_JUEVES,'fondoJueves_4.png')
viernes_4 = os.path.join(FONDOS_VIERNES,'fondoViernes_4.png')
sabado_4 = os.path.join(FONDOS_SABADO,'fondoSabado_4.png')

lunes_5 = os.path.join(FONDOS_LUNES,'fondoLunes_5.png')
martes_5 = os.path.join(FONDOS_MARTES,'fondoMartes_5.png')
miercoles_5 = os.path.join(FONDOS_MIERCOLES,'fondoMiercoles_5.png')
jueves_5 = os.path.join(FONDOS_JUEVES,'fondoJueves_5.png')
viernes_5 = os.path.join(FONDOS_VIERNES,'fondoViernes_5.png')
sabado_5 = os.path.join(FONDOS_SABADO,'fondoSabado_5.png')

dirfntB = os.path.join(FONTS_DIR,'Bebas Neue Pro Bold.otf')
dirfntR = os.path.join(FONTS_DIR,'Bebas Neue Pro Regular.otf')


def imagen_1(dia, titulo, numeroC):
    base = ""
    if dia == "Lunes":
        base = Image.open(lunes_1).convert('RGBA')
    if dia == "Martes":
        base = Image.open(martes_1).convert('RGBA')
    if dia == "Miercoles":
        base = Image.open(miercoles_1).convert('RGBA')
    if dia == "Jueves":
        base = Image.open(jueves_1).convert('RGBA')
    if dia == "Viernes":
        base = Image.open(viernes_1).convert('RGBA')
    if dia == "Sabado":
        base = Image.open(sabado_1).convert('RGBA')

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

def imagen_2(dia, titulo, numeroC):
    base = ""

    if dia == "Lunes":
        base = Image.open(lunes_2).convert('RGBA')
    if dia == "Martes":
        base = Image.open(martes_2).convert('RGBA')
    if dia == "Miercoles":
        base = Image.open(miercoles_2).convert('RGBA')
    if dia == "Jueves":
        base = Image.open(jueves_2).convert('RGBA')
    if dia == "Viernes":
        base = Image.open(viernes_2).convert('RGBA')
    if dia == "Sabado":
        base = Image.open(sabado_2).convert('RGBA')

    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fntB = ImageFont.truetype(dirfntB, 59)
    fntR = ImageFont.truetype(dirfntR, 30)

    d = ImageDraw.Draw(txt)


    diaC = dia
    w=1080
    h=1080
    

    fontsize_1 = fntB.getsize(titulo)
    fontsize_2 = fntR.getsize("REFLEXIÓN #"+numeroC)


    if diaC == "Jueves":
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.23), titulo, font=fntB, fill=(0, 255, 0,255))
    elif diaC == "Viernes":
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.23), titulo, font=fntB, fill=(241,90,36,255))
    else:
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.23), titulo, font=fntB, fill=(255, 255, 255,255))


    if diaC == "Lunes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.09), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 0,255))
    if diaC == "Martes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.09), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 255,255))
    if diaC == "Miercoles" or diaC == "Sabado":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.09), "REFLEXIÓN #"+numeroC, font=fntR, fill=(255, 255, 0,255))
    if diaC == "Viernes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.09), "REFLEXIÓN #"+numeroC, font=fntR, fill=(96, 56, 19,255))
    if diaC == "Jueves":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.09), "REFLEXIÓN #"+numeroC, font=fntR, fill=(255,255,255,255))


    out = Image.alpha_composite(base, txt)

    out.show()

    return out


def imagen_3(dia, titulo, numeroC):
    base = ""

    if dia == "Lunes":
        base = Image.open(lunes_3).convert('RGBA')
    if dia == "Martes":
        base = Image.open(martes_3).convert('RGBA')
    if dia == "Miercoles":
        base = Image.open(miercoles_3).convert('RGBA')
    if dia == "Jueves":
        base = Image.open(jueves_3).convert('RGBA')
    if dia == "Viernes":
        base = Image.open(viernes_3).convert('RGBA')
    if dia == "Sabado":
        base = Image.open(sabado_3).convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fntB = ImageFont.truetype(dirfntB, 67)
    fntR = ImageFont.truetype(dirfntR, 35)
    # get a drawing context
    d = ImageDraw.Draw(txt)


    diaC = dia
    w=1080
    h=1920
    

    fontsize_1 = fntB.getsize(titulo)
    fontsize_2 = fntR.getsize("REFLEXIÓN #"+numeroC)


    if diaC == "Jueves":
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.285), titulo, font=fntB, fill=(0, 255, 0,255))
    elif diaC == "Viernes":
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.285), titulo, font=fntB, fill=(241,90,36,255))
    else:
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.285), titulo, font=fntB, fill=(255, 255, 255,255))


    if diaC == "Lunes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 0,255))
    if diaC == "Martes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 255,255))
    if diaC == "Miercoles" or diaC == "Sabado":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(255, 255, 0,255))
    if diaC == "Viernes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(96, 56, 19,255))
    if diaC == "Jueves":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(255,255,255,255))


    out = Image.alpha_composite(base, txt)

    out.show()

    return out



def imagen_4(dia, titulo, numeroC):
    base = ""

    if dia == "Lunes":
        base = Image.open(lunes_4).convert('RGBA')
    if dia == "Martes":
        base = Image.open(martes_4).convert('RGBA')
    if dia == "Miercoles":
        base = Image.open(miercoles_4).convert('RGBA')
    if dia == "Jueves":
        base = Image.open(jueves_4).convert('RGBA')
    if dia == "Viernes":
        base = Image.open(viernes_4).convert('RGBA')
    if dia == "Sabado":
        base = Image.open(sabado_4).convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fntB = ImageFont.truetype(dirfntB, 59)
    fntR = ImageFont.truetype(dirfntR, 30)
    # get a drawing context
    d = ImageDraw.Draw(txt)


    diaC = dia
    w=1080
    h=1080
    

    fontsize_1 = fntB.getsize(titulo)
    fontsize_2 = fntR.getsize("REFLEXIÓN #"+numeroC)


    if diaC == "Jueves":
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.245), titulo, font=fntB, fill=(0, 255, 0,255))
    elif diaC == "Viernes":
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.245), titulo, font=fntB, fill=(241,90,36,255))
    else:
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.245), titulo, font=fntB, fill=(255, 255, 255,255))


    if diaC == "Lunes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.10), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 0,255))
    if diaC == "Martes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.10), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 255,255))
    if diaC == "Miercoles" or diaC == "Sabado":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.10), "REFLEXIÓN #"+numeroC, font=fntR, fill=(255, 255, 0,255))
    if diaC == "Viernes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.10), "REFLEXIÓN #"+numeroC, font=fntR, fill=(96, 56, 19,255))
    if diaC == "Jueves":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.10), "REFLEXIÓN #"+numeroC, font=fntR, fill=(255,255,255,255))


    out = Image.alpha_composite(base, txt)

    return out




def imagen_5(dia, titulo, numeroC):
    base = ""

    if dia == "Lunes":
        base = Image.open(lunes_5).convert('RGBA')
    if dia == "Martes":
        base = Image.open(martes_5).convert('RGBA')
    if dia == "Miercoles":
        base = Image.open(miercoles_5).convert('RGBA')
    if dia == "Jueves":
        base = Image.open(jueves_5).convert('RGBA')
    if dia == "Viernes":
        base = Image.open(viernes_5).convert('RGBA')
    if dia == "Sabado":
        base = Image.open(sabado_5).convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fntB = ImageFont.truetype(dirfntB, 67)
    fntR = ImageFont.truetype(dirfntR, 35)
    # get a drawing context
    d = ImageDraw.Draw(txt)


    diaC = dia
    w=1080
    h=1920
    

    fontsize_1 = fntB.getsize(titulo)
    fontsize_2 = fntR.getsize("REFLEXIÓN #"+numeroC)


    if diaC == "Jueves":
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.285), titulo, font=fntB, fill=(0, 255, 0,255))
    elif diaC == "Viernes":
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.285), titulo, font=fntB, fill=(241,90,36,255))
    else:
        d.text((((w/2)-(fontsize_1[0]/2)),h/1.285), titulo, font=fntB, fill=(255, 255, 255,255))


    if diaC == "Lunes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 0,255))
    if diaC == "Martes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(0, 255, 255,255))
    if diaC == "Miercoles" or diaC == "Sabado":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(255, 255, 0,255))
    if diaC == "Viernes":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(96, 56, 19,255))
    if diaC == "Jueves":
        d.text(((w/2)-(fontsize_2[0]/2),h/1.1838), "REFLEXIÓN #"+numeroC, font=fntR, fill=(255,255,255,255))


    out = Image.alpha_composite(base, txt)

    return out
