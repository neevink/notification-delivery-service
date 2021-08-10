import time
import asyncio
import aiohttp
from json import dumps


def time_str():
    while True:
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaavaaaaaaab'
        yield 'aaaaaaaaaaaaaaaaa'


async def make_request(gen):
    async with aiohttp.ClientSession() as session:
        msg = {
            'body': next(gen)
        }
        async with session.post(url='http://localhost:4567/send',
                                json=msg) as resp:
            print(resp.status)
            # print(await resp.json())


async def main(rps: float) -> None:
    gen = time_str()
    print('Ддос начался!')
    while True:
        asyncio.create_task(make_request(gen))
        await asyncio.sleep(1 / rps)


asyncio.run(main(30))
