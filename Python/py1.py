#Ex 1
def ex_1(argument):
	a = argument.replace(argument[1], '');
	print(a);

ex_1_end = ex_1('sahin');


#Ex 2
def ex_2(arg):
	
	a = arg.replace(arg[0], arg[len(arg) - 1])
	
	print(a)

ex_2_end = ex_2('Python')