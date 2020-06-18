from PIL import Image, ImageFilter
from math import ceil
import sys

if len(sys.argv) != 4:
    print("Usage image grid_size border_size")
    sys.exit(0)

original_img = sys.argv[1]
grid_size = int(sys.argv[2])
border_size = int(sys.argv[3])

im = Image.open( original_img )
width, height = im.size

cell_total_size = grid_size + border_size

cell_count_horizontal = ceil(width/cell_total_size)
cell_count_vertical = ceil(height/cell_total_size)

for i in range(cell_count_horizontal):
    for j in range(cell_count_vertical):
        left = i*cell_total_size
        upper = j*cell_total_size
        right = left + grid_size
        lower = upper + grid_size
        region = im.crop((left, upper, right, lower))
        new_left = i * grid_size 
        new_upper = j * grid_size
        new_right = new_left + grid_size
        new_lower = new_upper + grid_size
        im.paste(region, (new_left, new_upper, new_right, new_lower))
new_img = Image.new('RGBA', (cell_count_horizontal * grid_size, cell_count_vertical * grid_size), (0, 0, 0, 255))
new_img.paste(im)
new_img.save("joined."+original_img)
