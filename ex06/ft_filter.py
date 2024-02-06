

def ft_filter(function , iterator):
    """
    ft_fiter(function, iterable object)

    Parameters:
    function:a function or lamda expresion       iterator: an iterable object

    return :
    an iterable new object that has the all the emlemnts met the condtion 

    """
    return (item for item in iterator if function(item))

    # n_list = list()
    # for element in iterator:
    #     if(function(element)):
    #         n_list.append(element)
    # return iter(n_list)
    # pass


