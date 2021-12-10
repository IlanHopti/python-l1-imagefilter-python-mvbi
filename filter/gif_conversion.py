import glob
from PIL import Image

frames = []
imgs = glob.glob("/Users/Maxime/Desktop/PythonPyCharm/pythonImageFilter/gif_input/*.jpg")
print(imgs)
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)


frames[0].save('../output/png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all = True,
               duration=600, loop=0)



