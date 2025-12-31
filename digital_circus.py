import yt_dlp

# 1. Define your playlist URL and download path
playlist_url = "https://www.youtube.com/playlist?list=PLHovnlOusNLgvAbnxluXCVB3KLj8e4QB-"  # e.g., 'www.youtube.com...'
ydl_opts = {
    "format": "bestvideo+bestaudio/best",  # Downloads highest quality
    "outtmpl": "%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",  # Organizes into folders
    "noplaylist": False,  # Ensures it downloads the whole playlist
    "merge_output_format": "mp4",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
