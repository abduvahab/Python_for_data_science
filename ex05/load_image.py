import os
from PIL import Image
import numpy as np

def ft_load(path:str)->np.ndarray:
    """
    path:the path of the Image
    return: an array 
    """
    assert os.path.exists(path),"file not found"
    img = Image.open(path)
    arr = np.array(img)
    print("The shape of image is:",arr.shape)
    print(arr)
    img.show()
    return arr
