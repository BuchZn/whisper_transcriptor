# Whisper Transcriptor

A small Tkinter desktop app that lets you pick an `.mp4` video, extracts its
audio track to `.mp3`, and (once transcription is wired up) transcribes it
with [OpenAI Whisper](https://github.com/openai/whisper).

> **Status:** The file picker and mp4 → mp3 audio extraction are working.
> The actual Whisper transcription step (`transcribe()` in
> [transcriptor.py](transcriptor.py)) is not implemented yet, so running the
> app today will extract audio but won't produce a transcript.

## Requirements

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/download.html) installed and available on your
  `PATH` (required by both `moviepy` and `whisper`)

## Setup

1. Clone the repository and move into it:

   ```bash
   git clone <this-repo-url>
   cd whisper_transcriptor
   ```

2. (Recommended) create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install the Python dependencies:

   ```bash
   pip install -U openai-whisper moviepy
   ```

   `tkinter` ships with most standard Python installations, so no separate
   install is usually needed. On some Linux distributions you may need to
   install it separately, e.g. `sudo apt install python3-tk`.

4. Make sure `ffmpeg` is installed:

   ```bash
   ffmpeg -version
   ```

   If that fails, install it via your OS package manager (`choco install
   ffmpeg`, `brew install ffmpeg`, `sudo apt install ffmpeg`, etc.) or
   download a build from the ffmpeg website and add it to your `PATH`.

## Usage

Run the app:

```bash
python transcriptor.py
```

1. A small window titled **Whisper Transcriptor** opens.
2. Click **Open a File** and choose an `.mp4` video.
3. The app extracts the video's audio track and saves it as a timestamped
   `.mp3` file in the current working directory (e.g.
   `2026-08-25 14_30_00.mp3`).
4. Once transcription is implemented, the resulting text will be produced
   from that audio file using Whisper.

## Todo

- [ ] Make options for output filename, Whisper model, and output file format

## License

Licensed under the GNU General Public License v3.0 — see [LICENSE](LICENSE)
for details.
