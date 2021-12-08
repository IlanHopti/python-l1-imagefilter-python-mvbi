import cv2


image = cv2.imread('../img/juan.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray)

cv2.waitKey(2000)
cv2.destroyAllWindows()

result = cv2.imwrite(r'../img/grayJuan.jpg', gray)
if result:
    print("File saved successfully")
else:
    print("Error in saving file")

