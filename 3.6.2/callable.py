#  callable(object)
# 
# 	Return True if the object argument appears callable, False if not. 
# 	If this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed. 
# 	Note that classes are callable (calling a class returns a new instance); 
# 	instances are callable if their class has a __call__() method.

class CallableClass(object):
	def __init__(self):
		pass

	def callable_method():
		print('This is callable')


def main():
	print("\nabs(x):\n\n\tReturn True if the object argument appears callable, False if not. \n\tIf this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed. \n\tNote that classes are callable (calling a class returns a new instance); \n\tinstances are callable if their class has a __call__() method.\n")
	print("{}\n".format("#" * 100))

	print("callable(dict()): {}".format(callable(dict())))
	print("callable(str()): {}".format(callable(str())))
	print("callable(list()): {}".format(callable(list())))
	print("callable(set()): {}\n".format(callable(set())))

	print("class CallableClass(object):")
	print("\tdef __init__(self):")
	print("\t\tpass\n")
	print("\tdef callable_method():")
	print("\t\tprint('This is callable')\n")

	print("callable(CallableClass)): \t\t\t{}".format(callable(CallableClass)))
	print("callable(CallableClass.callable_method)): \t{}\n".format(callable(CallableClass.callable_method)))

	cc = CallableClass()
	print("cc = CallableClass()")
	print("callable(cc)): \t\t\t\t\t{}".format(callable(cc)))
	print("callable(cc.callable_method)): \t\t\t{}\n".format(callable(cc.callable_method)))

if __name__ == '__main__':
	main()