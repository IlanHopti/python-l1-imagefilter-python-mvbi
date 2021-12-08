import numpy as np
import cv2

img = cv2.imread('../img/juan.jpg', 1)
cv2.imshow('Original', img)

kernel = np.ones((5, 5), 'uint8')

dilate_img = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('Dilated Image', dilate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

result = cv2.imwrite(r'../img/blurJuan.jpg', dilate_img)
if result:
    print("File saved successfully")
else:
    print("Error in saving file")