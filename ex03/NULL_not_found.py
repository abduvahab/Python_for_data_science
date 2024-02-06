def NULL_not_found(object:any)->int:
    if (object == None):
        print(f"Nothing:{object} <class 'NoneType'>")
    elif(not(object == object)):
        print(f"Cheese:{object} <class 'float'>")
    elif((isinstance(object,int)) and (object is 0)):
        print(f"Zero:{object} <class 'int'>")
    elif((object == ' ')):
        print(f"Empty:{object} <class 'str'>")
    elif(isinstance(object, bool) and not(object) ):
        print(f"Fake:{object} <class 'bool'>")
    else:
        print("Type not found!")
        return 1
    
    pass
    

