# concurrent - is about to Managing with lots of things at once
# parallelism - is about to Executing with lots of things at once

# Threading
# Gil
# Eventloop



###############
# threading.Thread
###############

# import threading
# import requests

# class Task(threading.Thread):
#     def __init__(self, words):
#         self.words = words
#         self.total_word = len(words)
#         super().__init__()

#     def run(self):
#         for word in self.words:
#             requests.get(f"http://xxx{word}")

# t1 = Task(['w1', 'w2'])
# t2 = Task(['ww1','ww2'])
# t1.start()
# t2.start()
# t1.join()
# t2.join()



###############
# AsyncIO 协程
###############

# import asyncio
# import time

# async def task():
#     await asyncio.sleep(1)

# async def main():
#     task_list = [task() for _ in range(10)]
#     await asyncio.gather(*task_list)

# start = time.time()
# asyncio.run(main)
# print(time.time() - start)