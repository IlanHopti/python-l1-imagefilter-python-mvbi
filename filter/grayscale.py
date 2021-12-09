import cv2

def Gray(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    except cv2.error:
        print("Image not found")

        return None
