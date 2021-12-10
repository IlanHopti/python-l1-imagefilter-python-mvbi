import os
import cv2
from PIL import ImageColor
from matplotlib import colors

liste = os.listdir('./img')

def color_text(img,txt):
    """
    Colorize text on image
    :param img:  image to colorize
    :param txt:  text to colorize
    :return:  colored text
    """

    color = colors.to_hex('blue') 
    colorText = ImageColor.getcolor(color, 'RGB')
    org = (10, 25)
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 0.35
    thickness = 1
    bgr = list(colorText)
    bgr.reverse()
    image = cv2.putText(img, txt, org, fontface, fontscale, bgr, thickness)
    return image
