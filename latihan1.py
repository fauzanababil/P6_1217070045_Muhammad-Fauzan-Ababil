import cv2
import numpy as np

# read gambar
img=cv2.imread('w.jpg')
# operasi invers
im2= 255 - img
# menampilkan gambar
cv2.imshow('w.jpg',im2)
cv2.waitKey(0)
cv2.destroyAllWindows()