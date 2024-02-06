import numpy as np
def check_list(one:list)->bool:
    for e in one:
        if isinstance(e, int) or isinstance(e, float):
            continue
        else:
            return False
    return True
            


def give_bmi(height:list[int | float], weight:[int | float])->list[int | float]:
    
    """
    height : the height of th persons , it must be in meter
    weight : the wight of the persons, it must be un kilogram
    return : the list of bmi

    """
    if (len(height) != len(weight)):
        raise ValueError("Height and weight lists must be  same length")
    if not all(isinstance(h,(int,float)) for h in height) or not all(isinstance(w,(int,float)) for w in weight):
        raise ValueError("element of the weight or height list must be int or float")
    arr_height =np.array(height)
    arr_weight =np.array(weight)
    bmi = np.divide(arr_weight, np.power(arr_height, 2))
    # n_zip = zip(weight, height)
    # bmi=[w/(h**2) for w, h in n_zip]
    return bmi.tolist()

    # try:
    #     assert check_list(height), "the height has data not integer or float"
    #     assert check_list(weight), "the weight has data not integer or float"
    #     n_zip = zip(weight, height)
    #     bmi = [w /(h **2) for w, h in n_zip ]
    #     bmi=list()
    #     for w, h in n_zip:
    #         bmi.append((w / (h * h)))
    #     return bmi
    # except AssertionError as e:
    #     print(e)



def apply_limit(bmi:list[int | float], limit:int)->list[bool]:

    """
    bmi : a list which has bmi values
    limit: compare each value of the bmi list with this limit 

    return : list of boolean, if the element of the bmi list greater than limit , it will be true , other wise it will be false
    
    """
    if not all(isinstance(b, (int , float)) for b in bmi):
        raise ValueError("elements of the bmi must be int or float")
    arr_bmi = np.array(bmi)
    condition = arr_bmi > limit
    # new_bmi = arr_bmi[condition]
    # result = [x > limit for x in bmi]
    return condition.tolist()

    # result = list()
    # for e in bmi:
    #     if e > limit:
    #         result.append(True)
    #     else:
    #         result.append(False)
    # return result


