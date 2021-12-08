import cv2
import numpy


src = cv2.imread('img/juan.jpg', cv2.IMREAD_UNCHANGED)
dst = cv2.GaussianBlur(src,(9,9),cv2.BORDER_DEFAULT)

cv2.imshow("Gaussian Smoothing",numpy.hstack((src, dst)))


cv2.waitKey(10000)
cv2.destroyAllWindows()

result = cv2.imwrite(r'img/blurJuan.jpg', dst)
if result:
    print("File saved successfully")
else:
    print("Error in saving file")