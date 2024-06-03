import os
from ffmpeg import FFmpeg
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
        """
        Extracts audio from a video file using ffmpeg-python.

        Parameters:
        self (AudioExtractor): The instance of the AudioExtractor class.

        Returns:
        dict: A dictionary containing the result or error information.
              If successful, the dictionary contains the key "result" with the path of the extracted audio file.
              If an error occurs, the dictionary contains the keys "error" and "exception" with the error details.
        """
        try:

            output_filename = self.utils.get_file_name_without_extension(
                self.video_path
            )
            audio_output = os.path.join(
                self.output_path, output_filename + "." + self.format
            )

            # Extract audio from video using ffmpeg-python
            FFmpeg().option("y").input(self.video_path).output(
                audio_output, format=self.format, q="0"
            ).execute()
            return {
                "result": audio_output,
            }
        except Exception as e:
            exc_value = sys.exc_info()
            return {"error": True, "exception": str(exc_value)}
