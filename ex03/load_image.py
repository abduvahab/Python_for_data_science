import os, sys
import numpy as np
from PIL import Image

def ft_load(path:str)->np.ndarray:
    """
    path:path of the image to be load 
    return: an array of the image 
    """    
    if not(os.path.exists(path)):
        raise FileNotFoundError("error: the file not exists")
    img = Image.open(path)
    assert img.mode == "RGB", "the pixel of the image not containt in format RGG"
    img.show()
    return (np.array(img))
