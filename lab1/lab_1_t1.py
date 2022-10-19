import threading
from time import sleep, time


# Task 1.
class MyThread(threading.Thread):
    def run(self):
        print(f'{self.name} started!')  # flow notification.
        sleep(.2)
        print(f'{self.name} finished!')


for x in range(5):
    t = MyThread(name=f'Thread=-{x}')  # starting a thread.
    t.start()
    sleep(.3)
