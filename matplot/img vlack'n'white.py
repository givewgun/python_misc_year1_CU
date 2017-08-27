import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('monument.png')
'''Convolution core--------------------------'''

def convolute(image,kernel): #assume kernel is 3x3 matrix
    result = np.ndarray(image.shape)
    for r in range(image.shape[0]-2):
        for c in range(image.shape[1]-2):
            v = np.sum(image[r:r+3, c:c+3] * kernel)
            result[r+1,c+1] = min(1,max(0,v))
    return result
'''-----------------------------------------'''

def to_white(image):
    a_matrix = np.array([[1, 1, 1],
                         [1, -8,1],
                         [1, 1, 1]])
    img_new = convolute(img, a_matrix)
    return img_new

def to_black(image):
    return -to_white(image)

#original-----
plt.subplot(1,3,1)
plt.imshow(img) #วาดลงmemoryก่อน
#--------to white-----------
plt.subplot(1,3,2)
plt.imshow(to_white(img))
#-----to blck------------
plt.subplot(1,3,3)
plt.imshow(to_black(img))

plt.show()
