from PIL import Image
import numpy as np
import os

def ft_load(path:str)->np.ndarray:
    if not(os.path.exists(path)):
        raise FileNotFoundError("error:file not found")
    img = Image.open(path)
    arr_img = np.array(img)
    return  arr_img


def ft_zoom(arr:np.ndarray)->np.ndarray:
    
    new_arr = arr[100:500, 465:865,2]
    print("The shape of the image:",new_arr.reshape(400,400,1), "or", new_arr.shape)
    print(new_arr.reshape(400, 400, 1))
    return new_arr
