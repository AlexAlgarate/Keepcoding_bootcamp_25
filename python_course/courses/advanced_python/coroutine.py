import asyncio
import threading
import time


def countdown(number):
    while number > 0:
        number -= 1


def main_without_threading(count):
    start = time.time()

    countdown(count)
    countdown(count)

    print(f"\nExecution: {time.time() - start:.5f} seconds\n")


def main_with_threading(count):
    start = time.time()

    t1 = threading.Thread(target=countdown, args=(count,))
    t2 = threading.Thread(target=countdown, args=(count,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"\nExecution: {time.time() - start:.5f} seconds\n")


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main_async():
    print(f"Started at {time.strftime('%X')}")
    await say_after(1.5, "Hello")
    await say_after(1.5, "World")
    print(f"Finished at {time.strftime('%X')}")


if __name__ == "__main__":
    # count = 1000000
    # main_without_threading(count)
    # main_with_threading(count)

    asyncio.run(main_async())
