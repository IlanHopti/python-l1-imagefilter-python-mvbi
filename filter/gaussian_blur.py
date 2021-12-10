import cv2
import logger

def Blur(image, kernel_size):

    if  (kernel_size[0] % 2) == 0 and (kernel_size[1] % 2) == 0 or (kernel_size[0] <= 0 and kernel_size[0] <= 0):
        print("Blur value is not odd ")

    else:

        try:

            dst = cv2.GaussianBlur(image, kernel_size, cv2.BORDER_DEFAULT)
            logger.log("Application of Blur filter ")
            return dst

        except cv2.error as e:
            print("Image not found")
            return None
