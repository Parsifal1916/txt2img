from txt2imgConverter import read
from txt2imgConverter import write
import random
convertTable: str = " 1234567890abcdefghilmnopqrstuvwxyzjkABCDEFGHILMNOPQRSTUVWXYZJK\\/!\"\'|£$%&/()=+-*><,.-;:_{}[]#@^\n\t"

ReadFile = lambda file : read.readPixelData(file, convertTable)
WriteFile = lambda file : write.convertDataToPixel(file, convertTable)
def shuffleTable() -> str:
	global convertTable
	newCT: list = list(convertTable)
	convertTable = random.shuffle(newCT)
	"".join(newCT)
	return convertTable