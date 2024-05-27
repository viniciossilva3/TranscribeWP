# Video
"""Module providing a function to download a video from Youtube"""
# /usr/bin/env python3

import os
import pathlib
from pytube import Channel, Playlist, YouTube
from .terminal import ERROR, INFORMATION, SUCCESS

PATH_DATA = pathlib.Path(__file__).parent.parent / "data"
PATH_VIDEOS = pathlib.Path(__file__).parent.parent / "data" / "videos"


def download_video(url: str) -> None:
    """
    Download a Youtube video and saves on the specified directory.

    Args:
    url (str): The url from a Youtube video to download.

    Returns:
    None: The function does not return any object, just a success or error
     message on console.
    """
    class SuccessError(Exception):
        """Exception raised for errors in the success of the function."""

        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    try:
        # Verify if directory exists and if not create the directory
        if not os.path.isdir(PATH_VIDEOS):
            os.chdir(PATH_DATA)
            os.mkdir("videos")

        youtube_data = YouTube(url)

        video = youtube_data.streams.first()

        print(f"{INFORMATION} Downloading {video.title}...")

        video.download(PATH_VIDEOS)

        print(f"{SUCCESS} The  video {video.title} has been " +
              "downloaded successfully!")

    except SuccessError as e:
        print(f"\n{ERROR} An error occurred while downloading the video: {e}")


def download_playlist(url: str) -> None:
    """
    Download a Youtube Playlist and saves on the specified directory.

    Args:
    url (str): The url from a Youtube Playlist to download.

    Returns:
    None: The function does not return any object, just a success or error
     message on console.
    """
    class SuccessError(Exception):
        """Exception raised for errors in the success of the function."""

        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    try:
        # Verify if directory exists and if not create the directory
        if not os.path.isdir(PATH_VIDEOS):
            os.chdir(PATH_DATA)
            os.mkdir("videos")

        channel_data = Playlist(url)

        for video in channel_data.videos:
            print(f"{INFORMATION} Downloading {video.title}...")

            video.streams.first().download(PATH_VIDEOS)

            print(f"{SUCCESS} The  video {video.title} " +
                  "has been downloaded successfully!")

    except SuccessError as e:
        print("\n")
        print(f"{ERROR} An error occurred while downloading the Playlist: {e}")


def download_channel(url: str) -> None:
    """
    Download a Youtube Channel and saves on the specified directory.

    Args:
    url (str): The url from a Youtube Channel to download.

    Returns:
    None: The function does not return any object, just a success or error
     message on console.
    """
    class SuccessError(Exception):
        """Exception raised for errors in the success of the function."""

        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    try:
        # Verify if directory exists and if not create the directory
        if not os.path.isdir(PATH_VIDEOS):
            os.chdir(PATH_DATA)
            os.mkdir("videos")

        channel_data = Channel(url)

        for video in channel_data.videos:
            print(f"{INFORMATION} Downloading {video.title}...")

            video.streams.first().download(PATH_VIDEOS)

            print(f"{SUCCESS} The  video {video.title} " +
                  "has been downloaded successfully!")

    except SuccessError as e:
        print("\n")
        print(f"{ERROR} Error occurred while downloading Channel videos: {e}")
