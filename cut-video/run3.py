from moviepy.editor import VideoFileClip

def cut_video_into_two_hour_sections(input_file):
    clip = VideoFileClip(input_file)
    total_duration = int(clip.duration)  # Convert to integer
    two_hour_duration = 2 * 60 * 60  # 2 hours in seconds
    
    # Calculate the number of two-hour sections
    num_sections = total_duration // two_hour_duration
    remainder_duration = total_duration % two_hour_duration
    
    for i in range(num_sections):
        start_time = i * two_hour_duration
        end_time = (i + 1) * two_hour_duration
        sub_clip = clip.subclip(start_time, end_time)
        sub_clip.write_videofile(f"{input_file}_part_{i+1}.mp4", codec="libx264", audio_codec="aac")
    
    # Handle the remainder duration
    if remainder_duration > 0:
        start_time = num_sections * two_hour_duration
        sub_clip = clip.subclip(start_time, total_duration)
        sub_clip.write_videofile(f"{input_file}_part_{num_sections+1}.mp4", codec="libx264", audio_codec="aac")

# Example usage:
input_file = "NTV Russia Sep 11 2001 8_00am - 3_20pm.m4v"
cut_video_into_two_hour_sections(input_file)
