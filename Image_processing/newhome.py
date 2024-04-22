import cv2

image = cv2.imread('images/digital-art-cute-dog.jpg')

height , width = image.shape[:2]
new_height = height // 15
new_width = width // 10

resized_image = cv2.resize(image,(new_height,new_width))

cv2.imwrite('resized_img.jpg',resized_image)
grey_img = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
cv2.imshow('rezi',grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()