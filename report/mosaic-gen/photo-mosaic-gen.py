# borrowed code from - https://towardsdatascience.com/how-to-create-a-photo-mosaic-in-python-45c94f6e8308
import glob
import os
from PIL import Image
from scipy import spatial
import numpy as np

# Sources and settings
parent_dir = os.path.abspath(os.path.dirname(__file__))
main_photo_path = os.path.realpath(os.path.join(parent_dir, "Pose-Virabhadrasana-II.png"))
print(main_photo_path)
# main_photo_path = os.path.realpath(os.path.join(parent_dir, '../dataset-for-classification/virabhadrasana-ii/773da925d613f5ccab093c82dc12b44846451ce56864ce7c3e6cf8386c935f8b.png'))
tile_photos_path = os.path.realpath(os.path.join(parent_dir, "../dataset-for-classification/**/*.png"))
tile_size = (20, 20)


# Get all tiles
tile_paths = []
for file in glob.glob(tile_photos_path):
	tile_paths.append(file)

	
# Import and resize all tiles
tiles = []
for path in tile_paths:
	tile = Image.open(path).convert('RGBA')
	tile = tile.resize(tile_size)
	tiles.append(tile)
	

colors = []
for tile in tiles:
	mean_color = np.array(tile).mean(axis=0).mean(axis=0)
	colors.append(mean_color)

print(colors)
	

# Pixelate (resize) main photo
main_photo = Image.open(main_photo_path).convert('RGBA')

width = int(np.round(main_photo.size[0] / tile_size[0]))
height = int(np.round(main_photo.size[1] / tile_size[1]))

resized_photo = main_photo.resize((width, height))

# Find closest tile photo for every pixel

# Create a KDTree
tree = spatial.KDTree(colors)

# Empty integer array to store indices of tiles
closest_tiles = np.zeros((width, height), dtype=np.uint32)

for i in range(width):
    for j in range(height):
        pixel = resized_photo.getpixel((i, j))  # Getthe pixel color at (i, j)
        closest = tree.query(pixel)             # Returns (distance, index)
        closest_tiles[i, j] = closest[1]        # We only need the index
		

# Create an output image
output = Image.new('RGB', main_photo.size)

# Draw tiles
for i in range(width):
	for j in range(height):
		# Offset of tile
		x, y = i*tile_size[0], j*tile_size[1]
		# Index of tile
		index = closest_tiles[i, j]
		# Draw tile
		output.paste(tiles[index], (x, y))

# Save output
output.save("output.jpg")