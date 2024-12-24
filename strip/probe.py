import subprocess
import json
import os
import sys

def fetch_metadata(file_path):
    cmd = [
        'ffprobe',
        '-loglevel', 'quiet',
        '-print_format', 'json',
        '-show_format',
        '-show_streams',
        file_path
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return json.loads(result.stdout)

def determine_editor(metadata):
    software_used = metadata.get('format', {}).get('tags', {}).get('encoder', 'Unknown')
    return software_used

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    input_folder_path = os.path.join(script_dir, 'input')

    if not os.path.exists(input_folder_path):
        print(f"'input' folder does not exist in {script_dir}")
        sys.exit(1)

    for file in os.listdir(input_folder_path):
        if file.endswith(".mov"):
            mov_file = os.path.join(input_folder_path, file)
            metadata = fetch_metadata(mov_file)
            software = determine_editor(metadata)
            print(f"For file '{file}': Video editing software (based on encoder tag): {software}")
