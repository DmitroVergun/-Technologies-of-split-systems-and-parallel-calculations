import threading
from time import sleep
import numpy as np


# Task 2.
def matrix(a_matrix, b_matrix):
    print(np.dot(a_matrix, b_matrix))


for i in range(5):
    a_matrix = np.random.randint(100, size=(4, 4))  # random matrix 4:4.
    b_matrix = np.random.randint(50, size=(4, 4))
    print(f'Threading:  {i}')
    t = threading.Thread(target=matrix(a_matrix, b_matrix))
    t.start
