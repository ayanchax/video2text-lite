import asyncio
from Video2Text import Video2Text


if __name__ == "__main__":
    async def main():
        # Initialize Video2Text instance
        v2t = Video2Text("https://www.youtube.com/watch?v=hfIUstzHs9A")
        # Call workflow asynchronously
        v2tResult=await v2t.workflow()
        print("Result:",v2tResult)
    # Run main asynchronously
    asyncio.run(main())