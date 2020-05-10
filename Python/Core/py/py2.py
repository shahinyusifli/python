import datetime
import random
import string

#Ex 1
def ex_1():
	now = int(datetime.datetime.now().strftime('%w'))
	if now > 7:
		print(True)
	else:
		print(False)

ex_1_end = ex_1()


#Ex 2
def ex_2(arg):
	ran_number = random.randrange(0, 10)

	if (arg == ran_number):
		print('It is suitable. Random number is {}'.format(ran_number))
	else:
		print('It is not suitable. Random number is {}'.format(ran_number))

ex_2_end = ex_2(4)


#Ex 3
def ex_3(arg):
	if ((len(arg) - 1) > 3):
		a = arg[-3 : ]
		b = arg.replace(a, a.upper())
		print(b)
	else:
		print(arg.lower())

ex_3_end = ex_3('python') 


#Ex 4
def ex_4(*arg):
	end = arg[0] - arg[1]
	end_2 = arg[1] - arg[0]
	if (arg[0] == 5 or arg[1] == 5 or end == 5 or end_2 == 5 ):
		print(True)
	else:
		print(False)

ex_4_end = ex_4(15, 5)


#Ex 5
def ex_5(arg):
	list_new = []
	alphabet = string.ascii_lowercase
	for i in range(0,len(arg)):
		a = alphabet.find(arg[i])
		list_new.append(alphabet[a + 1])

	print(''.join(list_new))

ex_5_end = ex_5('python')


#Ex 6
def ex_6(**kwargs):

	len_word = len(kwargs["word"]) - 1
	find_let = kwargs["word"].find(kwargs["letter"])
	end = len_word + find_let

	if (end > 5):
		print('{} is bigger than 5'.format(end))
	else:
		print('{} is not bigger than 5'.format(end))

ex_6_end = ex_6(word = "python", letter = "t")
	

#Ex 7
def ex_7(*args):
	a = args[0].find(args[1])

	if (a == len(args[0]) -1):
		print(args[0][0 : 2])
	else:
		print(args[0][a : ])


ex_7_end = ex_7('python', 'n')

















	
















