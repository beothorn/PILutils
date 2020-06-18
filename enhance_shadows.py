from PIL import Image, ImageFilter, ImageChops, ImageEnhance
import sys

original_img = sys.argv[1]
dest_img = sys.argv[2]
mask_strength = sys.argv[3]

original = Image.open(original_img)
gray = original.convert("LA")
blurred = gray.filter(ImageFilter.GaussianBlur(radius=5))
blurred = blurred.convert("RGB")
enhancer = ImageEnhance.Brightness(blurred)
blurred = enhancer.enhance(float(mask_strength))
multiplied= ImageChops.multiply(original, blurred)
multiplied.save(dest_img)
