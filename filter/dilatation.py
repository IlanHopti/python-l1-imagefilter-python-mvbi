import numpy as np
import cv2


def dilatation(le_lien):
    img = cv2.imread(f'./img/{le_lien}', 1)
    if not le_lien.endswith('.jpg' or '.png'):
        print("Is not a jpg or a png")
    else:
        try:
            cv2.imshow('Original', img)

            kernel = np.ones((5, 5), 'uint8')

            dilate_img = cv2.dilate(img, kernel, iterations=1)

        except cv2.error as e:
            print("Image not found")

        try:
            result = cv2.imwrite(r'./output/dilated_juan.jpg', dilate_img)
            if result:
                print("File saved successfully")
            else:
                print("Error in saving file")
        except NameError as n:
            print("Wrong directory")
