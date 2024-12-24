import os
import speech_recognition as sr
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def transcribe_video_to_text(video_path):
    # Step 1: Extract audio from video
    video = VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path)

    # Step 2: Convert audio to WAV format using PyDub if necessary
    audio = AudioSegment.from_file(audio_path)
    audio.export(audio_path, format="wav")

    # Step 3: Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Step 4: Load audio file
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    # Step 5: Transcribe audio to text
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcription successful.")
    except sr.UnknownValueError:
        text = "Audio not clear enough to transcribe."
    except sr.RequestError as e:
        text = f"Could not request results from the service; {e}"

    # Step 6: Save transcription to a time-stamped text file
    transcript_filename = f"{os.path.splitext(video_path)[0]}_transcript.txt"
    with open(transcript_filename, "w") as transcript_file:
        transcript_file.write(text)

    # Step 7: Cleanup
    os.remove(audio_path)
    
    print(f"Transcription saved to {transcript_filename}")

if __name__ == "__main__":
    # Look for a video file in the root folder
    root_dir = os.getcwd()
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')  # Add more if needed

    for file_name in os.listdir(root_dir):
        if file_name.endswith(video_extensions):
            print(f"Found video file: {file_name}")
            transcribe_video_to_text(file_name)
            break
    else:
        print("No video files found in the root folder.")
