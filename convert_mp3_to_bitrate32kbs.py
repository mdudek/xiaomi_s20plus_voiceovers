import os
import subprocess

def convert_mp3_bitrate(input_folder, output_folder, bitrate="32k"):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get list of MP3 files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".mp3"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            # FFmpeg command to convert bitrate
            command = [
                "ffmpeg", "-i", input_path, "-b:a", bitrate, output_path
            ]

            print(f"Converting {file_name} to {bitrate}...")
            subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(f"Saved: {output_path}")

if __name__ == "__main__":
    # Define input and output folder paths
    input_folder = "mp3"
    output_folder = "mp3_32kbs"

    # Ensure the input and output folders exist
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist. Please create it and add MP3 files.")
    else:
        convert_mp3_bitrate(input_folder, output_folder)
