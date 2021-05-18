from PIL import Image
from PIL import ImageDraw


def create_array(size: tuple, value):
    array = []
    for x in range(size[1]):
        array.append([])
        for y in range(size[0]):
            array[x].append(value.copy())
    return array


# load all images into a array (not used)
def load_images(tiles):
    imgs = {}
    for key in tiles.keys():
        with Image.open(f'tileset/{key}.png') as im:
            if im is None:
                print(f'missing {key}.png')
            imgs[key] = im
    return imgs

# create a render of the grid with wheights
def render_grid(grid, gridResolution, gridSize, name, directory):
    img = Image.new('RGB', (gridResolution[0] * gridSize[0], gridResolution[1] * gridSize[1]))
    for x in range(gridSize[0]):
        for y in range(gridSize[1]):
            if len(grid[x][y]) == 1:
                tile = str(list(grid[x][y].keys())[0])
                with Image.open(f'{directory}/{tile}.png') as im:
                    img.paste(im, (x * gridResolution[0], y * gridResolution[1]))
            else:
                a = len(grid[x][y])
                ImageDraw.Draw(img).text((x * gridResolution[0], y * gridResolution[1]), str(a))

    img.save(f'render/{name}.png')

# return the possible tiles with a given direction
def possible_tiles(_list, direction):
    values = []
    for keys in _list:
        for a in _list[keys][direction]:
            values.append(a)
    a = list(dict.fromkeys(values))
    return a
