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
    
    # Create a black screen image (1080p resolution)
    black_screen = ColorClip(size=(1920, 1080), color=(0, 0, 0), duration=0)  # Dummy duration

    # Load the audio file (wav)
    audio = AudioFileClip(wav_file)

    # Set the correct duration of the black screen to match the audio
    black_screen = black_screen.set_duration(audio.duration)

    # Set the audio for the video
    black_screen = black_screen.set_audio(audio)

    # Write the output to an mp4 file with the same name as the wav file
    black_screen.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")

# Example usage
wav_to_mp4()
