from cmath import e

import cv2

try:
    image = cv2.imread('img/juan.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    cv2.imshow('Original image', image)
    cv2.imshow('Gray image', gray)

    cv2.waitKey(2000)
    cv2.destroyAllWindows()

except cv2.error as e:
    print("Image not found")


try:
    result = cv2.imwrite(r'./output/grayJuan.jpg', gray)
    if result:
        print("File saved successfully")
    else:
        print("Error in saving file")
except NameError as n:
    print("Wrong directory")




