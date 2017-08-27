#sin cos plot
import numpy as np
import matplotlib.pyplot as plt

#calculate the coordinate x,y that will be on sine and cos graph
x = np.arange(0 , 10*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

#Format/procedures of showing two sub-plot
plt.subplot(2 , 1, 1) #2separateplane in one column, first plane
plt.plot(x , y_sin)
plt.title('Sine')

plt.subplot(2 ,1, 2)
plt.plot(x , y_cos)
plt.title('Cosine')

plt.show()
