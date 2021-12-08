import cv2
import numpy

src = cv2.imread('../img/juan.jpg', cv2.IMREAD_UNCHANGED)
ksize1 = 9
ksize2 = 9

try:
    dst = cv2.GaussianBlur(src, (ksize1, ksize2), cv2.BORDER_DEFAULT)

    cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))

    cv2.waitKey(10000)
    cv2.destroyAllWindows()
except cv2.error as e:
    print("Image not found")

try:
    result = cv2.imwrite(r'../img/output/blurJuan.jpg', dst)
    if result:
        print("File saved successfully")
    else:
        print("Error in saving file")
except NameError as n:
    print("Wrong directory")
