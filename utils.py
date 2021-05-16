from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def createArray(size:tuple,value):
    array = []
    for x in range(size[1]):
        array.append([])
        for y in range(size[0]):
            array[x].append(value.copy())
    return array

def loadImages(tiles):
    imgs = {}
    for key in tiles.keys():
        with Image.open(f'tileset/{key}.png') as im:
            if im == None : print('missing')
            imgs[key] = im
    return imgs

def renderGrid(grid,gridResolution,gridSize,ID):
    img = Image.new('RGB', (gridResolution[0] * gridSize[0], gridResolution[1] * gridSize[1]))
    for x in range(gridSize[0]):
        for y in range(gridSize[1]):
            if len(grid[x][y]) == 1:
                tile = str(list(grid[x][y].keys())[0])
                with Image.open(f'tileset1010/{tile}.png') as im:
                    img.paste(im, (x * gridResolution[0], y * gridResolution[1]))
            else :
                a = len(grid[x][y])
                ImageDraw.Draw(img).text((x * gridResolution[0], y * gridResolution[1]),str(a))

    img.save(f'render/{ID}.png')

def possibleTiles (_list, direction):
    values = []
    for keys in _list:
        for a in _list[keys][direction]:
            values.append(a)
    a = list(dict.fromkeys(values))
    return a
