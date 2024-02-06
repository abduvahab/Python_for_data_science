import sys

try:
    len = len(sys.argv)
    assert len <= 2, "AssertionError:more than one arguments is provide"
    if len == 2 :
        my_arg = sys.argv[1]
        my_1 = my_arg.strip()
        if(my_arg[0] == '-' or my_arg[0] == '+'):
            my_1 = my_1[1:]
        assert my_1.isdigit(), "AssertionError:argument is not an integer"
        my_3 = int(my_1)
        if(my_3 % 2 == 0):
            print("I'm Even")
        else:
            print("I'm Odd")
except AssertionError as e:
    print(e)

print()

