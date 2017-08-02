#  bytearray([source[, encoding[, errors]]])
# 
#       Return a new array of bytes. 
#       The bytearray class is a mutable sequence of integers in the range 0 <= x < 256. 
#       It has most of the usual methods of mutable sequences, described in Mutable Sequence Types, 
#       as well as most methods that the bytes type has, see Bytes and Bytearray Operations.

def main():
    print("bytearray([source[, encoding[, errors]]]):\n\n\tReturn a new array of bytes. \n\tThe bytearray class is a mutable sequence of integers in the range 0 <= x < 256.  \n\tIt has most of the usual methods of mutable sequences, described in Mutable Sequence Types, \n\tas well as most methods that the bytes type has, see Bytes and Bytearray Operations.\n\n")
    print("{}\n".format("#" * 100))

    print("The optional source parameter can be used to initialize the array in a few different ways:\n")

    print("If it is a string, you must also give the encoding (and optionally, errors) parameters; \nbytearray() then converts the string to bytes using str.encode().")
    print("If it is an integer, the array will have that size and will be initialized with null bytes.")
    print("If it is an object conforming to the buffer interface, a read-only buffer of the object will be used to initialize the bytes array.\n")

    print("bytearray('Some string'.encode()): \t\t{}".format(bytearray('Some string'.encode())))
    print("bytearray(21): \t\t{}".format(bytearray(21)))
    print("bytearray({'key': [1, 2, 3, 4]}): \t\t{}".format(bytearray({'key': [1, 2, 3, 4]})))



if __name__ == '__main__':
    main()