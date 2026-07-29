# write fetch_result(source: str) that sleeps 1 second and returns a string; fetch 5 sources concurrently and show total runtime ~1 second
import asyncio, time

async def fetch_result(source: str) -> str:
    await asyncio.sleep(1)
    return f"data from {source}"

async def main():
    start = time.perf_counter()
    res = await asyncio.gather(*[fetch_result(p) for p in range(5)])
    print(len(res), round(time.perf_counter() - start, 2))
    
asyncio.run(main())