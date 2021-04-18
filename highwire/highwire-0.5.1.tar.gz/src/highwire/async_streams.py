import asyncio
import datetime as dt
from typing import Any

from highwire.events import Event
from highwire.streams import AsyncStream
from highwire.variables import T


async def tick(start: int, delay: dt.timedelta) -> AsyncStream[int]:
    current = start
    while True:
        yield Event(value=None, time=current)
        await asyncio.sleep(delay.total_seconds())
        current += round(delay.total_seconds() * 1000)


async def merge(t: AsyncStream[T], y: asyncio.Queue) -> AsyncStream[Any]:
    queue: asyncio.Queue = asyncio.Queue()

    async def insert_it(z):
        async for e in z:
            await queue.put(e)

    async def insert_queue(z):
        while True:
            e = await z.get()
            await queue.put(e)

    asyncio.create_task(insert_it(t))
    asyncio.create_task(insert_queue(y))

    while True:
        yield await queue.get()
