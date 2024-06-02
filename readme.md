# Video2Text

Video2Text is a Python module designed to transcribe and summarize the spoken content of videos. It utilizes various components to achieve this functionality, including audio extraction, speech-to-text conversion, and text summarization.

## GPU Requirements

The speech-to-text conversion process in Video2Text can be computationally intensive, especially when handling large volumes of audio data. Since we're using the `openai-whisper` package for speech recognition, it's recommended to have a GPU with the following specifications:

- **CUDA Support**: Ensure that the GPU supports CUDA, which is required for running deep learning models efficiently. Most modern NVIDIA GPUs support CUDA.
- **VRAM (Video RAM)**: The amount of VRAM on the GPU should be sufficient to store the model weights and intermediate data during the speech recognition process. A GPU with at least 8GB of VRAM is recommended for moderate to large-scale speech recognition tasks.
- **Processing Power**: The GPU should have sufficient processing power to handle the computational workload efficiently. A mid-range to high-end GPU, such as an NVIDIA GeForce GTX 1070 or higher, or an equivalent model from other vendors, should suffice for most speech recognition tasks.

By utilizing a GPU with these specifications, you can significantly accelerate the speech-to-text conversion process, leading to faster transcription of video content.

## CPU Operations

While GPU acceleration can enhance the performance of speech-to-text conversion, Video2Text can still operate on CPU-only systems. However, certain operations, such as speech-to-text conversion, may be slower compared to running on a GPU. Other CPU-bound operations, such as video downloading, audio extraction, audio splitting and text summarization, can be performed efficiently on CPU.

## Feature Limitations

It's important to note that the current implementation of Video2Text supports transcribing and summarizing only for videos containing human voice. Videos with no human voice, only music, or mute videos are not supported in the current version. These features are planned for implementation in future versions of the module.

# Open Source and API Key
Video2Text is fully open-source and does not require an API key for operation. You can freely use and modify the code according to your requirements.

## Usage

To use Video2Text, simply instantiate the `Video2Text` class and call its `workflow` method with the path to the video file as input. The method will handle the entire process, from video downloading (if applicable) to text summarization.

Example usage:
```python
from Video2Text import Video2Text

# Instantiate Video2Text
v2t = Video2Text()

# Provide video input (YouTube URL or local file path)
video_input = "https://www.youtube.com/watch?v=your_video_id"

# Call the workflow method
summary = await v2t.workflow(video_input)

print("Summary:", summary)
```

