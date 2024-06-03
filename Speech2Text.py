

import whisper
import asyncio
from asyncio import Semaphore
from CommonUtils import CommonUtils
class Speech2Text:
       
       def __init__(self,audio_path,max_concurrent_tasks=2):
              self.audio_path = audio_path
              self.max_concurrent_tasks = max_concurrent_tasks
              # Load the Whisper model
              self.model = whisper.load_model("medium")

       async def _convertSpeechToText(self,speechFilePath,semaphore):
                  """
    Asynchronously transcribes speech in an audio file to text using the Whisper model.
    This method is a helper method for the 'convertSpeechToText' method.

    Parameters:
    self (Speech2Text): The instance of the Speech2Text class.
    speechFilePath (str): The path to the audio file to be transcribed.
    semaphore (asyncio.Semaphore): A semaphore to limit the number of concurrent tasks.

    Returns:
    str: The transcribed text from the audio file. If an error occurs during transcription, an empty string is returned.

    Raises:
    None
    """
                  async with semaphore:
                                try:
                # Transcribe the audio asynchronously with a semaphore limit of concurrent tasks..
                                    result = await asyncio.to_thread(self.model.transcribe, speechFilePath)
                                    return result["text"]
                                except Exception as e:
                                            return ""
       
       async def convertSpeechToText(self):
                 """
    This method is responsible for converting speech in audio files to text.
    It uses asyncio and a semaphore to limit the number of concurrent tasks.

    Parameters:
    self (Speech2Text): The instance of the Speech2Text class.

    Returns:
    str: The transcribed text from the audio files.
    """
                 ct = CommonUtils()
                 files = ct.list_files(self.audio_path)[:2]
                 transcription = ''
                 semaphore = Semaphore(self.max_concurrent_tasks)
                 tasks = [self._convertSpeechToText(file,semaphore) for file in files]
                 transcriptionResults = await asyncio.gather(*tasks)
                 for transcriptionResult in transcriptionResults:
                     transcription += transcriptionResult
                 return transcription
     

    
                 



 