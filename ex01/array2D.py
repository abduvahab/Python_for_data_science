import numpy as np

def slice_me(family:list, start:int, end:int)->list:
    """
    family: the list to be cut
    start: the index wehre the cutting begin
    end: the index where the cutting end , ont includ ethe edn index

    return :a new list
    """
    if(len(family) == 0):
        raise ValueError(" the list is empty")
        
    for e in family:
        assert isinstance(e, list), "the argumect has not list element"
    len_list = len(family[0])
    if not all(len(e) == len_list for e in family):
        raise ValueError("the lists are not the same size")
    new_family = np.array(family)
    print("My shape is:", new_family.shape)
    slice_list = new_family[start:end]
    print("My new shape is:", slice_list.shape)
    return slice_list.tolist()
    
