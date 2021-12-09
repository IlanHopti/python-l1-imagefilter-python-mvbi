import sys

from filter.dilatation import Dilatation
from filter.gaussian_blur import Blur
from filter.grayscale import Gray
import cv2
import os


def Start():
    list = os.listdir("img")

    for img in list:
        if not img.endswith('.jpg' or '.png'):
            print("Is not a jpg or a png")
        else:
            img_path = f'{input_dir}/{img}'
            image = cv2.imread(img_path)
            image = Gray(image)
            image = Dilatation(image)
            image = Blur(image)

            output = f'{output_dir}/{img}'
            cv2.imwrite(output, image)

            print(" Image successfully uploaded")

args = sys.argv

for i, a in enumerate(args):

    if a == '-h' or a == '--help':
        print("usage: imagefilter\n"
              "-h, --help :\n"
              "-i,--input-dir <directory>\n"
              "-o,--output-dir <directory>\n")

    elif a == '-i' or a == '--input-dir':
        input_dir = args[i + 1]
        # mettre input_dir dans img du main
        print(input_dir)

    elif a == '-o' or a == '--output-dir':
        output_dir = args[i + 1]
        # mettre output_dir dans le fichier output du main
        print(output_dir)

    elif a == '-s' or a == '--start':
        Start()




