from ft_filter import ft_filter

s = [1, 2,-1, 4]
n_s = ft_filter(lambda x: x>0, s)
print(n_s)

for x in n_s:
    print(x)

