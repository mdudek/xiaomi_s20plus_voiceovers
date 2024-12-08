import os
import tarfile
import gzip

def pack_folder_to_targz_no_compression(input_folder, output_file):
    """
    Packs all files in the input folder into a .tar.gz archive with no compression.

    :param input_folder: Path to the folder containing files to pack.
    :param output_file: Path to the output .tar.gz file.
    """
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist.")
        return

    # Open a gzip file with compression level 0
    with gzip.open(output_file, "wb", compresslevel=0) as gz_file:
        with tarfile.open(fileobj=gz_file, mode="w") as tar:
            for root, _, files in os.walk(input_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=input_folder)
                    print(f"Adding {file_path} as {arcname}...")
                    tar.add(file_path, arcname=arcname)
    print(f"Files packed into {output_file} with no compression.")

if __name__ == "__main__":
    # Define input folder and output .tar.gz file
    input_folder = "mp3_32kbs"
    output_file = "dist/cs_google_tts.tar.gz"

    pack_folder_to_targz_no_compression(input_folder, output_file)
