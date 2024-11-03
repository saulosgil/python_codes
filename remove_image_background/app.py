# Remove image background
# Libraries
from rembg import remove
from PIL import Image

# Paths
input_path = 'remove_image_background\images\mickey_input.jpg'
output_path = 'remove_image_background\images\mickey_output.png'

# Open image with background and save in the inp object
inp = Image.open(input_path)

# Remove background and save in the output object
output = remove(inp)

# save the image witout backgroundin the path
output.save(output_path)

# Open the image without background
Image.open('mickey_output.png')