from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import requests
from termcolor import colored

def progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    bytes_downloaded = size - bytes_remaining
    progress = (bytes_downloaded / size) * 100
    print(f"\rDownloading: {progress:.1f}%", end="")
      

def video(path="C:\\Users\\jorgi\\Downloads"):
    url = input("\nYoutube video URL: ")
    
    try:
        #Youtube object with progress bar
        yt = YouTube(url, on_progress_callback=progress)
        
        #Get the highest resolution
        stream = yt.streams.get_highest_resolution()
        
        #Download the video
        stream.download(path)
        
        print(colored("\n\nVideo downloaded successfully", "light_green"))
        
    except VideoUnavailable as e:
        print(f"\nVideo unavailable: {e}")
        
    except requests.exceptions.RequestException as e:
        print(f"\nRequest error: {e}")
        
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

          
def audio(path="C:\\Users\\jorgi\\Downloads"):
    url = input("\nYoutube video URL: ")
    
    try:
        #Youtube object with progress bar
        yt = YouTube(url, on_progress_callback=progress)
        
        #Get the highest resolution
        stream = yt.streams.get_audio_only()
        
        #Download the video
        stream.download(path)
        
        print(colored("\n\nAudio downloaded successfully", "light_green"))
        
    except VideoUnavailable as e:
        print(f"\nVideo unavailable: {e}")
        
    except requests.exceptions.RequestException as e:
        print(f"\nRequest error: {e}")
        
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


#Loop
while True:
    print(colored("Youtube downloader", "light_yellow"))
    print("1. Download video\n2. Download audio only\n3. Exit\n")
    user = input("Choose: ")
    
    try:
        if int(user) in range(1,4):
            if user == "1":
                video()
                break
                    
            elif user == "2":
                audio()
                break
            
            else:
                break
                
        else:
            print(colored("Inexistent option\n", "light_red"))  
            
    except:
        print(colored("Inexistent option\n", "light_red"))  
        continue