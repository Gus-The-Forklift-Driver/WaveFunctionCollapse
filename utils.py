from PIL import Image

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
                key = str(list(grid[x][y].keys()))
                key = key.replace('[\'', '')
                key = key.replace('\']', '')
                with Image.open(f'tileset/{key}.png') as im:
                    img.paste(im, (x * gridResolution[0], y * gridResolution[1]))
    img.save(f'render/{ID}.png')
