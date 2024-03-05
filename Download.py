from pytube import YouTube
import os

os.system('cls' if os.name == 'nt' else 'clear')


print("\n    \033[31m██████╗  █████╗ ██████╗ ██╗  ██╗ \033[0m  \033[34m██████╗ ██╗       █████╗   ██████╗██╗  ██╗ \033[0m ")
print("    \033[31m██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝ \033[0m  \033[34m██╔══██╗██║      ██╔══██╗ ██╔════╝██║ ██╔╝ \033[0m ")
print("    \033[31m██║  ██║███████║██████╔╝█████╔╝  \033[0m  \033[34m██████╔╝██║      ███████║ ██║     █████╔╝  \033[0m ")
print("    \033[31m██║  ██║██╔══██║██╔══██╗██╔═██╗  \033[0m  \033[34m██╔══██╗██║      ██╔══██║ ██║     ██╔═██╗  \033[0m ")
print("    \033[31m██████╔╝██║  ██║██║  ██║██║  ██╗ \033[0m  \033[34m██████╔╝███████╗ ██║  ██║ ╚██████╗██║  ██╗ \033[0m ")
print("    \033[31m╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ \033[0m  \033[34m╚═════╝ ╚══════╝ ╚═╝  ╚═╝  ╚═════╝╚═╝  ╚═╝ \033[0m\n ")

def download_video(video_url, output_path="."):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()

        print(f"\033[34mDownloading:\033[0m {yt.title}")
        video.download(output_path)
        print("\033[34mDownload complete!\033[0m")

    except Exception as e:
        print(f"\033[91mError: \033[34mYOUR URL IS WRON\033[0m")

if __name__ == "__main__":
    video_url = input("\033[91m\nEnter the YouTube video URL:\033[0m")
    output_path = input("\033[91m\nEnter the output path (default is current directory):\033[0m  ") or "."

    download_video(video_url, output_path)
