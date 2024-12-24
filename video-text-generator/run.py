from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip
import os
import subprocess
import platform
import random

# Import text from file with UTF-8 encoding
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.upper()

RECOGNIZED_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$.,;?!\"' ")

def check_for_unrecognized_chars(word):
    for char in word:
        if char not in RECOGNIZED_CHARS:
            print(f"WARNING: Unrecognized character '{char}' found in word '{word}'.")



# Replace curly quotes with straight ones
text = text.replace('“', '"').replace('”', '"')
text = text.replace('‘', "'").replace('’', "'")

# Split the text into words
words = text.split()

# Create a folder to store generated images
if not os.path.exists('frames'):
    os.makedirs('frames')

# Parameters
image_size = (1080, 1920)
frames = []
durations = []

# Predefined list of colors (R, G, B, A)
predefined_colors = [
    (255, 0, 0, 255),
    (255, 255, 255, 255),
]

# Use only "infinite.ttf" font
selected_font = "infinite.ttf"

# Initialize last color variable
last_color = None

# Additional pause duration for words ending with a period
additional_pause_for_period = 1.0  # 1 second

# Generate images
for i, word in enumerate(words):

    check_for_unrecognized_chars(word)

    if len(word) >= 12:
        font_size = 55
    else:
        font_size = 90

    font = ImageFont.truetype(selected_font, font_size)

    img = Image.new('RGBA', image_size, (0, 255, 0, 255))
    d = ImageDraw.Draw(img)

    # Use textbbox() instead of textsize()
    text_bbox = d.textbbox((0, 0), word, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

    # Randomly pick a new color that is different from the last one
    random_color = random.choice([color for color in predefined_colors if color != last_color])
    last_color = random_color  # Update last color
    
    d.text(position, word, fill=random_color, font=font)
    
    frame_path = f'frames/frame_{i}.png'
    img.save(frame_path)
    
    frames.append(frame_path)
    
    x = len(word)
    print(f"The word '{word}' has {x} characters.")
    
    dur = (.3 * x) / 4  # Adjusted duration
    
    # Add additional pause if word ends with a period
    if word.endswith('.'):
        dur += additional_pause_for_period

    print(f"Duration is: {dur}")
    
    durations.append(dur)


# Create video from images
clip = ImageSequenceClip(frames, durations=durations)

# Save the video    
clip.write_videofile("output.mp4", fps=24, codec="libx264")

# Remove generated frames
for frame in frames:
    os.remove(frame)

print("Video created!")

# Open the project folder
if platform.system() == "Windows":
    subprocess.run(["explorer", "."])
elif platform.system() == "Darwin":
    subprocess.run(["open", "."])
elif platform.system() == "Linux":
    subprocess.run(["xdg-open", "."])
else:
    print("Could not determine OS to open folder.")
