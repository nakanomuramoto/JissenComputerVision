from scipy import ndimage

import numpy as np
import matplotlib.python as plt

im = np.array(Image.open('empire.jpg').convert('L'))
H = np.array([[1.4, 0.05, -100], [0.05, 1.5, -100], [0, 0, 1]])
im2 = ndimage.affine_transport(im, [:2, :2], (H[0, 2], H[1, 2]))

plt.figure()
plt.gray()
plt.imshow(im2)
plt.show()