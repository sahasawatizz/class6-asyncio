import asyncio
import time

async def print_after(message, delay):
    print(f'{time.ctime()}-start of :',message)
    await asyncio.sleep(1)
    print(f"{time.ctime()}-end of",message)
async def main():
    #Start coroutine twice (hopefully they start!)
    first_awaitable=print_after("world!",2)
    second_awaitable=print_after("Hello",1)
    #Wait for coroutine to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())
    