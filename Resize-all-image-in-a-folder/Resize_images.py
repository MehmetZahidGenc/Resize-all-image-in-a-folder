from PIL import Image
import os

path = "folder_path use "//" between folders example; Mehmet//CV//data//train//"
dirs = os.listdir(path)


def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((500, 500), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()


