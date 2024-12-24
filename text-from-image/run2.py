import os
from PIL import Image
import pytesseract

# Specify the path to the input directory containing images
input_directory = os.path.join(os.getcwd(), "input")

# Ensure Tesseract executable path is set if necessary
# Example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path, output_file):
    try:
        # Open the image
        img = Image.open(image_path)

        # Extract text from the image using pytesseract
        text = pytesseract.image_to_string(img, lang='eng')

        # Save the extracted text to a file
        with open(output_file, "w") as file:
            file.write(text)

        print(f"Text from {os.path.basename(image_path)} has been saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while processing {image_path}: {e}")

# Process all image files in the input directory
def process_images():
    if not os.path.exists(input_directory):
        print(f"Directory '{input_directory}' does not exist.")
        return

    for filename in os.listdir(input_directory):
        # Check if the file is an image (you can expand the list of extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join(input_directory, filename)
            output_file = os.path.join(os.getcwd(), f"{os.path.splitext(filename)[0]}.txt")
            image_to_text(image_path, output_file)

# Run the process
process_images()
