import random
import utils
import wavefunction
from PIL import Image

#initiate variables

gridSize = (20,20)
gridResolution = (5,5)
# 0,0 is top left corner
# 0 : up
# 1 : right
# 2 : down
# 3 : left
tiles = {

    "1": [1, 2, 3, 4],
    "2": [1, 2, 3],
    "3": [1, 2],
    "4": [0, 1],
    "5": [0, 3],
    "6": [2, 3],
    "7": [0, 1, 2],
    "8": [0, 1, 3],
    "9": [0, 2, 3],
}

grid = utils.createArray(gridSize,tiles)

#choose a starting tile

startX = random.randint(0,gridSize[0]-1)
startY = random.randint(0,gridSize[1]-1)
startKey = random.choice(list(tiles))
startTile = tiles[startKey]
print (f'Starting at : {startX},{startY} with key {startKey}')
grid[startX][startY].clear()
grid[startX][startY] = {startKey:startTile}


wavefunction.propagate(grid,gridSize,(startX,startY))

print (wavefunction.entropyMap(grid, gridSize))
ID = 0
while True:
    entropyMap = wavefunction.entropyMap(grid,gridSize)
    #print(entropyMap)
    coord = wavefunction.consolidateEntropy(entropyMap,gridSize)
    if coord == False:
        break
    #print(f'Updating : {coord[0]},{coord[1]} ', end='')
    newKey = random.choice(list(grid[coord[0]][coord[1]]))
    newTile = tiles[newKey]
    grid[coord[0]][coord[1]].clear()
    grid[coord[0]][coord[1]] = {newKey:newTile}
    utils.renderGrid(grid,gridResolution,gridSize,ID)
    ID += 1
    #print(f'with key {newKey}')


    wavefunction.propagate(grid,gridSize,coord)
print('--------Done--------')
print(grid)

