import numpy as np
from PIL import Image

a = np.array(np.random.randint(255, size=(4,4)), int)
print(a)
for i in range(0, len(a), 2):
    for j in range(len(a[i])):
        a[i:i+2, j] = (a[i, j] + a[i+1, j]) // 2
print(a)
a = np.delete(a, range(1, len(a), 2), 0)

print(a)


a = Image.fromarray(a, "L")

a.show()