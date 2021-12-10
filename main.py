import logger
from filter.dilatation import Dilatation
from filter.gaussian_blur import Blur
from filter.grayscale import Gray
import cv2
import os


list = os.listdir("img")


for img in list:
    if not img.endswith('.jpg' or '.png'):
        print("Is not a jpg or a png")
    else:
        img_path = f'img/{img}'
        image = cv2.imread(img_path)
        image = Gray(image)
        image = Dilatation(image)
        image = Blur(image)

        output = f'output/{img}'
        cv2.imwrite(output, image)
        logger.log("Applied filter")
        print(" Image successfully uploaded")
