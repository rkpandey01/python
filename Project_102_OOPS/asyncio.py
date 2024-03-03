import asyncio
import time

async def func1():
    time.sleep(3)
    print("Task 1 completed")

async def func2():
    time.sleep(1)
    print("Task 2 completed")

async def func3():
    time.sleep(2)
    print("Task 3 completed")    

# async def main():
#     await func1()
#     await func2()
#     await func3()


async def main():
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    task3 = asyncio.create_task(func3())


asyncio.run(main())