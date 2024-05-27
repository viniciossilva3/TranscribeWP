<div align="center">
<img  alt="Logo" src="https://github.com/viniciossilva3/TranscribeWP/assets/56976328/508b2d89-cfd4-4a27-878a-0b4911b0bde2" width="800">
</div>

<h1 align="center">TranscribeWP</h1>

## Documentation

- [EN - 🇺🇸](/docs/readme/README-EN.md)
- [ES - 🇪🇸](/docs/readme/README-ES.md)
- [PT-BR - 🇧🇷](/docs/readme/README-PT-BR.md)

## Description

This is a Python project developed to download videos, extract audio from videos, transcribe the text, proofread and modify the text, search for an image corresponding to the text theme and publish the content on a WordPress blog.

## Features

- [x] **Download a Youtube video:** Use the `download_video(url)` function to download a youtube video.
- [x] **Download a Youtube playlist:** Use the `download_playlist(url)` function to download a youtube playlist. (Waiting for pytube library update to make it work)
- [x] **Download a Youtube video:** Use the `download_channel(url)` function to download a youtube channel video.
- [x] **Extract audio from video:** Use the `extract_audio(video, audio)` function to extract audio from a video and save it to an audio file.
- [x] **Transcribe text:** Use the `transcribe_audio_to_text(audio)` function to transcribe the audio to text.
- [ ] **Proofread and modify text:** Implement the functions needed to proofread and modify the text according to your needs.
- [ ] **Search for image:** Implement the `search_image(theme)` function to find an image corresponding to the text theme.
- [ ] **Publish to WordPress blog:** Use the `publish_to_blog(text, image)` function to publish the content to your WordPress blog.

## Requirements

- Python 3.x
- Packages:
  - moviepy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/viniciossilva3/TranscribeWP.git
   ```
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Import the necessary functions into your Python script:

   ```python
   from .modules.audio import extract_audio
   from .modules.video import download_video
   from .modules.video import download_playlist
   from .modules.video import download_channel
   #from .modules.transcribe_audio_to_text import transcribe_audio_to_text
   #from .modules.proofread_text import proofread_text
   #from .modules.search_image import search_image
   #from .modules.publish_to_blog import publish_to_blog
   ```

2. Use the functions as needed, for example:

   ```python
   # Extract audio from a video
   audio = extract_audio("video.mp4", "audio.mp3")

   # Transcribe the audio to text
   transcribed_text = transcribe_audio_to_text(audio)

   # Proofread and modify the text
   proofread_text = proofread_text(transcribed_text)

   # Search for an image corresponding to the text theme
   image = search_image("theme")

   # Publish the text and image to the WordPress blog
   publish_to_blog(proofread_text, image)
   ```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
