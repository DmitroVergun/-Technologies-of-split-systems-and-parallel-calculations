import threading
import re


# Task 3.
def record(i: int):
    with open(f'in_{i}.txt', encoding="utf-8") as file:
        f2 = open(f'in_{i}.txt', encoding="utf-8")
        f = re.findall(f'\d+', file.read())  # search by numbers.
        sum = (str(eval(f'{f[0]} {f2.readline(1)} {f[1]}')))  # task execution
        print(sum)

    with open(f'out.txt', 'a', encoding="utf-8") as out:
        out.write(f'in_{i}.txt: {sum} \n')  # response record.


for i in range(1, 5):
    t = threading.Thread(target=record(i))
    t.start()
