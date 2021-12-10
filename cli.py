import sys
from _ast import arguments

from filter.dilatation import Dilate
from filter.gaussian_blur import Blur
from filter.grayscale import Gray
import cv2
import os
from color_text import color_text


arguments = {
    # "filter": "",
}

# arguments["filter"] = 1

def Start():
    list = os.listdir("img")
    try:
        for img in list:
            if not img.endswith('.jpg' or '.png'):
                print("Is not a jpg or a png")
            else:
                img_path = f'{input_dir}/{img}'
                image = cv2.imread(img_path)
                # image = Gray(image)
                # image = Dilatation(image)
                # image = Blur(image)

                if "blur" in arguments:
                    print("ya blur")
                    image = Blur(image, (arguments["blur"], arguments["blur"]))

                if "grayscale" in arguments:
                    print("ya grayscale")
                    image = Gray(image)

                if "dilate" in arguments:
                    print("ya dilate")
                    image = Dilate(image, (arguments["dilate"], arguments["dilate"]))

                if "ColorText" in arguments:
                    image = color_text(image, 'Baptiste Dumoulin, Ilan Petiot, Maxime Nicolas et Vahe Krikorian')

                output = f'{output_dir}/{img}'
                cv2.imwrite(output, image)
                # print(" Image successfully uploaded")
    except NameError:
        print('Input or output directory not found')



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

    elif a == '--filter':
        params = args[i + 1].split('|')

        for param in params:
            param = param.split(':')

            if param[0] == "grayscale":
                arguments[param[0]]=0
            elif param[0] == "ColorText":
                arguments[param[0]] = 0
            else:
                arguments[param[0]] = int(param[1])
            print(arguments)

    elif a == '-s' or a == '--start':
        Start()






