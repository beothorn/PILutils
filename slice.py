from PIL import Image, ImageFilter
from math import ceil
import sys

if len(sys.argv) != 3:
    print("Usage slice image grid_size")
    sys.exit(0)

original_img = sys.argv[1]
grid_size = int(sys.argv[2])

im = Image.open( original_img )
width, height = im.size


cell_count_horizontal = ceil(width/grid_size)
cell_count_vertical = ceil(height/grid_size)

for i in range(cell_count_horizontal):
    for j in range(cell_count_vertical):
        left = i*grid_size
        upper = j*grid_size
        right = left + grid_size
        lower = upper + grid_size
        region = im.crop((left, upper, right, lower))
        new_img = Image.new('RGBA', (grid_size, grid_size) , (0, 0, 0, 255))
        new_img.paste(region, (0, 0, grid_size, grid_size))
        new_img.save("slice"+str(i)+"_"+str(j)+".png")
