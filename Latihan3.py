import cv2
import numpy as np

img = cv2.imread('w.jpg')

# mencari 4 nilai gamma
for gamma in [0.1,0.5,1.2,2.2]:
    # Apply gamma correction
    gamma_corrected= np.array(255*(img/255) ** gamma,dtype= 'uint8')

    # save gambar
    cv2.imwrite('gamma_transformed' + str(gamma)+'.jpeg',gamma_corrected)