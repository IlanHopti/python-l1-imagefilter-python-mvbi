import configparser
import inspect
import sys
from _ast import arguments
import filter
from filter.dilate import Dilate
from filter.blur import Blur
from filter.grayscale import Gray
from filter.gif_conversion import Gif
from filter.video_capture import VideoCapture
import logger
import cv2
import os
from filter.FilterZeTeam import color_text


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
            if not img.endswith(('.jpg', '.png', '.jpeg')): # if it's not a .jpg a .png or a .jpeg file stop the program
                print(f"{img} is not a jpg, a png or a jpeg file")
                logger.log(f"{img} is not a jpg, a png or a jpeg file")

            else:
                img_path = f'{input_dir}/{img}'
                image = cv2.imread(img_path)

                if "blur" in arguments: # if the user want to blur the image
                    image = Blur(image, (arguments["blur"], arguments["blur"]))
                    if image is None: # if the image is None stop the program
                        logger.log("Blur value is not odd ")
                        break
                    logger.log("Application of Blur filter ")


                if "grayscale" in arguments: # if the user want to grayscale the image
                    logger.log("Application of Grayscale filter")
                    image = Gray(image)


                if "dilate" in arguments: # if the user want to dilate the image
                    image = Dilate(image, (arguments["dilate"], arguments["dilate"]))
                    if image is None: # if the image is None stop the program
                        logger.log("Blur value is not odd ")
                        break
                    logger.log("Application of dilatation filter")


                if "FilterZeTeam" in arguments: # if the user want to color the image
                    image = color_text(image, 'Baptiste Dumoulin | Ilan Petiot | Maxime Nicolas | Vahe Krikorian')
                    logger.log("Application of FilterZeTeam ")


                output = f'{output_dir}/{img}'
                cv2.imwrite(output, image) # save the processed image in the output file
                logger.log("Image successfully saved to " + output_dir)

    except NameError:
        print('Input or output directory not found')
        logger.log("Input or output directory not found")


args = sys.argv


for i, a in enumerate(args):

    if a == '-h' or a == '--help':
        print("Usage: imagefilter -->\n"
              "-h, --help                   : To show all commands \n"
              "-i, --input-dir <directory>  : To set your directory where your images are \n"
              "-o, --output-dir <directory> : To set your directory where your modified images will be saved \n"
              "--gif                        : To convert your images to a gif \n"
              "--frame <--video=video-name> : To convert a video into a frame \n"
              "--list-filters               : To show the list of available filters \n"
              "--filter <\"parameter\">       : To chose your filters \n"
              "-s, --start                  : To run the function which add your selected filters on your images \n")


    elif a == '-i' or a == '--input-dir': # To set your directory where your images are
        # Initialized input directory
        input_dir = args[i + 1]
        logger.log(f"Set input to {input_dir}")


    elif a == '-o' or a == '--output-dir': # To set your directory where your modified images will be saved
        # Initialized output directory
        output_dir = args[i + 1]
        logger.log(f"Set output to {output_dir}")


    elif a == '--gif': # To convert your images to a gif
        Gif()
        logger.log("Convert images to gif")


    elif a == "--frame": # To convert a video into a frame
        params = args[i + 1].split('=')
        arguments[params[0]] = params[1]
        VideoCapture(params[1])
        logger.log("Convert video to frames")
    #   commande -i video/ -o output/ --frame "--video=videoplayback.mp4"

    elif a == '--config-file':
        configuration = configparser.ConfigParser()
        config = args[i + 1]
        configuration.read(config)

        input_dir = configuration["DEFAULT_CONFIG"]["inputdir"]
        output_dir = configuration["DEFAULT_CONFIG"]["outputdir"]
        filters = configuration["DEFAULT_CONFIG"]["filters"]

        logger.log(f"Set input to {input_dir}")
        logger.log(f"Set output to {output_dir}")
        logger.log(f"Set filters to {filters}")

    elif a == '--filter': # To chose your filters
        params = args[i + 1].split('|')

        for param in params:
            param = param.split(':')

            if param[0] == "grayscale" or param[0] == "FilterZeTeam":
                arguments[param[0]] = 0

            else:
                arguments[param[0]] = int(param[1])
    #   commande  exemple: python cli.py -i img/ -o output/ --filter "blur:9|grayscale" -s


    elif a == '--list-filters': # To show the list of available filters
        print("Available filters:")
        function_list = inspect.getmembers(filter, inspect.ismodule)
        for sublist in function_list:
            # print(sublist[0])
            if sublist[0] == 'blur': print(sublist[0] + " : Add a blurred filter to your images, value need to be odd and <0")
            elif sublist[0] == 'dilate': print(sublist[0] + " : Add a dilated filter to your images")
            elif sublist[0] == 'grayscale': print(sublist[0] + " : Add a black and white filtered filter to your images")
            elif sublist[0] == 'FilterZeTeam': print(sublist[0] + " : Add team's Name")


    elif a == '-s' or a == '--start': # To run the function which add your selected filters on your images
        Start()
