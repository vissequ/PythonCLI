import os
from moviepy.editor import *

def find_wav_file():
    # Look for a .wav file in the root directory
    for file in os.listdir('.'):
        if file.endswith('.wav'):
            return file
    return None

def wav_to_mp4():
    wav_file = find_wav_file()
    
    if not wav_file:
        print("No .wav file found in the root directory.")
        return
    
    # Get the base name (without extension) from the wav file
    output_file = os.path.splitext(wav_file)[0] + ".mp4"
    
    # Load the image (1920x1080 resolution)
    image = ImageClip("template.jpg").set_duration(0)  # Dummy duration

    # Load the audio file (wav)
    audio = AudioFileClip(wav_file)

    # Set the correct duration of the image to match the audio
    image = image.set_duration(audio.duration)

    # Set the audio for the video
    image = image.set_audio(audio)

    # Write the output to an mp4 file with the same name as the wav file
    image.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")

# Example usage
wav_to_mp4()
