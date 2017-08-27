import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('monument.png')
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
dim_percent = int(input('Dim by what percent? 0-100 ; ')) / 100.0
blur_fac = int(input("How much percent of blur 0-100?:'"))/ 100.0
#dim-----------------------
def image_dim(image):
    return img * (1 - dim_percent)
#gray-----------------------
def grayscale(image):
    # return (image[:,:,0]+image[:,:,1]+image[:,:,2])/3 สูตรเก่า
    return R*0.299 + G*0.587 + B*0.114
#sepia----------------------
def sepia(image): #กัน1.0(array)~ไว้เวลาเทียบทุกๆชุด เพราะไม่อยากได้ให้เกิน1มา)
    Rs = np.minimum(1.0, 0.393*R + 0.769*G + 0.189*G)
    Gs = np.minimum(1.0, 0.349*R + 0.686*G + 0.168*G)
    Bs = np.minimum(1.0, 0.272*R + 0.534*G + 0.131*G)
    return np.dstack((Rs,Gs,Bs)) #ซ้อน layer

'''Convolution core--------------------------'''

def convolute(image,kernel): #assume kernel is 3x3 matrix
    result = np.ndarray(image.shape)
    for r in range(image.shape[0]-2):
        for c in range(image.shape[1]-2):
            v = np.sum(image[r:r+3, c:c+3] * kernel)
            result[r+1,c+1] = min(1,max(0,v))
    return result
'''-----------------------------------------'''

#Blur convolution--------------------------------------
def blur(image):
    if blur_fac == 0:
        return image
    else:
        blur_matrix = np.full((3,3),blur_fac )
        blur_img = convolute(image,blur_matrix)
        return blur_img
    
#original-----
plt.subplot(3,2,1)
plt.imshow(img) #วาดลงmemoryก่อน
#--------dim-----------
plt.subplot(3,2,2)
plt.imshow(image_dim(img))
#-----gray------------
plt.subplot(3,2,3)
plt.imshow(grayscale(img), cmap='gray')
#-----sepia-----------
plt.subplot(3,2,4)
plt.imshow(sepia(img),)
#----blur------------
plt.subplot(3,2,5)
plt.imshow(blur(grayscale(img)),cmap='gray')

plt.show() #แสดงออกนอกจอภาพ

