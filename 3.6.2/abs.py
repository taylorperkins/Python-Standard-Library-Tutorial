#   abs(x)
# 
# 	Return the absolute value of a number. 
# 	The argument may be an integer or a floating point number. 
# 	If the argument is a complex number, its magnitude is returned.

def main():
    print("\nabs(x):\n\n\tReturn the absolute value of a number. \n\tThe argument may be an integer or a floating point number. \n\tIf the argument is a complex number, its magnitude is returned.\n")
    print("{}\n".format("#" * 100))

    print("abs(x) will handle standard, negative, decimal, and complex int\n")
    print("Standard: \tabs(73): {}".format(abs(73)))
    print("Negative: \tabs(-73): {}".format(abs(-73)))
    print("Decimal: \tabs(73.2): {}\n".format(abs(73.2)))
    print("In python 3, int is the same as Long.. So..\n")
    print("Complex: \tabs(0x80000000): {}\n".format(abs(0x80000000)))


if __name__ == '__main__':
    main()
