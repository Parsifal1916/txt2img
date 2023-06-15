from PIL import Image
import numpy as np

def CreateFormPixels(pixel, altezza, larghezza):
    image = Image.new("RGB", (larghezza, altezza))

    for y in range(altezza):
        for x in range(larghezza):
            if y < len(pixel) and x < len(pixel[y]):
                color = tuple(pixel[y][x])
            else:
                color = (0, 0, 0)
            image.putpixel((x, y), color)

    return image

def transformArray(array):
    num_elements = len(array)
    num_arrays = (num_elements + 2) // 3
    padded_length = num_arrays * 3
    array += [0] * (padded_length - num_elements)
    return [array[i:i+3] for i in range(0, padded_length, 3)]

def convertDataToPixel(file, convertTable):
    with open(file, "r") as content:
        content = content.read()
        pixelsArrayBC = [findFromConvertTable(i) for i in content]
        pixelsArrayBC = transformArray(pixelsArrayBC)

        side = int(np.floor(np.sqrt(len(pixelsArrayBC))) + 1)

        newArray = [pixelsArrayBC[i:i+side] for i in range(0, len(pixelsArrayBC), side)]
        
        CreateFormPixels(newArray, side, side).save("risultato.png")

def findFromConvertTable(letter: str):
	for i in range(len(convertTable)):
		if convertTable[i] == letter: return i+100
	return 0