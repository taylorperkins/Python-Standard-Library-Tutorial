#   bool([x])
# 
# 	Return a Boolean value, i.e. one of True or False. 
# 	x is converted using the standard truth testing procedure. 
# 	If x is false or omitted, this returns False; otherwise it returns True. 
# 	The bool class is a subclass of int (see Numeric Types — int, float, complex). 
# 	It cannot be subclassed further. Its only instances are False and True (see Boolean Values).

from fractions import Fraction
from decimal import Decimal

def main():
    print("bool([x]):\n\n\tReturn a Boolean value, i.e. one of True or False. \n\tx is converted using the standard truth testing procedure. \n\tIf x is false or omitted, this returns False; otherwise it returns True. \n\tThe bool class is a subclass of int (see Numeric Types — int, float, complex). \n\tIt cannot be subclassed further. Its only instances are False and True (see Boolean Values). \n\n")
    print("{}\n".format("#" * 100))

    print("Here are the operands considered to be false: \n")

    print("Constants defined to be false.")
    print("None: \t\t\tbool(None): \t\t{}".format(bool(None)))
    print("False: \t\t\tbool(False): \t\t{}\n".format(bool(False)))

    print("Zero of any numeric type.")
    print("Standard: \t\tbool(0): \t\t{}".format(bool(0)))
    print("Decimal: \t\tbool(Decimal(0)): \t{}".format(bool(Decimal(0))))
    print("Fraction: \t\tbool(Fraction(0, 1)): \t{}\n".format(bool(Fraction(0, 1))))

    print("Empty sequences and collections.")
    print("String: \t\tbool(''): \t\t{}".format(bool('')))
    print("Tuple: \t\t\tbool(()): \t\t{}".format(bool(())))
    print("List: \t\t\tbool([]): \t\t{}".format(bool([])))
    print("Dictionary: \t\tbool({}): \t\t{}".format('{}', bool({})))
    print("Set: \t\t\tbool(set()): \t\t{}".format(bool(set())))
    print("Range: \t\t\tbool(range(0)): \t{}\n".format(bool(range(0))))


if __name__ == '__main__':
    main()
