import os
import subprocess

# Set the path to the video file
video_path = 'Downloads/4e65b7c7-f311-459a-87e7-50760b50a210.MP4'

# Set the directory where screenshots will be saved
output_directory =r'/Users/damsara/Downloads/Video screenshot'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# The interval for screenshots (in seconds)
interval = 2

# Build the ffmpeg command
command = [
    'ffmpeg',
    '-i', video_path,  # Input file
    '-vf', f'fps=1/{interval}',  # Set the frame rate for screenshots (1 frame every `interval` seconds)
    '-q:v', '2',  # Output quality (lower number is higher quality)
    os.path.join(output_directory, 'screenshot_%04d.jpg')  # Output file pattern
]

# Run the command
subprocess.run(command)

print(f'Screenshots saved to {output_directory}')
