import random

#Ex 1
def ex_1(argument):
	a = argument.replace(argument[1], '');
	print(a);

ex_1_end = ex_1('Baku');


#Ex 2
def ex_2(arg):
	
	len_arg = (len(arg) - 1)
	new = arg[1:len_arg]

	print(arg[len_arg] + new + arg[0])

ex_2_end = ex_2('Tabriz')


#Ex 3
def ex_3(arg):
	
	arg_23 = arg[1:3].upper()
	new = arg.replace(arg[1:3], arg_23)

	print(new)

ex_3_end = ex_3('Shusha')


#Ex 4
def ex_4(arg):

	last_3 = arg[-3:]
	two = arg.split(arg[3])

	print(two[0] + last_3 + arg[3] +two[1])

ex_4_end = ex_4('Irevan')


#Ex 5
def ex_5(arg):

	len_arg = (len(arg) - 1)
	random_num = random.randrange(0, len_arg)
	new_word = arg[random_num].upper()
	end = arg.replace(arg[random_num], new_word)

	print(end)

ex_5_end = ex_5('Derbend')


#Ex 6 
def ex_6(x):
	num = abs(13 - x)

	if (num < 13):
		print(num * 2)
	else :
		print(num)

ex_6_end = ex_6(20)


#Ex 7 
def ex_7(x):
	if(x%7 == 0 or x%3 == 0):
		print(True)
	else:
		print(False)

ex_7_end = ex_7(20)


#Ex 8
def ex_8(*arg):
	if (arg[0] > 30 and arg[1] < 70 and arg[1] > 30 and arg[0] < 70):
		print('{} and {} is between 70 and 30'.format(arg[0], arg[1]))

	elif (arg[0] > 30 and arg[1] < 70 or arg[0] < 30 and arg[1] > 70):
		print('One of {} and {}  is not between 70 and 30'.format(arg[0], arg[1]))

	else:
		print('{} and {} is not between 70 and 30'.format(arg[0], arg[1]))

ex_8_end = ex_8(50, 20)


#Ex 9
def ex_9(*arg):
	if (abs(arg[0] - 50) < abs(arg[1] -50)):
		print('{} is next to 50'.format(arg[0]))
	else:
		print('{} is next to 50'.format(arg[1]))

ex_9_end = ex_9(20, 30)


#Ex 10 
def ex_10(arg):
	new_arg = arg.split('.')

	print('{} is extention of file'.format(new_arg[1].upper()))

ex_10_end = ex_10('python.py')


#Ex 11
def ex_11(arg):
	first_let = arg[0]

	print(first_let + arg + first_let)

ex_11_end = ex_11('python')


#Ex 12
def ex_12(number, word):
	new_word = word.split(word[number - 1])
	print(new_word[0] + new_word[1])

ex_12_end = ex_12(1, 'python')


#Ex 13
def ex_13(*arg):
	if(arg[0] == arg[1]):
		print(arg[0] * 3)

	else:
		print(arg[0] + arg[1])

ex_13_end = ex_13(45, 23)


#Ex 14 
def ex_14(**kwarg):
	if (kwarg["first"] < 0 or kwarg["second"] < 0):
		print(True)
	else:
		print(False)

ex_14_end = ex_14(first = 10, second = -4)


#Ex 15
def ex_15 (**kwarg):
	new_word = kwarg["first"] in kwarg["second"]
	if (new_word == False):
		print(kwarg["first"] + kwarg["second"])
	else:
		print(kwarg["second"])


ex_15_end = ex_15(first = 'django', second = 'python')


















	
















