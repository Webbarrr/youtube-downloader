from pytube import YouTube
from sys import argv
from pathlib import Path

link = argv[1] # first argument from the command line
yt = YouTube(link)

print(f"Downloading '{yt.title}' now...")

yd = yt.streams.get_highest_resolution()

if len(argv) > 2:
    folder = argv[2]
else:
    folder = str(Path.home() / "Downloads")

yd.download(folder)

print("Finished downloading")
print(f"Downloaded in '{folder}'")