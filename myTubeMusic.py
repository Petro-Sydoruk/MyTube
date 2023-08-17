#pip install pytube moviepy mutagen pillow


import os
import requests
from pytube import YouTube
from moviepy.editor import AudioFileClip
from mutagen.id3 import ID3, APIC, TPE1
from PIL import Image
from io import BytesIO

def download_music_with_metadata(url, output_path):
    try:
        # Download the YouTube video using pytube
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        print(f"Downloading: {video.title}...")
        video_stream_file = stream.download(output_path)
        print("Download complete!")

        # Get the thumbnail image
        thumbnail_url = video.thumbnail_url
        response = requests.get(thumbnail_url)
        thumbnail_image = Image.open(BytesIO(response.content))

        # Save the thumbnail image in the output directory
        thumbnail_path = os.path.join(output_path, f"{video.title}.jpg")
        thumbnail_image.save(thumbnail_path)

        # Convert the downloaded video to MP3 format
        mp3_file = os.path.join(output_path, f"{video.title}.mp3")
        audio_clip = AudioFileClip(video_stream_file)
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()

        # Remove the original video file
        os.remove(video_stream_file)

        # Set cover art and author
        with open(thumbnail_path, 'rb') as thumbnail_file:
            audio = ID3(mp3_file)
            audio.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=thumbnail_file.read()))

        # Add the author/artist information to metadata
        audio.add(TPE1(text=video.author))

        # Save the metadata
        audio.save(v2_version=3)

        # Remove the thumbnail image after embedding
        os.remove(thumbnail_path)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube URL of the music video: ")

    #output_directory = r"C:\Users\petro\Documents\MEGAsync\MyTube" # destination directory for the output
    output_directory = r"C:\Users\p3--\Music\MyTube"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    download_music_with_metadata(url, output_directory)
