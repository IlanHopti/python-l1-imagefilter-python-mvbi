import numpy as np
import cv2


def Dilatation(image):
    try:
        kernel = np.ones((5, 5), 'uint8')

        dilate_img = cv2.dilate(image, kernel, iterations=1)
        return dilate_img

    except cv2.error:
        print("Image not found")

        return None


