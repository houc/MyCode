import asyncio
import aiohttp
import requests
import time


async def get(url):
    session = aiohttp.ClientSession()
    result = await session.get(url)
    return result.status


if __name__ == '__main__':
    s = time.time()
    task = [get('http://ukuaiqi.com') for _ in range(100)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*task))


    print(time.time() - s)