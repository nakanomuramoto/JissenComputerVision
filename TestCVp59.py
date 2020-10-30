from scipy import ndimage
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

im = np.array(Image.open('empire.jpg').convert('L'))
H = np.array([[1.4, 0.05, -100], [0.05, 1.5, -150], [0, 0, 1]])
im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))
#im2 = ndimage.affine_transform(im, H[:2, :2])

print("H[0, 2] : ", H[0, 2])
print("\nH[1, 2] : ", H[1, 2])

plt.figure()
plt.gray()
plt.imshow(im)
plt.show()
plt.imshow(im2)
plt.show()