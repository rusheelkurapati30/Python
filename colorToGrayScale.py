#Python program to convert a color image into grayscale image.

import cv2
image = cv2.imread('D:\\Training\\Python\\2.1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
# cv2.imwrite('grayscaleImage.jpg', gray)
cv2.waitKey(2000)
cv2.destroyAllWindows()


























# cv2.imwrite("2.1.jpg", gray)
# gray=cv2.resize(image,(int(image.shape[1]/6),int(image.shape[1]/8)))