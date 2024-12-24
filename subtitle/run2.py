import os
import math
import speech_recognition as sr
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def get_duration_in_seconds(audio_segment):
    return len(audio_segment) / 1000  # Duration in seconds

def transcribe_chunk_with_timestamps(recognizer, audio_chunk, chunk_start_time):
    with sr.AudioFile(audio_chunk) as source:
        audio_data = recognizer.record(source)
    
    try:
        # Transcribe chunk
        text = recognizer.recognize_google(audio_data)
        timestamp = convert_seconds_to_hhmmss(chunk_start_time)
        return f"[{timestamp}] {text}\n"
    except sr.UnknownValueError:
        return f"[{convert_seconds_to_hhmmss(chunk_start_time)}] [Unclear audio]\n"
    except sr.RequestError as e:
        return f"[{convert_seconds_to_hhmmss(chunk_start_time)}] [Error: {e}]\n"

def convert_seconds_to_hhmmss(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def transcribe_video_to_text_with_timestamps(video_path):
    # Step 1: Extract audio from video
    video = VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path)
    
    # Step 2: Convert to WAV format
    audio = AudioSegment.from_file(audio_path)
    
    # Step 3: Initialize recognizer and break audio into chunks
    recognizer = sr.Recognizer()
    chunk_length_ms = 30000  # 30 seconds per chunk
    chunks = math.ceil(get_duration_in_seconds(audio) / (chunk_length_ms / 1000))

    transcript_filename = f"{os.path.splitext(video_path)[0]}_transcript.txt"
    with open(transcript_filename, "w") as transcript_file:
        for i in range(chunks):
            chunk_start_time = i * (chunk_length_ms / 1000)  # in seconds
            chunk_end_time = (i + 1) * (chunk_length_ms / 1000)  # in seconds
            print(f"Processing chunk {i + 1}/{chunks} (from {chunk_start_time}s to {chunk_end_time}s)")
            
            # Extract chunk and export it to temporary file
            chunk_audio = audio[chunk_start_time * 1000:chunk_end_time * 1000]
            chunk_filename = f"temp_chunk_{i}.wav"
            chunk_audio.export(chunk_filename, format="wav")
            
            # Transcribe the chunk with timestamp
            transcribed_text = transcribe_chunk_with_timestamps(recognizer, chunk_filename, chunk_start_time)
            transcript_file.write(transcribed_text)
            
            # Cleanup the temporary chunk file
            os.remove(chunk_filename)
    
    # Step 4: Cleanup
    os.remove(audio_path)
    print(f"Transcription with timestamps saved to {transcript_filename}")

if __name__ == "__main__":
    # Look for a video file in the root folder
    root_dir = os.getcwd()
    video_extensions = ('.mp4', '.m4v', '.avi', '.mov', '.mkv')  # Add more if needed

    for file_name in os.listdir(root_dir):
        if file_name.endswith(video_extensions):
            print(f"Found video file: {file_name}")
            transcribe_video_to_text_with_timestamps(file_name)
            break
    else:
        print("No video files found in the root folder.")
