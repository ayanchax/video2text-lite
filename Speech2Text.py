

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
                  async with semaphore:
                                try:
                # Transcribe the audio asynchronously with a semaphore limit of concurrent tasks..
                                    result = await asyncio.to_thread(self.model.transcribe, speechFilePath)
                                    return result["text"]
                                except Exception as e:
                                            return ""
       
       async def convertSpeechToText(self):
                 ct = CommonUtils()
                 files = ct.list_files(self.audio_path)
                 transcription = ''
                 semaphore = Semaphore(self.max_concurrent_tasks)
                 tasks = [self._convertSpeechToText(file,semaphore) for file in files]
                 transcriptionResults = await asyncio.gather(*tasks)
                 for transcriptionResult in transcriptionResults:
                     transcription += transcriptionResult
                 return transcription
     

    
                 



 