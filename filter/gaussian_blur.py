import cv2
import numpy

def blur(le_lien):

    src = cv2.imread(f'./img/{le_lien}', cv2.IMREAD_UNCHANGED)

    if not le_lien.endswith('.jpg' or '.png'):
        print("Is not a jpg or a png")
    else:
        ksize1 = 9
        ksize2 = 9
        try:
            dst = cv2.GaussianBlur(src, (ksize1, ksize2), cv2.BORDER_DEFAULT)

            cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))

            cv2.waitKey(3000)
            cv2.destroyAllWindows()
        except cv2.error as e:
            print("Image not found")

        try:
            result = cv2.imwrite(r'./output/blur_juan.jpg', dst)
            if result:
                print("File saved successfully")
            else:
                print("Error in saving file")
        except NameError as n:
            print("Wrong directory")
