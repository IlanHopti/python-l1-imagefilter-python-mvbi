import numpy as np
import cv2


img = cv2.imread('../img/juan.jpg', 1)

try:
    cv2.imshow('Original', img)

    kernel = np.ones((5, 5), 'uint8')

    dilate_img = cv2.dilate(img, kernel, iterations=1)
    cv2.imshow('Dilated Image', dilate_img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
except cv2.error as e:
    print("Image not found")

try:
    result = cv2.imwrite(r'../img/output/blurJuan.jpg', dilate_img)
    if result:
        print("File saved successfully")
    else:
        print("Error in saving file")
except NameError as n:
    print("Wrong directory")