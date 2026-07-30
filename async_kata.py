import asyncio, time

START = time.perf_counter()

async def fetch_result(source: str) -> str:
    await asyncio.sleep(1)
    return f"data from {source}"

SEM = asyncio.Semaphore(3)

async def fetch_limited(source: str) -> str:
    async with SEM:
        print(f"{time.perf_counter()-START: .1f}s start {source}")
        return await fetch_result(source)

async def main() -> None:
    res = await asyncio.gather(*[fetch_result(p) for p in range(5)])
    print(len(res), round(time.perf_counter() - START, 2))
    res2 = await asyncio.gather(*[fetch_limited(p) for p in range(10)])
    print(res2)
    
asyncio.run(main())