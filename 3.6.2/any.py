# any(iterable)
# 
# 	Return True if any element of the iterable is true. 
# 	If the iterable is empty, return False. Equivalent to:
# 
# 	def any(iterable):
#             for element in iterable:
#                 if element:
#             	return True
#     	        return False

def main():
    print("\nany(iterable):\n\n\tReturn True if any element of the iterable is true. \n\tIf the iterable is empty, return False. \n")
    print("{}\n".format("#" * 100))

    print("List: \t\t\tany([1, 2, 3, 4]): \t\t{}".format(any([1, 2, 3, 4])))
    print("List with None: \tany([None, None, 3, None]): \t{}".format(any([None, None, 3, None])))
    print("Only None: \t\tany([None, '', 0]): \t\t{}".format(any([None, '', 0])))
    print("Empty List: \t\tany(list()): \t\t\t{}".format(any(list())))
    print("Dict Types: \t\tany(dict()): \t\t\t{}\n".format(any(dict())))


if __name__ == '__main__':
    main()
