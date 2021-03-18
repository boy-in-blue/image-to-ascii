from PIL import Image
import numpy as np

# im = Image.open('cat.jpg')
# im.thumbnail((50, 100))
size = w, h = 64, 64
im = Image.new("1", size, (255))
m = np.array(im)
print(m.shape, m)
#m = m.mean(axis=2, dtype=int) #rgb to gray
# for i in range(m.shape[0]):
#     for j in range(m.shape[1]):
#         if m[i, j] > 255//2:
#             m[i, j] = 255
#         else:
#             m[i, j] = 0
# dont 'mean' it to make trippy
#m[m > 255//2] = 255 # gray to
#m[m <= 255//2] = 0  # 1 bit
m[:, w//2] = False
m[h//2, :] = False
fuckallstring = ''
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i, j] == True:
            fuckallstring += '  ' #space for white
        else:
            fuckallstring += '* ' #star for blakc
    fuckallstring += '\n'
print(m.shape, m)
im = Image.fromarray(m)
print(fuckallstring)
im.show()

