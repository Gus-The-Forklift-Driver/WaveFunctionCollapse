import random
import sys
import utils

# def propagate(grid,gridSize):
#     print('**************PROPAGATING**************')
#     sys.stdout.flush()
#     for x in range(gridSize[0]):
#         for y in range(gridSize[1]):
#             print(f'{x},{y}',end=' : ')
#             sys.stdout.flush()
#             if len(grid[x][y]) == 1:
#                 print("entropy too low skipping")
#                 pass
#             else :
#                 if y == 0:
#                     print("too low")
#                     sys.stdout.flush()
#                     pass
#                 else :
#                     print("processing",end=' : ')
#                     sys.stdout.flush()
#                     for tiles in list(grid[x][y]):
#                             if str(grid[x][y][tiles]) not in str(grid[x][y-1]) :
#                                 grid[x][y].pop(tiles)
#                                 print('=poped=',end='')
#                                 sys.stdout.flush()
#                     print('end')
#
#                 if y == gridSize[1]-1:
#                     print("too high")
#                     sys.stdout.flush()
#                     pass
#                 else :
#                     print("processing",end=' : ')
#                     sys.stdout.flush()
#                     for tiles in list(grid[x][y]):
#                             if str(grid[x][y][tiles]) not in str(grid[x][y+1]) :
#                                 grid[x][y].pop(tiles)
#                                 print('=poped=',end='')
#                                 sys.stdout.flush()
#                     print('end')
#
#                 if x == 0:
#                     print("too far right")
#                     sys.stdout.flush()
#                     pass
#                 else :
#                     print("processing",end=' : ')
#                     sys.stdout.flush()
#                     for tiles in list(grid[x][y]):
#                             if str(grid[x][y][tiles]) not in str(grid[x-1][y]) :
#                                 grid[x][y].pop(tiles)
#                                 print('=poped=',end='')
#                                 sys.stdout.flush()
#                     print('end')
#
#                 if x == gridSize[0]-1:
#                     print("too far left")
#                     sys.stdout.flush()
#                     pass
#                 else :
#                     print("processing",end=' : ')
#                     sys.stdout.flush()
#                     for tiles in list(grid[x][y]):
#                             if str(grid[x][y][tiles]) not in str(grid[x+1][y]) :
#                                 grid[x][y].pop(tiles)
#                                 print('=poped=',end='')
#                                 sys.stdout.flush()
#                     print('end')
#

