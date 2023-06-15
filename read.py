from PIL import Image

def readPixelData(file, convertTable) -> str:

    #apre e inizializza largezza e altezza
    image = Image.open(file)
    larghezza, altezza = image.size
    pixel: list[list[int, ...], ...] = []

    #va nell'immagine e prende il colore dell'immagine organizzandoli in righe
    '''[
        [(255,255,255), (30,34,89),    (78, 65,52), ...]
        [(0,98,76),     (123, 54, 76), ...]
        .
        .
        .
    ]'''
    for y in range(altezza):
        line: list = []
        for x in range(larghezza):
            colore = image.getpixel((x, y))
            line.append(colore)
        pixel.append(line)

    #costruisce la lista che contiene tutti i valori rgb in fila
    out: list[int, ... ] = []
    for y in range(altezza):
        for x in range(larghezza):
            if x < len(pixel[y]) and y < len(pixel):
                for i in range(3):
                    out.append(pixel[y][x][i])
            else:
                for i in range(3):
                    out.append(0)

    #traduce la lista out secondo la convertTable
    out2: list = ""
    for i in out:
        if i - 100 >= 0 and i - 100 < len(convertTable):
           out2 += convertTable[i - 100]
    return out2