import pytube
import os

pytube.innertube._default_clients["ANDROID"] = pytube.innertube._default_clients["WEB"]

yt = pytube.YouTube("https://youtu.be/Regpv0xU3ZQ?si=TTf_c-DyLmUM--Mh")

video = yt.streams.filter(only_audio=True).first()

dest = "D:\Music"

out_file = video.download(output_path=dest)

base, ext = os.path.splitext(out_file)
new_file = base + ".wav"
os.rename(out_file,new_file)

print("Download")