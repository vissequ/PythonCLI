import subprocess
import os
import sys

def remove_metadata(input_file, output_file):
    try:
        # Construct the ffmpeg command
        cmd = [
            'ffmpeg',
            '-i', input_file,
            '-map', '0',
            '-c', 'copy',
            '-map_metadata', '-1',
            '-movflags', 'use_metadata_tags',
            output_file
        ]

        # Execute the command
        subprocess.run(cmd, check=True)
        
        print(f"Metadata removed. New file saved as {output_file}")
        
    except subprocess.CalledProcessError:
        print("Error during processing. Ensure ffmpeg is installed and available in your PATH.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    input_folder_path = os.path.join(script_dir, 'input')

    if not os.path.exists(input_folder_path):
        print(f"'input' folder does not exist in {script_dir}")
        sys.exit(1)

    for file in os.listdir(input_folder_path):
        if file.endswith(".mov"):
            input_file = os.path.join(input_folder_path, file)
            output_file_name = os.path.splitext(file)[0] + "_9999.mov"
            output_file = os.path.join(script_dir, output_file_name)
            remove_metadata(input_file, output_file)
