from PIL import Image
import utils

class graphics:
    def __init__(self,gridResolution:tuple,gridSize:tuple,tiles):
        self.gridResolution = gridResolution
        self.gridSize = gridSize
        self.image = Image.new('RGB', (gridResolution[0]*gridSize[0],gridResolution[1]*gridSize[1]))
        self.tiles = utils.loadImages(tiles)
    def setTile(self,location:tuple,tile):

        self.image.paste(self.tiles[tile],(location[0]*self.gridResolution[0],location[1]*self.gridResolution[1]))

    def displayImage(self):
        self.image.show()
