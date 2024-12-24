import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_webm(input_path, output_path):
    """Converts mp4 file to webm using moviepy."""
    with VideoFileClip(input_path) as video:
        video.write_videofile(output_path, codec='libvpx')

def find_and_convert_mp4_to_webm(root_folder):
    """Searches for mp4 files in the root folder and converts them to webm."""
    for filename in os.listdir(root_folder):
        if filename.endswith('.mp4'):
            input_path = os.path.join(root_folder, filename)
            output_path = os.path.join(root_folder, filename.replace('.mp4', '.webm'))
            
            print(f"Converting {filename} to webm...")
            try:
                convert_mp4_to_webm(input_path, output_path)
                print(f"Conversion completed: {output_path}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    root_folder = os.getcwd()  # Use current working directory as root
    find_and_convert_mp4_to_webm(root_folder)
