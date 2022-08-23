import numpy as np

a = np.arange(10).reshape(5,2) + 10

b = np.argmax(a,0)
print(b)