from cmath import e
import cv2

def gray(le_lien):

    try:
        image = cv2.imread('img/juan.jpg')
        if not le_lien.endswith('.jpg' or '.png'):
            print("Is not a jpg or a png")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            cv2.imshow('Original image', image)
            cv2.imshow('Gray image', gray)

            cv2.waitKey(3000)
            cv2.destroyAllWindows()

    except cv2.error as e:
        print("Image not found")

        try:
            result = cv2.imwrite(r'./output/grayJuan.jpg', gray)
            if result:
                print("File saved successfully")
            else:
                print("Error in saving file")
        except NameError as n:
            print("Wrong directory")
