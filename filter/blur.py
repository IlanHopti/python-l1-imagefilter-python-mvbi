import cv2
import logger

def Blur(image, kernel_size):
    """
    Blurs an image using a Gaussian kernel.
    :param image: Url of the image to be blurred.
    :param kernel_size: blur size
    :return: returns the blurred image, if the image is not found, returns None.
    """

    if  (kernel_size[0] % 2) == 0 and (kernel_size[1] % 2) == 0 or (kernel_size[0] <= 0 and kernel_size[0] <= 0): # Check if the kernel size is odd and positive
        print("Blur value is not odd ")

    else:

        try:
            dst = cv2.GaussianBlur(image, kernel_size, cv2.BORDER_DEFAULT) # Blur the image
            return dst

        except cv2.error as e: # If the image is not found, return None
            print("Image not found")
            logger.log("Image not found")
            return None
