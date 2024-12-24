import os
from moviepy.editor import VideoFileClip

# Define the root directory (current directory)
root_dir = "."

# Iterate over each file in the root directory
for filename in os.listdir(root_dir):
    # Check if the file is an MP4 file
    if filename.lower().endswith('.mp4'):
        # Define the output filename with an MP3 extension
        mp3_filename = os.path.splitext(filename)[0] + '.mp3'
        
        # Load the video file
        try:
            video = VideoFileClip(os.path.join(root_dir, filename))
            
            # Extract the audio and save as MP3
            video.audio.write_audiofile(os.path.join(root_dir, mp3_filename))
            
            print(f"Converted {filename} to {mp3_filename}")
            
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
