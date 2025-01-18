import os
import subprocess
import json

def get_video_dimensions(input_file):
    # Use ffprobe to get video stream information in JSON format
    cmd = [
        'ffprobe', '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height',
        '-of', 'json', input_file
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Parse the JSON output
    try:
        probe = json.loads(result.stdout)
        width = probe['streams'][0]['width']
        height = probe['streams'][0]['height']
        return width, height
    except (KeyError, IndexError, json.JSONDecodeError):
        raise ValueError(f"Failed to extract dimensions from the video: {input_file}")

def resize_video(input_file, output_file, percent):
    try:
        width, height = get_video_dimensions(input_file)
    except ValueError as e:
        print(e)
        return

    # Calculate new dimensions, ensuring they are divisible by 2
    new_width = int(width * percent / 100) // 2 * 2
    new_height = int(height * percent / 100) // 2 * 2

    # Resize the video
    cmd = [
        'ffmpeg', '-i', input_file,
        '-vf', f"scale={new_width}:{new_height}",
        '-c:a', 'copy',
        output_file
    ]
    subprocess.run(cmd)

def resize_videos_in_directory(percent):
    # Get all mp4 files in the current directory
    files = [f for f in os.listdir('.') if f.endswith('.mp4')]
    
    for file in files:
        output_file = f"resized_{file}"
        print(f"Resizing {file} to {percent}%...")
        resize_video(file, output_file, percent)
        print(f"Saved resized video as {output_file}")

def main():
    while True:
        try:
            percent = int(input("Enter resize percentage (1-400%): "))
            if 1 <= percent <= 400:
                break
            else:
                print("Please enter a value between 1 and 400.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 400.")

    resize_videos_in_directory(percent)

if __name__ == "__main__":
    main()
