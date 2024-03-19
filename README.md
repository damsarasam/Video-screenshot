# Video Screenshot Extractor

Welcome to the Video Screenshot Extractor repository! This Python script automates the process of extracting screenshots from a video file at specified intervals using ffmpeg.

## Features

- **Screenshot Extraction**: Captures screenshots from a video file at regular intervals.
- **Customizable Parameters**: Users can specify the video path, output directory, and interval between screenshots.
- **Efficient Processing**: Utilizes ffmpeg for fast and efficient extraction of screenshots.
- **Convenient Visualization**: Provides a convenient way to extract visual data for analysis or visualization purposes.

## Usage

1. Set the path to the input video file (`video_path`).
2. Define the directory where screenshots will be saved (`output_directory`).
3. Specify the time interval between consecutive screenshots (`interval`).
4. Run the script to extract screenshots from the video file.

```python
python screenshot_extractor.py
```

## Requirements

- Python 3.x
- ffmpeg (Ensure ffmpeg is installed and accessible in your system PATH)

## Parameters

- `video_path`: Path to the input video file.
- `output_directory`: Directory where screenshots will be saved.
- `interval`: Time interval (in seconds) between consecutive screenshots.

## Example

```python
video_path = 'path/to/video.mp4'
output_directory = 'output/screenshots'
interval = 2  # Extract one screenshot every 2 seconds
```
