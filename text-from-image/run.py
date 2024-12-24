from PIL import Image
import pytesseract
import os

# Make sure to specify the path to the tesseract executable if it's not in your PATH
# For example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Extract text from the image using pytesseract
        text = pytesseract.image_to_string(img, lang='eng')

        # Define the output file path
        output_file = os.path.join(os.getcwd(), "output_text.txt")

        # Save the extracted text to a file
        with open(output_file, "w") as file:
            file.write(text)

        print(f"Text has been extracted and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
image_path = input("Enter the path to the image file: ")
image_to_text(image_path)
