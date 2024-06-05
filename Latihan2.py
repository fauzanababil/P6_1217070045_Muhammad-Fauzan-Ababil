import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('w.jpg')
# long transformation
c = 255/np.log(1* np.max(img))
log_image= c * (np.log(img + 1))

log_image = np.array(log_image, dtype= np.uint8)
# display
plt.imshow(img)
plt.show()
plt.imshow(log_image)
plt.show()