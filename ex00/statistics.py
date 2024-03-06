class My_exception(Exception):
    """custome exception for ft_calculate function"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def ft_mean(data: any) -> None:
    if len(data) == 0:
        print("Error")
        return
    length = len(data)
    sum = 0
    for x in data:
        sum += x
    print("mean:", float(sum) / length)

def ft_quartile(data:any) -> None:
    if len(data) == 0:
        print("Error")
        return
    s_data = list(data)
    s_data.sort()
    length = len(s_data)
    index_25 = int(0.25 * (length))
    index_75 = int(0.75 * (length))
    q = list((index_25, index_75))
    quartile: list[float] = []
    for index in q:
        quartile.append(float(s_data[index]))
        # if index.is_integer():
        #     q1 = s_data[int(index) - 1]
        #     quartile.append(q1)
        # else:
        #     l_index = int(index)
        #     u_index = l_index + 1
        #     l_value = s_data[l_index - 1]
        #     u_value = s_data[u_index - 1]
        #     q1 = l_value +(index -l_index) * (u_value - l_value)
        #     quartile.append(q1)
    print("quartile:",quartile)

def ft_median(data:any) -> None:
    if len(data) == 0:
        print("Error")
        return
    length = len(data)
    my_list = list(data)
    my_list.sort()
    if (length % 2) == 0:
        sum = float(my_list[int(length / 2)] + my_list[int(length / 2) - 1])
        print("median:",sum / 2)
        pass
    elif (length % 2) == 1:
        print("median:",my_list[int((length)/ 2)])
        pass

def ft_var(data:any) -> any:
    m_d = list(data)
    sum = 0
    for x in m_d:
        sum +=x
    mean = sum / (len(m_d))
    e = 0
    for x in m_d:
        e += (x - mean)**2
    e = e / (len(m_d))
    return e

def ft_statistics(*args:any, **kwargs: any) -> None:
    """
    calculate the Mean, Median, Quartile, Standard Deviation
    and Variance according to key words
    """
    try:
        for x in args:
            if not(isinstance(x, int) or isinstance(x, float)):
                raise My_exception("the numbers must be integer or float")
        k_list = ["mean", "median", "quartile", "std", "var"]
        for value in kwargs.values():
            if value.lower() in k_list:
                if (value).lower() == "mean":
                    ft_mean(args)
                elif (value).lower() == "median":
                    ft_median(args)
                elif value.lower() == "quartile":
                    ft_quartile(args)
                elif value.lower() == "var":
                    e = ft_var(args)
                    print("var:", e)
                elif value.lower() == "std":
                    e = ft_var(args)
                    print("std:", e**(0.5))
    except My_exception as e:
        print(e)
