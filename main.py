import json
import random
import utils
import wavefunction

# todo find proper naming for everything

# initiate variables
directory = 'D:/Programming/006_Python/WaveFunctionCollapse/tilesets/dev-10'
render_frequency = 10
config_file = open(f'{directory}/config.json')
config_variables = json.load(config_file)

gridSize = (10, 10)
gridResolution = config_variables['resolution']

tiles = config_variables['tiles']

# this is temporary until I find a way to use strings as keys
# todo implement key with strings
for keys in list(tiles):
    tiles[int(keys)] = tiles.pop(keys)

# create default 'play area'
grid = utils.create_array(gridSize, tiles)

# choose a random starting tile
startX = random.randint(0, gridSize[0] - 1)
startY = random.randint(0, gridSize[1] - 1)
startKey = random.choice(list(tiles))
startTile = tiles[startKey]
grid[startX][startY].clear()
grid[startX][startY] = {startKey: startTile}

print(f'Starting at : {startX},{startY} with key {startKey}')

wavefunction.update_adjacent(grid, gridSize, (startX, startY))

ID = 0
while True:
    # propagate
    entropyMap = wavefunction.entropy_map(grid, gridSize)
    coord = wavefunction.consolidate_entropy(entropyMap, gridSize)
    # until all entropy is equal to 1
    if coord == False:
        break
    newKey = random.choice(list(grid[coord[0]][coord[1]]))
    newTile = tiles[newKey]
    grid[coord[0]][coord[1]].clear()
    grid[coord[0]][coord[1]] = {newKey: newTile}
    wavefunction.update_adjacent(grid, gridSize, (coord[0], coord[1]))

    # outpout an image every Nth render_frequency
    if ID % render_frequency == 0:
        utils.render_grid(grid, gridResolution, gridSize, ID, directory)
    ID += 1
    # print(f'with key {newKey}')

    wavefunction.propagate(grid, gridSize, coord)
print(f'--------Done in {ID} steps--------')
utils.render_grid(grid, gridResolution, gridSize, 'final', directory)
