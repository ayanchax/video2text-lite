import os
import ffmpeg
from CommonUtils import CommonUtils
import sys


class AudioExtractor:
    
    def __init__(self, video_path, output_path="output/audio/", format="wav"):
        os.makedirs(output_path, exist_ok=True)
        self.video_path = video_path
        self.output_path = output_path
        self.format = format
        self.utils = CommonUtils()

    def extractAudio(self):
        try:
            
            output_filename = self.utils.get_file_name_without_extension(self.video_path)
            print(output_filename)
            audio_output = os.path.join(
                self.output_path, output_filename + "." + self.format
            )
            # Extract audio from video using ffmpeg-python
            ffmpeg.input(self.video_path).output(
                audio_output, format=self.format, q="0"
            ).run(overwrite_output=True)
            return {
                "result": audio_output,
            }
        except Exception as e:
             exc_value  = sys.exc_info()
             return {"error":True, "exception":str(exc_value)}
