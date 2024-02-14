import os, sys
import numpy as np
from PIL import Image
from load_image import ft_load


def main():
    try:
        arr_img = ft_load("./animal.jpeg")
        print("The shape of image is:",arr_img.shape)
        print(arr_img)
        # print(ft_load.__doc__)
        new_arr = arr_img[100:500,465:865,2]
        print("New shape after slicing:",new_arr.reshape(400,400,1).shape,"or",new_arr.shape)
        print(new_arr.reshape(400,400,1))
        new_img = Image.fromarray(new_arr)
        new_img.show()
    except FileNotFoundError as e:
        print(e)
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()



