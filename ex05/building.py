import sys


def is_punctuation(char)->bool:
    p_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return  (char in p_characters)

def is_upper(char)->bool:
    if (char[0] >= 'A' and char[0] <= "Z"):
        return True
    return False

def is_lower(char)->bool:
    if (char[0] >= "a" and char[0] <= "z"):
        return True
    return False

def is_digit(char)->bool:
    if (char[0] >= "0" and char[0] <= "9"):
        return True
    return False


def is_space(char)->bool:
    if (char[0] == " "):
        return True
    return False




def main():
    p_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    s_len = len(sys.argv)
    my_arg = ""
    if(s_len == 1):
        my_arg = input("please enter a string :")
    if (my_arg == ""):
        assert s_len == 2, "more than one arguments is provide!"
    if(my_arg == ""):
        my_str = sys.argv[1]
    else:
        my_str = my_arg
    len_str = len(my_str)
    up_letter = 0
    low_letter = 0
    space = 0
    digits = 0
    p_letters = 0
    
    for x in my_str:
        if(is_upper(x)):
            up_letter += 1
        elif(is_lower(x)):
            low_letter += 1
        elif(is_digit(x)):
            digits += 1
        elif(is_space(x)):
            space += 1
        elif(is_punctuation(x)):
            p_letters += 1
    print(f"the textcontains {len_str} characters:")
    print(f"{up_letter} upper letters")
    print(f"{low_letter} lower letters")
    print(f"{p_letters} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")



if (__name__ == "__main__"):
    main()
