from moviepy.editor import VideoFileClip

def cut_video_into_one_minute_segments(input_file):
    clip = VideoFileClip(input_file)
    total_duration = int(clip.duration)  # Convert to integer
    one_minute_duration = 60  # 1 minute in seconds
    
    # Calculate the number of one-minute segments
    num_segments = 2
    segment_duration = one_minute_duration
    
    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = (i + 1) * segment_duration
        sub_clip = clip.subclip(start_time, end_time)
        sub_clip.write_videofile(f"{input_file}_segment_{i+1}.mp4", codec="libx264", audio_codec="aac")

# Example usage:
input_file = "Texas TCN 09 11 2001 8_00am - 4_00pm.mov"
cut_video_into_one_minute_segments(input_file)
