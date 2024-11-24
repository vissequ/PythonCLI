import os
import subprocess

def convert_to_mp4(file_name):
    # Get the file's base name (without extension)
    base_name = os.path.splitext(file_name)[0]
    
    # Define the output filename
    output_name = base_name + ".mp4"
    
    # Use ffmpeg to convert
    command = ['ffmpeg', '-i', file_name, '-c:v', 'libx264', '-c:a', 'aac', output_name]
    subprocess.run(command)

def main(directory):
    # Get all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".webm") or file.endswith(".ogv") or file.endswith(".vob") or file.endswith(".VOB"):
                file_path = os.path.join(root, file)
                print(f"Converting {file_path} to MP4...")
                convert_to_mp4(file_path)
                print(f"Converted {file_path} to MP4 successfully!")

if __name__ == "__main__":
    # Directory containing the files. You can change this.
    dir_path = "toconvert"
    main(dir_path)
