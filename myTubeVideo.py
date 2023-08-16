import os
from pytube import YouTube

def download_video(url, output_path):
    try:
        # Download the YouTube video using pytube
        video = YouTube(url)
        stream = video.streams.filter(file_extension='mp4', only_video=True).first()
        print(f"Downloading video: {video.title}...")
        video_stream_file = stream.download(output_path)
        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube URL of the video: ")

    output_directory = r"C:\Users\petro\Documents\MEGAsync\MyTube"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    download_video(url, output_directory)
