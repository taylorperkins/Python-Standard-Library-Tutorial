#   all(iterable)
# 
# 	Return True if all elements of the iterable are true (or if the iterable is empty). 
# 	Equivalent to:

# 	def all(iterable):
#     	    for element in iterable:
#                 if not element:
#                     return False
#             return True

class AllMain(object):
    def __init__(self):
        self._list_one = [1, 2, 3]
        self._list_two = [0, 1, 2]
        self._list_three = [1, 2, None]
        self._list_four = [1, 2, str()]
        self._list_five = [1, 2, dict()]
        self._list_six = [1, 2, list()]

    def main(self):
        print("\nall(iterable): \n\n\tReturn True if all elements of the iterable are true (or if the iterable is empy).\n")
        print("{}\n".format("#" * 100))

        print("all([1, 2, 3]): \t{}".format(all(self._list_one)))
        print("all([0, 1, 2]): \t{}".format(all(self._list_two)))
        print("all([1, 2, None]): \t{}".format(all(self._list_three)))
        print("all([1, 2, str()]): \t{}".format(all(self._list_four)))
        print("all([1, 2, dict()]): \t{}".format(all(self._list_five)))
        print("all([1, 2, list()]): \t{}\n".format(all(self._list_six)))


if __name__ == '__main__':
    all_example = AllMain()
    all_example.main()






