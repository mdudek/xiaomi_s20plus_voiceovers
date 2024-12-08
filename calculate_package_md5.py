import hashlib

with open("./dist/cs_google_tts.tar.gz", "rb") as f:
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)

print(file_hash.hexdigest())  # to get a printable str instead of bytes
