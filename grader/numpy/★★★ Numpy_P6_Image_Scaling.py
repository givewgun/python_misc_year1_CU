import numpy as np
def scale(img, c) :
    a,b = np.shape(img)
    row,col = (int(a/c),int(b/c))
    m = np.zeros((row,col), dtype = float)
    for i in range(row):
        for j in range(col):
            m[i][j] = np.mean(img[i*c:i*c + c,j*c:j*c + c])
    return m
def read_img():
    row, col = [int(e) for e in input().split()]
    img = np.ndarray((row,col))
    for i in range(row):
        img[i] = [float(e) for e in input().split()]
    return img
def show_output(out):
    for i in range(out.shape[0]):
        print(" ".join([str(e) for e in out[i]]))

img = read_img()
c = int(input())
out = scale(img, c)
show_output(out)
