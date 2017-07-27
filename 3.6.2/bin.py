#   bin(x)
# 
# 	Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. 
# 	If x is not a Python int object, it has to define an __index__() method that returns an integer. 

def main():
    print("\nbin(x):\n\n\tConvert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. \n\tIf x is not a Python int object, it has to define an __index__() method that returns an integer. \n")
    print("{}\n".format("#" * 100))

    print("bin(3): \t\t{}".format(bin(3)))
    print("bin(-3): \t\t{}".format(bin(-3)))

    print("\nIt's also worth noting that if you prefer or don't prefer the '0b', you could always just use format.\n")

    print("format(3, '#b'): \t{}".format(format(3, '#b')))
    print("format(-3, 'b'): \t{}\n".format(format(-3, 'b')))    


if __name__ == '__main__':
    main()
