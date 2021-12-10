import inspect
import sys
from _ast import arguments
import filter

from filter.dilatation import Dilate
from filter.gaussian_blur import Blur
from filter.grayscale import Gray
import cv2
import os

arguments = {}


def Start():
    """
    Start the program
    If it's not a .jpg a .png or a .jpeg file stop the program
    else it will start the program
    search for filters in arguments and apply them
    save the processed image in the output file

    """
    list = os.listdir("img")
    try:
        for img in list:
            if not img.endswith(('.jpg', '.png', '.jpeg')):
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
                    if image is None:
                        print("The configuration of blur is invalid")
                        break
                if "grayscale" in arguments:
                    print("ya grayscale")
                    image = Gray(image)

                if "dilate" in arguments:
                    print("ya dilate")
                    image = Dilate(image, (arguments["dilate"], arguments["dilate"]))

                output = f'{output_dir}/{img}'
                cv2.imwrite(output, image)
                # print(" Image successfully uploaded")
    except NameError:
        print('Input or output directory not found')


args = sys.argv

for i, a in enumerate(args):
    """
    when help is requested, print the help message
    when i is requested, print the input directory
    when o is requested, print the output directory
    when f is requested, print the filters available   
    the user can choose the filters he wants to apply
    and can parameterize them
    if he requested a filter that doesn't exist, print an error message
    if he requested a filter that exists, save the filter in the dictionary
    if he requested s or start, start the function "Start"
    
    """

    if a == '-h' or a == '--help':
        print("usage: imagefilter\n"
              "-h, --help :\n"
              "-i,--input-dir <directory>\n"
              "-o,--output-dir <directory>\n"
              "-s,--start\n"
              "--filter <parameter>\n"
              "--list-filters\n")

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
                arguments[param[0]] = 0
            else:
                arguments[param[0]] = int(param[1])

    elif a == '--list-filters':
        print("Available filters:")
        function_list = inspect.getmembers(filter, inspect.ismodule)
        for sublist in function_list:
                print(sublist[0])

    elif a == '-s' or a == '--start':
        Start()