# def propagate(grid, gridSize, cell):
#     x = cell[0]
#     y = cell[1]
#     updated = False
#     if len(grid[x][y]) == 1:
#         return
#     # check if no too high
#     if y == 0:
#         pass
#     else:
#         # check if can connect with adjacent cell
#         if '0' not in str(grid[x][y].values()):
#             # if not remove 'bad'  from the adjacent cell
#             for keys in list(grid[x][y - 1]):
#                 if '2' in str(grid[x][y - 1][keys]):
#                     grid[x][y - 1].pop(keys)
#                     updated = True
#             if updated :
#                 propagate(grid,gridSize,(x,y-1))
#                 updated = False
#         else :
#             for keys in list(grid[x][y - 1]):
#                 if '2' not in str(grid[x][y - 1][keys]):
#                     grid[x][y - 1].pop(keys)
#                     updated = True
#             if updated :
#                 propagate(grid,gridSize,(x,y-1))
#                 updated = False
#
#     if y == gridSize[1] - 1:
#         pass
#     else:
#         if '2' not in str(grid[x][y].values()):
#             for keys in list(grid[x][y + 1]):
#                 if '0' in str(grid[x][y + 1][keys]):
#                     grid[x][y + 1].pop(keys)
#                     updated = True
#             if updated:
#                 propagate(grid, gridSize, (x, y + 1))
#                 updated = False
#         else :
#             for keys in list(grid[x][y + 1]):
#                 if '0' not in str(grid[x][y + 1][keys]):
#                     grid[x][y + 1].pop(keys)
#                     updated = True
#             if updated :
#                 propagate(grid,gridSize,(x,y+1))
#                 updated = False
#
#     if x == 0:
#         pass
#     else:
#         if '3' not in str(grid[x][y].values()):
#             for keys in list(grid[x - 1][y]):
#                 if '1' in str(grid[x - 1][y][keys]):
#                     grid[x - 1][y].pop(keys)
#                     updated = True
#             if updated:
#                 propagate(grid, gridSize, (x-1, y ))
#                 updated = False
#         else :
#             for keys in list(grid[x-1][y]):
#                 if '1' not in str(grid[x-1][y][keys]):
#                     grid[x-1][y].pop(keys)
#                     updated = True
#             if updated :
#                 propagate(grid,gridSize,(x-1,y))
#                 updated = False
#
#     if x == gridSize[0] - 1:
#         pass
#     else:
#         if '3' not in str(grid[x][y].values()):
#             for keys in list(grid[x + 1][y]):
#                 if '1' in str(grid[x + 1][y][keys]):
#                     grid[x + 1][y].pop(keys)
#                     updated = True
#             if updated:
#                 propagate(grid, gridSize, (x+1, y))
#         else :
#             for keys in list(grid[x+1][y]):
#                 if '1' not in str(grid[x+1][y][keys]):
#                     grid[x+1][y].pop(keys)
#                     updated = True
#             if updated :
#                 propagate(grid,gridSize,(x+1,y))
#                 updated = False
#
#
#     if updated:
#         # if done any changes to the current cell propagate to adjacent ones
#         updateAdjacent(grid, gridSize, cell)

def propagate(grid, gridSize,cell):
    x = cell[0]
    y = cell[1]
    if len(grid[x][y]) == 1:
        return

    updated = False
    # check if no too high
    if y != 0:
        if updateCell(grid[x][y],grid[x][y-1],2):
            updated = True

    if y != gridSize[1]-1:
        if updateCell(grid[x][y], grid[x][y + 1], 0):
            updated = True

    if x != 0:
        if updateCell(grid[x][y], grid[x-1][y], 1):
            updated = True

    if x != gridSize[0]-1:
        if updateCell(grid[x][y], grid[x+1][y], 3):
            updated = True

    if updated:
        updateAdjacent(grid,gridSize,cell)



def updateAdjacent(grid, gridSize, cell):
    x = cell[0]
    y = cell[1]
    if x != gridSize[0]-1:
        propagate(grid, gridSize, (x + 1, y))
    if x != 0:
        propagate(grid, gridSize, (x - 1, y))
    if y != gridSize[1]-1:
        propagate(grid, gridSize, (x, y + 1))
    if y != 0:
        propagate(grid, gridSize, (x, y - 1))


def entropyMap(grid, gridSize):
    entropy = []
    for x in range(gridSize[0]):
        entropy.append([])
        for y in range(gridSize[1]):
            entropy[x].append(len(grid[x][y].keys()))
    return entropy


def consolidateEntropy(entropyGrid, gridSize):
    min = 50
    coords = []
    for x in range(gridSize[0]):
        for y in range(gridSize[1]):
            if entropyGrid[x][y] == min:
                coords.append((x, y))
            if entropyGrid[x][y] < min and not entropyGrid[x][y] == 1:
                min = entropyGrid[x][y]
                coords.clear()
                coords.append((x, y))

    if min == 50 :
        return False
    else:
        return random.choice(coords)

def updateCell(source, destination, direction):
    updated = False
    possibleTile = utils.possibleTiles(destination, direction)
    #print(possibleTile)
    for sourceTiles in list(source):
        if sourceTiles not in possibleTile:
            #print(f'no match with source : {sourceTiles} destination : {possibleTile}')
            #sys.stdout.flush()
            source.pop(sourceTiles)
            updated = True
    return  updated