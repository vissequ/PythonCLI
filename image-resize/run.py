import os
from PIL import Image

# Path to the folder containing images
folder_path = '.'

# Function to compress and resize images
def compress_and_resize_image(image_path, output_path, target_size_kb=500, max_dimension=1000):
    img = Image.open(image_path)
    
    # Resize image if dimensions exceed the max_dimension (preserving aspect ratio)
    if max(img.size) > max_dimension:
        ratio = max_dimension / max(img.size)
        new_size = tuple([int(x * ratio) for x in img.size])
        img = img.resize(new_size, Image.LANCZOS)  # Use LANCZOS for high-quality downsampling
    
    quality = 85  # Starting quality
    img_format = img.format
    
    # Compress the image until it's under the target size
    while True:
        img.save(output_path, format=img_format, quality=quality, optimize=True)
        file_size_kb = os.path.getsize(output_path) / 1024  # Get file size in KB
        
        if file_size_kb <= target_size_kb or quality <= 10:
            break
        
        quality -= 5  # Reduce the quality in steps to achieve target size

# Scan the folder and compress each image
def compress_images_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file)
                output_path = os.path.join(root, f"compressed_{file}")
                compress_and_resize_image(image_path, output_path)

# Run the script
compress_images_in_folder(folder_path)
