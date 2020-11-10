import numpy as np
import math as math
a = [[],[],[]]
binary = np.zeros((len(a),4))
print(a)

for i in range(3):
    k = a[i]
    for j in range(4):
        if k>0:
            binary[i][3-j] = k%2
            k = int(k/2)
print(binary)
