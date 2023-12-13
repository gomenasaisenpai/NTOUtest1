import numpy as np
from numpy import random
A = int(input("輸入最大值:"))
B = int(input('抽幾位:'))
data = np.arange(A)
print(random.choice(data, B))