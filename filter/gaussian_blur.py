import cv2

import logger


def Blur(image):
    ksize1 = 9
    ksize2 = 9

    if  (ksize1 and ksize2 % 2) == 0 or ksize1 and ksize2 < 0:
        print("The configuration of blur is invalid")

    else:

        try:
            dst = cv2.GaussianBlur(image, (ksize1, ksize2), cv2.BORDER_DEFAULT)
            logger.log("Application of Blur filter ")
            return dst

        except cv2.error as e:
            print("Image not found")
            return None
