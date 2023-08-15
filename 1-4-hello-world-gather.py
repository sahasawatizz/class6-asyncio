import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specific delay(in second)"""
    await asyncio.sleep(delay)
    print(f'{time.ctime()}-{message}')

async def main():
    await asyncio.gather(
        print_after("World!",2),
        print_after("Hello",1)
    )

asyncio.run(main())
    