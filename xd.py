from yt_dlp import YoutubeDL

url = "https://youtu.be/Regpv0xU3ZQ?si=za_rUTGJo6_YvSHA"
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])