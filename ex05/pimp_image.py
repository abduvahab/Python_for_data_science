import numpy as np
from PIL import Image

def ft_invert(arr:np.ndarray)->np.ndarray:
    """
    Invert the color of the image.
    """
    new_arr = 255 - arr
    img = Image.fromarray(new_arr)
    img.show()

def ft_red(array:np.ndarray)->np.ndarray:
    """
    change the color of the image to red.
    """
    arr = array.copy()
    arr[:, :, 1] = 0
    arr[:, :, 2] = 0
    img = Image.fromarray(arr)
    img.show()

def ft_green(array:np.ndarray)->np.ndarray:
    """
    change the color of the image to green.
    """
    arr = array.copy()
    arr[:, :, 0] = 0
    arr[:, :, 2] = 0
    img = Image.fromarray(arr)
    img.show()

def ft_bleu(array:np.ndarray)->np.ndarray:
    """
    change the color of the image to bleu.
    """
    arr = array.copy()
    arr[:, :, 0] = 0
    arr[:, :, 1] = 0
    img = Image.fromarray(arr)
    img.show()

def ft_grey(array:np.ndarray)->np.ndarray:
    """
    change the color of the image to grey.
    """
    arr = array.copy()
    arr = np.dot(arr[..., :3],[0.2989, 0.5870,0.1140])
    img = Image.fromarray(arr.astype(np.uint8))
    img.show()

