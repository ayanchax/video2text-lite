import asyncio
from Video2Text import Video2Text


if __name__ == "__main__":
    async def main():
        # Initialize Video2Text instance
        v2t = Video2Text()
        # Call workflow asynchronously
        video_input ="output/video/Generative AI in a Nutshell - how to survive and thrive in the age of AI.mp4"
        v2tSummary=await v2t.workflow(video_input)
        print("Summary:",v2tSummary)
    # Run main asynchronously
    asyncio.run(main())