#Very simple downlaod of video files from URL (HTML is fine)

import os
import yt_dlp

def download_video(url, output_folder="videos"):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download the best quality available
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Set the output template for the file
        'noplaylist': True,  # Avoid downloading playlists
        'quiet': False,  # Show download progress in terminal
    }
    
    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f"Error downloading video: {e}")

if __name__ == "__main__":
    url = input("Enter the video URL: ")
    download_video(url)
