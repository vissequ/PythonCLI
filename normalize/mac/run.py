#LUFS target -12 dB

#!/usr/bin/env python3
import os
import time
import subprocess

def is_video_file(filename):
    """
    Checks if a filename ends with one of the common video file extensions.
    """
    video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.mpeg', '.mpg']
    return any(filename.lower().endswith(ext) for ext in video_extensions)

def process_video(input_path, output_path):
    """
    Processes the input video by copying the video stream and applying an audio filter chain:
      1. acompressor – applies dynamic range compression.
      2. alimiter   – limits the peaks (with a valid 'limit' value).
      3. loudnorm   – normalizes the integrated loudness to –12 LUFS.
    
    Adjust the filter parameters as needed.
    """
    # Note: The 'limit' parameter for alimiter must be between 0.0625 and 1.
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "copy",
        "-af", "acompressor=threshold=-24dB:ratio=4:attack=20:release=200,alimiter=limit=0.95,loudnorm=I=-12:TP=-2:LRA=11",
        "-y",  # Overwrite output files without asking.
        output_path
    ]
    
    print(f"Processing: {input_path}")
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Saved processed file to: {output_path}\n")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {input_path}: {e}\n")

def main():
    # Use the current working directory as the root.
    root_dir = os.getcwd()
    
    # Create an output folder named "output" + unix time.
    unix_time = int(time.time())
    output_folder = f"output{unix_time}"
    os.makedirs(output_folder, exist_ok=True)
    print(f"Output folder created: {output_folder}\n")
    
    # Walk through the directory tree.
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip the output folder to avoid reprocessing files.
        if output_folder in dirnames:
            dirnames.remove(output_folder)
        for filename in filenames:
            if is_video_file(filename):
                input_path = os.path.join(dirpath, filename)
                # Place the processed file in the output folder using the same filename.
                output_path = os.path.join(output_folder, filename)
                process_video(input_path, output_path)

if __name__ == "__main__":
    main()
