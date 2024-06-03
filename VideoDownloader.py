from pytube import YouTube
import requests
import os
import sys
class VideoDownloader:
    def __init__(self, url,output_path='output/video/'):
        # Ensure the output directory exists
        os.makedirs(output_path, exist_ok=True)
        self.url = url
        self.output_path = output_path

    def download(self):
         """
    Downloads a video from a given URL.

    Parameters:
    self (VideoDownloader): The instance of the VideoDownloader class.
    url (str): The URL of the video to be downloaded.

    Returns:
    dict: A dictionary containing the result or error information.
          If successful, the dictionary will contain the key 'result' with the path of the downloaded video.
          If an error occurs, the dictionary will contain the keys 'error' and 'exception' with the error details.
    """
         try:
             # Check if the input is a YouTube URL
          if 'youtube.com' in self.url or 'youtu.be' in self.url:
        # Download video from YouTube URL
            yt = YouTube(self.url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            output_path = video.download(output_path=self.output_path)
          else:
        # Try Download video from direct HTTP URL
            response = requests.get(self.url)
            filename = os.path.basename(self.url)
            output_path = os.path.join(self.output_path, filename)
            with open(output_path, 'wb') as f:
                f.write(response.content)
          return {"result":output_path}
         except Exception as e:
             exc_value = sys.exc_info()
             return {"error":True, "exception":str(exc_value)}
        

    

