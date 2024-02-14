from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_bleu, ft_grey

arr = ft_load("./landscape.jpg")
ft_invert(arr)
ft_red(arr)
ft_green(arr)
ft_bleu(arr)
ft_grey(arr)
print(ft_invert.__doc__)
