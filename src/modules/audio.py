# Video to Audio
"""Module providing a function to extract the audio from a video and export"""
# /usr/bin/env python3

import os
import pathlib

from moviepy.editor import VideoFileClip
from .terminal import ALERT, BOLD, ERROR, INFORMATION, SUCCESS


PATH_DATA = pathlib.Path(__file__).parent.parent / "data"
PATH_VIDEOS = pathlib.Path(__file__).parent.parent / "data" / "videos"
PATH_AUDIOS = pathlib.Path(__file__).parent.parent / "data" / "audios"


# Voltar 2 diretórios e entrar na pasta data
print(f"{BOLD}######################################")
print(f"{BOLD}   ALL VIDEOS ON DIRECTORY VIDEOS")

FILE_NUM = 0
for item in PATH_VIDEOS.iterdir():
    if item.is_file():
        FILE_NUM += 1
        print(f"{BOLD} {FILE_NUM} - {item.name}")

print(f"{BOLD}######################################\n\n")


def extract_audio(video: str, audio: str) -> None:
    '''
    Converts a video file to an MP3 audio file and saves it to the specified
    directory.

    Args:
    video (str): The name of the video file to be converted.
    audio (str): The name of the resulting MP3 audio file.

    Returns:
    None: The function does not return any object, just a success or error
     message on console.
    '''
    class SuccessError(Exception):
        """Exception raised for errors in the success of the function."""

        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    try:
        # Verify if directory exists and if not create the directory
        if not os.path.isdir(PATH_AUDIOS):
            os.chdir(PATH_DATA)
            os.mkdir("audios")

        if not os.path.isdir(PATH_VIDEOS):
            os.chdir(PATH_DATA)
            os.mkdir("videos")

        # Define the input video file and output audio file
        mp4_file = f"{PATH_VIDEOS}/{video}"
        mp3_file = f"{PATH_AUDIOS}/{audio}"

        # Load the video clip
        video_clip = VideoFileClip(mp4_file)

        # Extract the audio from the video clip
        audio_clip = video_clip.audio

        # Write the audio to a separate file
        audio_clip.write_audiofile(os.path.join(PATH_AUDIOS, mp3_file))
        # audio_clip.write_audiofile(os.path.join("audios", mp3_file))

        # Close the video and audio clips
        audio_clip.close()
        video_clip.close()

        print(f"{ALERT} Audio extraction from {video} successful!")
        print(f"{INFORMATION} Audio extraction from {video} successful!")
        print(f"{ERROR} Audio extraction from {video} successful!")
        print(f"{SUCCESS} Audio extraction from {video} successful!")
    except SuccessError as e:
        print(f"\n{ERROR} An error occurred while extracting audio: {e}")
