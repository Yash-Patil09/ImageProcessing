import cv2

image = cv2.imread('images/digital-art-cute-dog.jpg')

# cv2.imshow('Image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

height, width = image.shape[:2]
new_width = width // 10
new_height = height // 15

# Resize the image to half its original size
resized_image = cv2.resize(image, (new_width, new_height))

# Save or display the resized image
cv2.imwrite('resized_image.jpg', resized_image)
gray_img = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('New Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


