import string

#   ascii(obj)
# 
# 	As repr(), return a string containing a printable representation of an object, 
# 	but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes. 
# 	This generates a string similar to that returned by repr() in Python 2.


def main():
    print("\nascii(obj):\n\n\tAs repr(), return a string containing a printable representation of an object, \n\tbut escape the non-ASCII characters in the string returned by repr() using \\x, \\u or \\U escapes. \n\tThis generates a string similar to that returned by repr() in Python 2.\n")    
    print("{}\n".format("#" * 100))

    print("So what are the ASCII characters??")
    print("\n\t[1]: import string")

    print("\t[2]: print(string.ascii_letters)\n\t\t{}\n".format(string.ascii_letters))
    print("\t[3]: print(string.ascii_lowercase)\n\t\t{}\n".format(string.ascii_lowercase))
    print("\t[4]: print(string.ascii_uppercase)\n\t\t{}\n".format(string.ascii_uppercase))

    print("Awesome. So now that we know what NOT to use, we not what should qualify as a non-ASCII character.")
    print("\nsome_string = 'Œ‰ˇÁ¨ˆØ∏ÒÔÓ¸˛Ç◊ı˜Â'")
    print("ascii(some_string): {}\n".format(ascii('Œ‰ˇÁ¨ˆØ∏ÒÔÓ¸˛Ç◊ı˜Â')))    


if __name__ == '__main__':    
    main()
