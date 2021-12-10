import cv2

import logger


def Gray(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        logger.log("Application of G@rayscale filter")
        return gray

    except cv2.error:
        print("Image not found")


        return None
