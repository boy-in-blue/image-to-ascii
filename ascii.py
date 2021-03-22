from PIL import Image, ImageOps
import numpy as np

im = Image.open('dog.jpg')
im2 = ImageOps.grayscale(im)
im2.thumbnail((178, 178))
# im.thumbnail((50, 100))
size = w, h = 64, 64
im = Image.new("1", size, (255))
m = np.array(im)
# m = m.mean(axis=2, dtype=int) #rgb to gray
# for i in range(m.shape[0]):
#     for j in range(m.shape[1]):
#         if m[i, j] > 255//2:
#             m[i, j] = 255
#         else:
#             m[i, j] = 0
# dont 'mean' it to make trippy
# m[m > 255//2] = 255 # gray to
# m[m <= 255//2] = 0  # 1 bit
m[:, w//2] = False
m[h//2, :] = False
fuckallstring = ''
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i, j] == True:
            fuckallstring += '  '  # space for white
        else:
            fuckallstring += '* '  # star for blakc
    fuckallstring += '\n'
im = Image.fromarray(m)


class Ascii:
    def __init__(self) -> None:
        self.symbols = ['#', '*', 'o', '.']

    def create8bitgrayscale(cls, size: tuple, color: int):
        return Image.new("L", size, color)

    def imagetoarray(cls, img):
        return np.array(img)

    def arraytoimage(cls, arr):
        return Image.fromarray(arr)


if __name__ == '__main__':
    a = Ascii()
    b = a.create8bitgrayscale((32, 32), 200)
    b = im2
    b = b.resize((b.size[0], b.size[1]//2))
    b = a.imagetoarray(b)
    stringshit = ''
    # for i in range(0, 32, 4):
    #     b[:, i:i+4] = 255 - range(0, 256, 256//8)[i//4]
    # for i in range(0, len(b), 2):
    #     for j in range(len(b[i])):
    #         b[i:i+2, j] = (b[i, j] + b[i+1, j]) // 2
    # b = np.delete(b, range(1, len(b), 2), 0)
    print(b)
    for i in b:
        for j in i:
            if j >= 255 - 0*32:
                print('.', end='')
            elif j >= 255 - 1*32:
                print('+', end='')
            elif j >= 255 - 2*32:
                print('o', end='')
            elif j >= 255 - 3*32:
                print('x', end='')
            elif j >= 255 - 4*32:
                print('X', end='')
            elif j >= 255 - 5*32:
                print('$', end='')
            elif j >= 255 - 6*32:
                print('&', end='')
            elif j < 255 - 6*32:
                print('@', end='')
            else:
                print(j, end='')
        print()

    print(stringshit)
    b = a.arraytoimage(b)
    b.show()


# average x[0][0] + x[1][0] and so on
# todo. document and packaging 