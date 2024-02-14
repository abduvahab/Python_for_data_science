from load_image import ft_load,ft_zoom
import numpy as np
from PIL import Image

def ft_rotate(arr:np.ndarray):
    new_arr = np.transpose(arr)
    print("New shape after transpose:", new_arr.shape)
    print(new_arr)
    img = Image.fromarray(new_arr)
    img.show()



def main():
    try:
        arr = ft_load("./animal.jpeg")
        new_arr = ft_zoom(arr)
        ft_rotate(new_arr)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()

