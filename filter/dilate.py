import numpy as np
import cv2
import logger


def Dilate(image, size):
    """
    Performs dilation on the image.
    :param image: url of the image
    :param size: dilate size
    :return: returns the dilated image, if the image is not found, returns None.
    """

    if size[0] <= 0 and size[0] <= 0:
        print("Blur value is not odd ")
    else:

        try:
            kernel = np.ones(size, 'uint8')
            dilate_img = cv2.dilate(image, kernel, iterations=1)
            return dilate_img

        except cv2.error:
            print("Image not found")
            logger.log("Image not found")

            return None


