
ft_list = ["Hello", "tato!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
new_tuple = list(ft_tuple)
new_tuple[1] = "France!"
ft_tuple = tuple(new_tuple)
new_set = list(("Hello","Mulhouse!"))
ft_set = set(new_set)
ft_dict["Hello"] = "42Mulhouse!"
a = 7

print(a)


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
