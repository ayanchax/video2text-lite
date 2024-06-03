from AudioExtractor import AudioExtractor
from AudioSplitter import AudioSplitter
from CommonUtils import CommonUtils
from Speech2Text import Speech2Text
from TextSummarizer import TextSummarizer
from VideoDownloader import VideoDownloader


class Video2Text:

    def __init__(self, video_input, summarize=False):
        self.ct = CommonUtils()
        self.summarize = summarize
        self.video_input = video_input

    async def workflow(self):
        """
        This function orchestrates the entire video to text conversion process.
        It handles video downloading, audio extraction, audio chunking, speech to text conversion, and optionally, text summarization.

        Parameters:
        self (Video2Text): The instance of the Video2Text class.

        Returns:
        str: The transcript of the video or a summary of the transcript if the summarize flag is True.
        str: "FAILED" if any step of the process fails.
        """
        video_input = self.video_input
        # Check if the input is a URL or a local file
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

            else:
                return (
                    "FAILED: Video not downloaded due to error:",
                    downloader["exception"],
                )

        # 2 Extract entire audio from downloaded video.
        print("Extracting audio from video")
        audioExtractor = AudioExtractor(video_path).extractAudio()
        # Assert audio extraction
        if "result" in audioExtractor:
            audio_path = audioExtractor["result"]
            print("Audio extracted successfully at", audio_path)
            # clean up video
            self.ct.delete_file(video_path)
            # 3 Gather audio chunks from extracted Audio file
            # We are gathering audio chunks from the audio so that we do not overload the speech to text functionality with a large audio file at once.
            audio_splitter = AudioSplitter(audio_path).split_audio()

        else:
            return (
                "FAILED: Audio not extracted due to error:",
                audioExtractor["exception"],
            )

        # Assert audio chunking
        if audio_splitter is not None:
            print("Splitted audio into chunks successfully", audio_splitter)
            # clean up audio
            self.ct.delete_file(audio_path)
            print("Converting speech to text")
            # Pass audio chunks collected from audio, to Speech to Text Model and return transcription text of video.
            st = Speech2Text(audio_splitter)
            transcript = await st.convertSpeechToText()
            print("Transcript:", transcript)
        else:
            return "FAILED: Splitting failed"

        # clean up audio chunks
        self.ct.delete_files(audio_splitter)
        if self.summarize is True:
            print("Summarizing transcript")
            summarizer = TextSummarizer()
            prompt = "Please summarize the following transcription"
            v2tSummary = summarizer.summarize(prompt, transcript)
            return v2tSummary if v2tSummary is not None else "FAILED"
        else:
            return transcript if transcript is not None else "FAILED"
