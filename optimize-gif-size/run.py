import os
from PIL import Image, ImageSequence

def optimize_gif(input_path, output_path, max_colors=64, frame_skip=2):
    # Open the GIF
    gif = Image.open(input_path)
    
    # Create a list to store optimized frames
    frames = []
    
    # Loop through each frame in the original GIF
    for i, frame in enumerate(ImageSequence.Iterator(gif)):
        # Only keep every 'frame_skip' frame to reduce the frame count
        if i % frame_skip == 0:
            # Convert to P mode (palette-based) and reduce the number of colors
            optimized_frame = frame.convert("P", palette=Image.ADAPTIVE, colors=max_colors)
            frames.append(optimized_frame)
    
    # Save the optimized GIF with compression options
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=gif.info['duration'] * frame_skip,  # Adjust duration to keep original speed
        loop=gif.info.get('loop', 0)
    )
    print(f"Optimized GIF saved as {output_path}")

def process_all_gifs_in_root(root_folder):
    # Create output folder if it doesn't exist
    output_folder = os.path.join(root_folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Process each GIF in the root folder
    for filename in os.listdir(root_folder):
        if filename.lower().endswith(".gif"):
            input_path = os.path.join(root_folder, filename)
            output_path = os.path.join(output_folder, f"optimized_{filename}")
            print(f"Optimizing {filename}...")
            optimize_gif(input_path, output_path)
    print("All GIFs have been processed.")

# Example usage
root_folder = "."  # Change to your folder path if not the current directory
process_all_gifs_in_root(root_folder)
