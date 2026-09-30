import asyncio


async def task(name):
    print(f"{name} started")

    await asyncio.sleep(2)

    print(f"{name} finished")


async def main():
    await asyncio.gather(
        task("AI 1"),
        task("AI 2"),
        task("AI 3")
    )


asyncio.run(main())