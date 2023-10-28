from PIL import Image
import os

# Set the input and output folder paths and the desired size
input_folder = "Snake_Photos/8"
output_folder = "Snake_Photos/8"
desired_size = (256, 256)

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all files in the input folder
input_files = os.listdir(input_folder)

for filename in input_files:
    # Check if the file is an image (you can add more file extensions as needed)
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        # Open the image using Pillow
        image = Image.open(os.path.join(input_folder, filename))

        # Resize the image to the desired size
        image = image.resize(desired_size, Image.ANTIALIAS)

        # Save the resized image to the output folder
        image.save(os.path.join(output_folder, filename))

print("Image resizing complete.")