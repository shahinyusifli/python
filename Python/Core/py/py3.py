import datetime
import random
import string

#Ex 1
def ex_1(arg):
	first = arg[0]
	last = arg[len(arg) - 1]
	arg[0] = last
	arg[len(arg) - 1] = first

	print(arg)

ex_1_end = ex_1([1, 5, 6, 7])


#Ex 2
def ex_2(arg):
	lis = []
	for x in range(0,len(arg)):
		if x==0:
			mid = str(arg[x])
		else:
			mid = str(' - ' + arg[x])
		
		lis.append(mid)
	

	print(''.join(lis))

ex_2_end = ex_2(["BMW", "Fiat", "Mercedez", "Audi", "Opel", "Bentley"])


#Ex 3
def ex_3(arg):
	if (arg == 3 or arg == 1):
		print(False)
	

ex_3_end = list(map(ex_3, [4,9,6,3]))


#Ex 4
def ex_4(arg):

	flo = str(arg).split('.')
	print(int(flo[0]) + int(flo[1]))

ex_4_end = ex_4(2.7)


#Ex 5
def ex_5(*args):
	
	a = args[0].index(args[1])
	args[0][a] = args[2]

	print(args[0])
ex_5_end = ex_5([1, 5, 7, 4], 1, 3)


#Ex 6
def ex_6(*args):
	
	args[0][args[1]] = args[2]

	print(args[0])

ex_6_end = ex_6([10, 20, 40, 50, 70], 0, 3)


#Ex 7
def ex_7(arg):
	arg.sort()

	print(arg)

ex_7_end = ex_7([-1, 5, -7, 8])


#Ex 8
def ex_8(arg):
	rand = random.randrange(0, len(arg) - 1)

	for x in range(0, len(arg)):
		if arg[x] == rand:
			a = arg[rand : rand*2]
			print(a)

		

ex_8_end = ex_8([5, 7, 7, 3, 9])


#Ex 9
def ex_9(*args):
	
	x = args[0].index(args[1])
	print('{} is between {} and {} in index'.format(args[1], x-1, x+1))
		

ex_9_end = ex_9([5, 7, 8, 3, 9], 8)


#Ex 10
def ex_10(*args):
	
	a = args[0].index(args[1])
	b = (len(args[0]) - 1) - a

	print(b)	

ex_10_end = ex_10([5, 7, 8, 3, 9], 8)


#Ex 11
def ex_11(*args):
	
	args[0].remove(args[1])
	print(args[0])

ex_11_end = ex_11([40, 20, 90, 100, 70], 20)


#Ex 12
def ex_12(arg):
	
	if (len(arg) -1) < 3:
		a = arg.lower()
		print(a) 

	else:
		new_arg = arg[-3 : ].lower()
		b = arg.replace(arg[-3 : ], new_arg)
		print(b)

ex_12_end = ex_12('PYTHON')





















	













	
















