from AudioExtractor import AudioExtractor
from AudioSplitter import AudioSplitter
from Speech2Text import Speech2Text
from TextSummarizer import TextSummarizer
from VideoDownloader import VideoDownloader

class Video2Text:

    def __init__(self):
        pass

    async def workflow(self, video_input):
        # Check if the input is a YouTube URL or a local file
        if video_input.startswith("http://") or video_input.startswith("https://"):
            video_type = "url"
            downloader = VideoDownloader(video_input).download()
        else:
            video_type = "local"
            video_path = video_input

        if video_type == "url":
            if "result" in downloader:
                video_path = downloader["result"]
                print("Video downloaded successfully at", video_path)
                # 2 Extract entire audio from downloaded video.
                audioExtractor = AudioExtractor(video_path).extractAudio()
            else:
                print("Video not downloaded due to error:", downloader["exception"])
                return
        else:
            audioExtractor = AudioExtractor(video_path).extractAudio()

        # Assert audio extraction
        if "result" in audioExtractor:
            audio_path = audioExtractor["result"]
            print("Audio extracted successfully at", audio_path)
            # 3 Gather audio chunks from extracted Audio file
            audio_splitter = AudioSplitter(audio_path).split_audio()

        else:
            print("Audio not extracted due to error:", audioExtractor["exception"])
            return

        # Assert audio chunking
        if audio_splitter is not None:
            print("Splitted audio into chunks successfully", audio_splitter)
            print("Converting speech to text")
            # Pass audio chunks collected from audio, to Speech to Text Model and return transcription text of video.
            st = Speech2Text(audio_splitter)
            transcript = await st.convertSpeechToText()
            print("Transcript:", transcript)
        else:
            print("Splitting failed")
            return
        print("Summarizing transcript")
        summarizer = TextSummarizer()
        prompt = "Please summarize the following transcription"
        v2tSummary = summarizer.summarize(prompt, transcript)
        return v2tSummary


