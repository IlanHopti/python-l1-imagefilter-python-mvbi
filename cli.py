import sys
from _ast import arguments
from filter.dilatation import Dilate
from filter.gaussian_blur import Blur
from filter.grayscale import Gray
from filter.video_capture import VideoCapture
import configparser
import cv2
import os
import logger


arguments = {}


def Start():
    list = os.listdir("img")
    try:
        for img in list:
            if not img.endswith(('.jpg', '.png', '.jpeg')):
                print(f"{img} is not a jpg, a png or a jpeg file")
            else:
                img_path = f'{input_dir}/{img}'
                image = cv2.imread(img_path)

                if "blur" in arguments:
                    image = Blur(image, (arguments["blur"], arguments["blur"]))
                    if image is None:
                        break
                    logger.log("Application of Blur filter ")

                if "grayscale" in arguments:
                    logger.log("Application of Grayscale filter")
                    image = Gray(image)


                if "dilate" in arguments:
                    image = Dilate(image, (arguments["dilate"], arguments["dilate"]))
                    logger.log("Application of dilatation filter")

                if "FilterZeTeam" in arguments:
                    image = cv2.putText(image, "Baptiste Dumoulin | Ilan Petiot | Maxime Nicolas | Vahe Krikorian",
                                        org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.35,
                                        color=(0, 0, 255), thickness=1)
                    logger.log("Application of FilterZeTeam ")

                output = f'{output_dir}/{img}'
                cv2.imwrite(output, image)
                logger.log("Image successfully saved to " + output_dir)
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

    # elif a == '--config-file':
    #     configuration = configparser.ConfigParser()
    #     config = args[i + 1]
    #     configuration.read(config)
    #
    #     input_dir = configuration["DEFAULT_CONFIG"]["inputdir"]
    #     print(configuration)


    elif a == "--frame":
        params = args[i + 1].split('=')
        arguments[params[0]] = params[1]
        VideoCapture(params[1])
    #   commande -i video/ -o output/ --frame "--video=videoplayback.mp4" -sv

    elif a == '--filter':
        params = args[i + 1].split('|')

        for param in params:
            param = param.split(':')

            if param[0] == "grayscale" or param[0] == "FilterZeTeam":
                arguments[param[0]] = 0

            else:
                arguments[param[0]] = int(param[1])
    #   commande  exemple: python cli.py -i img/ -o output/ --filter "blur:9|grayscale" -s


    elif a == '-s' or a == '--start':
        Start()
