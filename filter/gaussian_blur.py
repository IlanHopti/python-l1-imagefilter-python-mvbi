import cv2

def Blur(image, kernel_size):

    if  (kernel_size[0] % 2) == 0 and (kernel_size[1] % 2) == 0 or (kernel_size[0] <= 0 and kernel_size[0] <= 0):
        print("The configuration of blur is invalid")

    else:

        try:
            dst = cv2.GaussianBlur(image, kernel_size, cv2.BORDER_DEFAULT)
            return dst

        except cv2.error as e:
            print("Image not found")
            return None
