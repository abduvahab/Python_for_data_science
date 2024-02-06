from ft_filter import ft_filter
import sys, argparse, string

def main():
    try:
        # print(ft_filter.__doc__)
        parse = argparse.ArgumentParser()
        parse.add_argument("text",type=str, help="a string")
        parse.add_argument("number",type=int, help="a number greator than 0")

        args = parse.parse_args()
        text = args.text
        number = args.number

        # assert len(args)==2, "the arguments are bad"
        assert text.isprintable(),"text contain invisible charactor"
        assert not any(x in string.punctuation for x in text), "text contain punctuation charactor"
        assert number >= 0, "you have to enter a number bigger than 0"
        
        str_list = text.split()
        # n_list = [x for x in str_list if(len(x) > number)]
        n_list = list(ft_filter(lambda x: len(x) > number, str_list))
        print(n_list) 
        pass
    except AssertionError as e:
        print(e)


if (__name__ == "__main__"):
    main()
