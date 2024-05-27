# Audio
"""Module providing a function to extract the audio from a video and export"""
# /usr/bin/env python3

import os
import pathlib
import datetime

from moviepy.editor import VideoFileClip
import speech_recognition as sr
from .terminal import ALERT, ERROR, INFORMATION, SAVED_IN, SUCCESS


PATH_DATA = pathlib.Path(__file__).parent.parent / "data"
PATH_VIDEOS = pathlib.Path(__file__).parent.parent / "data" / "videos"
PATH_AUDIOS = pathlib.Path(__file__).parent.parent / "data" / "audios"
PATH_TEXTS = pathlib.Path(__file__).parent.parent / "data" / "texts"


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
        wav_file = f"{PATH_AUDIOS}/{audio}"

        # Load the video clip
        video_clip = VideoFileClip(mp4_file)

        # Extract the audio from the video clip
        audio_clip = video_clip.audio

        # Write the audio to a separate file
        audio_clip.write_audiofile(os.path.join(PATH_AUDIOS, wav_file))
        # audio_clip.write_audiofile(os.path.join("audios", wav_file))

        # Close the video and audio clips
        audio_clip.close()
        video_clip.close()

        print(f"{SUCCESS} Audio extraction from {video} successful!")

        saved_in = f"[src/data/audios/{audio}]"
        print(f"{SAVED_IN} The extracted audio was saved in {saved_in}")

    except SuccessError as e:
        print(f"\n{ERROR} An error occurred while extracting audio: {e}")


def transcribe_audio_to_text(audio: str) -> str:
    '''
    Transcribe a audio file to an text file and saves it to the specified
    directory.

    Args:
    audio (str): The name of the audio to transcribe for a text file.

    Returns:
    None: The function  return a text file and a success or error
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

        if not os.path.isdir(PATH_TEXTS):
            os.chdir(PATH_DATA)
            os.mkdir("texts")

        r = sr.Recognizer()

        wav_file = f"{PATH_AUDIOS}/{audio}"

        # Open the audio file
        with sr.AudioFile(wav_file) as source:
            # Read the audio from the file
            audio = r.record(source)

        # Transcribe the audio
        filename = os.path.basename(wav_file)
        print(f"{INFORMATION} Initializing the transcription of [{filename}].")

        transcribed_text = r.recognize_google(audio, language='pt-BR')

        # Opens a file in writing mode and saves the trascribed text inside.
        basename = os.path.splitext(filename)

        # Get the current date and current hour
        date = datetime.datetime.now()
        formated_hour = f"{date.hour}-{date.minute}-{date.second}"
        formated_date = f"{date.year}-{date.month:02d}-{date.day:02d}"

        # Create the format  for the output directory and file name
        output_file = f"{basename[0]}-{formated_date}_{formated_hour}.txt"
        save_dir = f"{PATH_TEXTS}/{output_file}"

        # Open a file in write mode
        with open(save_dir, 'w', encoding="utf-8") as f:
            # Writes the transcribed_text content in the file
            f.write(f"{transcribed_text}")

        # Close the opened file
        f.close()

        # Show message on terminal for a success execution
        print(f"{SUCCESS} Audio extraction from [{filename}] successful!")

        saved_in = f"[src/data/texts/{output_file}]"
        print(f"{SAVED_IN} The transcribed text was saved in {saved_in}")

        # Show a message with a example of trascribed text
        print("\n### EXAMPLE TEXT ###\n" + transcribed_text)

    # Show a message if ocurred a error
    except sr.UnknownValueError:
        print(f"{ALERT} Unable to understand the audio.")
    except SuccessError as e:
        print(f"\n{ERROR} An error occurred while transcribe the audio: {e}")
