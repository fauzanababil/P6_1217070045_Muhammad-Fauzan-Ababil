import cv2

img= cv2.imread('w.jpg',1)
cv2.imshow("Original Image",img)

# CLAHE
clahe= cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))

lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l,a,b= cv2.split(lab)
l2= clahe.apply(l)

lab= cv2.merge((l2,a,b))
img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('Hasil peningkatan kontras dengan CLAHE' ,img2)

cv2.waitKey(0)
cv2.destroyAllWindows()