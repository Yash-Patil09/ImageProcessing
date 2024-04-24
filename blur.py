# Write Python3 code here 

import cv2 
import numpy as np 

image = cv2.imread('resized_img.jpg') 

# making filter of 3 by 3 filled with 1 divide 
# by 9 for normalization 
blur_filter1 = np.ones((3, 3), np.float64)/(9.0) 

# making filter of 5 by 5 filled with 1 divide 
# by 25 for normalization 
blur_filter2 = np.ones((5, 5), np.float64)/(25.0) 

# making filter of 7 by 7 filled with 1 divide 
# by 49 for normalization 
blur_filter3 = np.ones((9,9), np.float64)/(81.0) 

image_blur1 = cv2.filter2D(image, -1, blur_filter1) 
image_blur2 = cv2.filter2D(image, -1, blur_filter2) 
image_blur3 = cv2.filter2D(image, -1, blur_filter3) 

cv2.imshow('geek', image) 
cv2.imshow('3*3 blur', image_blur1) 
cv2.imshow('5*5 blur', image_blur2) 
cv2.imshow('9*9 blur', image_blur3) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 
