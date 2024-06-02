
from pydub import AudioSegment
import os
import math
from CommonUtils import CommonUtils

class AudioSplitter:
       def __init__(self, audio_file, chunk_size=2*1024*1024, format='mp3', chunk_output_path='output/audio/chunks/'):
            # Ensure the output directory exists
            self.audio_file = audio_file
            self.chunk_size = chunk_size
            self.format = format
            utils = CommonUtils()
            self.audio_chunk_name_prefix=f"{utils.get_file_name_without_extension(self.audio_file)}"
            self.chunk_output_path = chunk_output_path+self.audio_chunk_name_prefix
            os.makedirs(self.chunk_output_path, exist_ok=True)
          
       def split_audio(self)->bool|str|None:
          try:
                  #Load the audio file
               audio = AudioSegment.from_file(self.audio_file)

               #Calculate the number of chunks
               file_size = os.path.getsize(self.audio_file)
         
               num_chunks = math.ceil(file_size / self.chunk_size)

               #Calculate chunk duration in milliseconds
               duration_ms = len(audio)
               chunk_duration_ms = duration_ms / num_chunks

               #Split and save audio chunks
               
               for i in range(num_chunks):
                start_time = i * chunk_duration_ms
                end_time = start_time + chunk_duration_ms
                chunk = audio[start_time:end_time]
                chunk_file_name = os.path.join(self.chunk_output_path, f"{self.audio_chunk_name_prefix}_{i+1}.{self.format}")
                chunk.export(chunk_file_name, format=self.format)
                print(f"Exported {chunk_file_name}")
               print("Number of chunks created", num_chunks)
               return self.chunk_output_path
          except Exception as e:
                  return None
           