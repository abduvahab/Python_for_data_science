import argparse,string

def code_to_morse(text:str):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',' ':'/',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }
    morse_code = str(" ")
    for char in text :
        if (char.upper() in morse_code_dict):
            morse_code += morse_code_dict.get(char.upper())+" "
    print(morse_code.strip())
    pass


def main():
    try:
        
        parse = argparse.ArgumentParser()
        parse.add_argument("text", type=str, help="a text to code to morse Cpode")
        args = parse.parse_args()
        text = args.text
        assert text.isprintable(), "string has a invisible character"
        # assert not any(char in string.punctuation for char in text), "punctuation charactor found!"
        assert not any(char in string.punctuation for char in text),"the arguments are bad!"
        code_to_morse(text)
    except AssertionError as e:
        print(e)


if (__name__ == "__main__"):
    main()
