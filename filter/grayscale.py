import cv2

def Gray(image):
    """
    Convert image to grayscale
    :param image: url of image
    :return: return grayscale image,if the image is not found, returns None.
    """
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    except cv2.error:
        print("Image not found")

        return None
