import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specific delay(in second)"""
    await asyncio.sleep(delay)
    print(f'{time.ctime()}-{message}')

async def main():
    #Start coroutine twice (hopefully they start!)
    first_awaitable=asyncio.create_task(print_after("world!",2))
    second_awaitable=asyncio.create_task(print_after("Hello",1))
    #Wait for coroutine to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())
    