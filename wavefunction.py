import random
import utils


def propagate(grid, grid_size, cell):
    x = cell[0]
    y = cell[1]
    if len(grid[x][y]) == 1:
        return

    updated = False
    # check if no too high
    if y != 0:
        if update_cell(grid[x][y], grid[x][y - 1], 2):
            updated = True

    if y != grid_size[1] - 1:
        if update_cell(grid[x][y], grid[x][y + 1], 0):
            updated = True

    if x != 0:
        if update_cell(grid[x][y], grid[x - 1][y], 1):
            updated = True

    if x != grid_size[0] - 1:
        if update_cell(grid[x][y], grid[x + 1][y], 3):
            updated = True

    if updated:
        update_adjacent(grid, grid_size, cell)


def update_adjacent(grid, gridSize, cell):
    x = cell[0]
    y = cell[1]
    if x != gridSize[0] - 1:
        propagate(grid, gridSize, (x + 1, y))
    if x != 0:
        propagate(grid, gridSize, (x - 1, y))
    if y != gridSize[1] - 1:
        propagate(grid, gridSize, (x, y + 1))
    if y != 0:
        propagate(grid, gridSize, (x, y - 1))


def entropy_map(grid, gridSize):
    entropy = []
    for x in range(gridSize[0]):
        entropy.append([])
        for y in range(gridSize[1]):
            entropy[x].append(len(grid[x][y].keys()))
    return entropy


# todo put the whole consolidate entropy and entropy map together
# return the coordinates of a random low entropy tile
def consolidate_entropy(entropy_grid, grid_size):
    # todo change the way min is handled
    minimum = 50
    coordinates = []
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            if entropy_grid[x][y] == minimum:
                coordinates.append((x, y))
            if entropy_grid[x][y] < minimum and not entropy_grid[x][y] == 1:
                minimum = entropy_grid[x][y]
                coordinates.clear()
                coordinates.append((x, y))

    if minimum == 50:
        return False
    else:
        return random.choice(coordinates)


# update the current tiles
def update_cell(source, destination, direction):
    updated = False
    possibleTile = utils.possible_tiles(destination, direction)
    for sourceTiles in list(source):
        if sourceTiles not in possibleTile:
            # print(f'no match with source : {sourceTiles} destination : {possibleTile}')
            source.pop(sourceTiles)
            updated = True
    # only return updated because of python dict copy system
    return updated
