#   all(iterable)
# 
# 	Return True if all elements of the iterable are true (or if the iterable is empty). 
# 	Equivalent to:

# 	def all(iterable):
#     	    for element in iterable:
#                 if not element:
#                     return False
#             return True

def main():
    print("\nall(iterable): \n\n\tReturn True if all elements of the iterable are true (or if the iterable is empy).\n")
    print("{}\n".format("#" * 100))

    print("all([1, 2, 3]): \t{}".format(all([1, 2, 3])))
    print("all([0, 1, 2]): \t{}".format(all([0, 1, 2])))
    print("all([1, 2, None]): \t{}".format(all([1, 2, None])))
    print("all([1, 2, str()]): \t{}".format(all([1, 2, str()])))
    print("all([1, 2, dict()]): \t{}".format(all([1, 2, dict()])))
    print("all([1, 2, list()]): \t{}\n".format(all([1, 2, list()])))


if __name__ == '__main__':
    main()






