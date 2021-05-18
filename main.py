import random
import utils
import wavefunction
from PIL import Image

# initiate variables

gridSize = (50, 50)
gridResolution = (10, 10)
# 0,0 is top left corner
# 0 : up
# 1 : right
# 2 : down
# 3 : left
tiles = {

    1: [[1, 2, 3, 6, 7, 9], [1, 2, 5, 6, 8, 9], [1, 4, 5, 7, 8, 9], [1, 2, 3, 4, 7, 8]],
    2: [[4, 5, 8], [1, 2, 5, 6, 8, 9], [1, 4, 5, 7, 8, 9], [1, 2, 3, 4, 7, 8]],
    3: [[4, 5, 8], [1, 2, 5, 6, 8, 9], [1, 4, 5, 7, 8, 9], [5, 6, 9]],
    4: [[1, 2, 3, 6, 7, 9], [1, 2, 5, 6, 8, 9], [2, 3, 6], [5, 6, 9]],
    5: [[1, 2, 3, 6, 7, 9], [3, 4, 7], [2, 3, 6], [1, 2, 3, 4, 7, 8]],
    6: [[4, 5, 8], [3, 4, 7], [1, 4, 5, 7, 8, 9], [1, 2, 3, 4, 7, 8]],
    7: [[1, 2, 3, 6, 7, 9], [1, 2, 5, 6, 8, 9], [1, 4, 5, 7, 8, 9], [5, 6, 9]],
    8: [[1, 2, 3, 6, 7, 9], [1, 2, 5, 6, 8, 9], [2, 3, 6], [1, 2, 3, 4, 7, 8]],
    9: [[1, 2, 3, 6, 7, 9], [3, 4, 7], [1, 4, 5, 7, 8, 9], [1, 2, 3, 4, 7, 8]],
}

grid = utils.createArray(gridSize, tiles)

# choose a starting tile

# import json
# print(json.dumps(grid))

startX = random.randint(0, gridSize[0] - 1)
startY = random.randint(0, gridSize[1] - 1)
startKey = random.choice(list(tiles))
startTile = tiles[startKey]
print(f'Starting at : {startX},{startY} with key {startKey}')
grid[startX][startY].clear()
grid[startX][startY] = {startKey: startTile}

wavefunction.updateAdjacent(grid, gridSize, (startX, startY))

print(wavefunction.entropyMap(grid, gridSize))

ID = 0
while True:
    entropyMap = wavefunction.entropyMap(grid, gridSize)
    # print(entropyMap)
    coord = wavefunction.consolidateEntropy(entropyMap, gridSize)
    if coord == False:
        break
    # print(f'Updating : {coord[0]},{coord[1]} ', end='')
    newKey = random.choice(list(grid[coord[0]][coord[1]]))
    newTile = tiles[newKey]
    grid[coord[0]][coord[1]].clear()
    grid[coord[0]][coord[1]] = {newKey: newTile}
    wavefunction.updateAdjacent(grid, gridSize, (coord[0], coord[1]))
    if ID % 10 == 0:
        utils.renderGrid(grid, gridResolution, gridSize, ID)
    ID += 1
    # print(f'with key {newKey}')

    wavefunction.propagate(grid, gridSize, coord)
print('--------Done--------')
utils.renderGrid(grid, gridResolution, gridSize, 'final')
