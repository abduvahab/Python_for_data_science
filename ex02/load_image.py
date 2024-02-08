import os,sys
from PIL import Image
import numpy as np

def ft_load(path:str)->np.ndarray:
    try:
        if not (os.path.exists(path)):
            raise ValueError("the path not exist")
        im = Image.open(path)
        # print(im.format,im.size,im.mode)
        assert im.mode == "RGB", "the pixels of image not content in RGB format"
        # im.show()
        img_arr = np.array(im)
        print("the shape of the image:",img_arr.shape)
        return img_arr
    except Exception as e:
        print (e)

    pass


