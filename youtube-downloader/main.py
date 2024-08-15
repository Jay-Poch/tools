import requests
import os
import pytubefix # type: ignore
import colorama
header = {"Accept": "application/json", "Content-Type": "application/json"}
parameters = {}
def download(url: str, type: bool, name: str, quality: int = 720): 
    """
    Downloads a file from the given URL using the Cobalt API.

    Args:
        url (str): The URL of the file to download.
        type (bool): A flag indicating the type of download. True for audio, False for video.
        name (str): The name of the file to save the downloaded file as.
        quality (int, optional): The quality of the video to download. Defaults to 720.
    Returns:
        dict: The JSON response from the Cobalt API.

    Raises:
        requests.exceptions.RequestException: If there is an error making the request.

    """

    parameters["url"] = url
    parameters["isAudioOnly"] = type
    parameters["vQuality"] = quality
    try:
        response = requests.post("https://api.cobalt.tools/api/json", headers=header, json=parameters, timeout=2)
    except:
        response = requests.post("https://api.cobalt.tools/api/json", headers=header, json=parameters, timeout=2)
    file = response.json()
    if type == False:
        os.system(f"curl -L '{file['url']}' -o '{name}.mp4'")
    else:
        os.system(f"curl -L '{file['url']}' -o '{name}.mp3'")

def playlist_download(url: str, type: bool):
    """
    Downloads all the videos in a YouTube playlist.

    :param url: The URL of the YouTube playlist.
    :type url: str

    :param type: A flag indicating the type of download. True for audio, False for video.
    :type type: bool

    :return: None
    """

    p1 = pytubefix.Playlist(url)
    for video in p1:
        yt = pytubefix.YouTube(video)
        download(video, type, str(yt.title))

#wrapper
print(colorama.Fore.GREEN + "Cobalt - YouTube Downloader")
mode = input(colorama.Fore.CYAN + "Enter 1 for video or 2 for playlist: ")
if mode == "1":
    url = input(colorama.Fore.BLUE + "Enter the link of the video: ")
    type = input(colorama.Fore.BLUE + "Enter 1 for audio or 2 for video: ")
    if type == "1":
        type = True
    else:
        type = False
    name = input(colorama.Fore.BLUE + "Enter the name of the file: ")
    download(url, type, name)
elif mode == "2":
    url = input(colorama.Fore.BLUE + "Enter the link of the playlist: ")
    type = input(colorama.Fore.BLUE + "Enter 1 for audio or 2 for video: ")
    if type == "1":
        type = True
    else:
        type = False
    playlist_download(url, type)