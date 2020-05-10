import numpy as np 
from numpy import random 
from matplotlib import pyplot as plt 
import seaborn as sns
 
  
#Ex 1
def ex_1():
	ver = np.__version__
	print('Current used NumPy version is {}'.format(ver))

ex_1_end = ex_1()


#Ex 2
def ex_2(arg):
	
	nd_arry = np.array(arg)

	print('{} is type of new array and {} is this array'.format(type(nd_arry), nd_arry))

ex_2_end = ex_2([1, 8, 80, 90])


#Ex 3
def ex_3(*args):
	a = np.array(args[0])
	b = np.array(args[1])

	print('How many dimensions the array have. First is {} and second is {}'.format(a.ndim, b.ndim))

ex_3_end = ex_3([20, 40, 80, 70], [[50, 70, 80, 90], [1, 8, 80, 90]])


#Ex 4
def ex_4(arg):
	nd_arry = np.array(arg)
	nd_sum = nd_arry[0, 1, 0] + nd_arry[1, 0, 2]

	print(nd_sum)

ex_4_end = ex_4([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])


#Ex 5
def ex_5(arg):
	nd_arry = np.array(arg)
	print(nd_arry.dtype)

ex_5_end = ex_5([1, 2, 3, 4])


#Ex 6
def ex_6(arg):
	nd_arry = np.array(arg, dtype = 'S')
	print(nd_arry.dtype)

ex_6_end = ex_6([[70, 40, 90, 100], [40, 50, 30, 80]])


#Ex 7
def ex_7(arg):

	nd_arry = np.array(arg, dtype = 'f')

	new_arry = nd_arry.astype('i')

	print('Ndarray is {} and its type is {}'.format(new_arry, new_arry.dtype))

ex_7_end = ex_7([1.1, 2.1, 3.1])


#Ex 8
def ex_8(arg):
	nd_arry = np.array(arg, dtype = 'S')
	new_arry = nd_arry.reshape(4, 2)


	print('{} is first ndarray and its type is {}. Reshape ndarray is {}'.format(nd_arry, nd_arry.dtype, new_arry))

ex_8_end = ex_8([1, 2, 3, 4, 5, 6, 7, 8])



#Ex 9
def ex_9(arg):
	
	nd_arry = np.array(arg)
	sum_arr = 0
	for x in np.nditer(nd_arry):
		sum_arr += x
	print(sum_arr)

ex_9_end = ex_9([1, 2, 3, 4, 5, 6, 7, 8])


#Ex 10
def ex_10(arg):
	
	nd_arry = np.array(arg)
	
	for idx, x in np.ndenumerate(nd_arry):
		print(idx, x)

ex_10_end = ex_10([[1, 2, 3, 4] , [5, 6, 7, 8]])


#Ex 11
def ex_11(arg):
	
	nd_arry = np.array(arg)
	
	for idx, x in np.ndenumerate(nd_arry):
		print(idx, x)

ex_11_end = ex_11([[1, 2, 3, 4] , [5, 6, 7, 8]])


#Ex 12
def ex_12(*args):
	
	nd_1 = np.array(args[0])
	nd_2 = np.array(args[1])
	nd_3 = np.concatenate((nd_1, nd_2))

	print(nd_3)

ex_12_end = ex_12([1, 2, 3 ] , [5, 6, 7 ])



#Ex 13
def ex_13(arg):
	
	nd_1 = np.array(arg)
	nd_2 = np.where(nd_1 == 100)
	print(nd_2)

ex_13_end = ex_13([[70, 40, 90] , [80, 100, 60]])


#Ex 14
def ex_14(arg):

	nd_1 = np.array(arg)
	arr_filter = nd_1 > 50
	end = nd_1[arr_filter]
	print(end)

ex_14_end = ex_14([[70, 40, 90] , [80, 100, 60]])



#Ex 15
def ex_15(arg):

	rand_np = random.randint(arg)
	print(rand_np)

ex_15_end = ex_15(50)



#Ex 16
def ex_16(*args):

	rand_np = random.randint(args[0], size = (args[1]))
	print(rand_np)

ex_16_end = ex_16(20, [2, 3])


#Ex 17
def ex_17(*args):
	
	rand_np = random.choice(args[0], size = (args[1]))

ex_17_end = ex_17([7, 4, 9] , [2, 3])


#Ex 18
def ex_18(arg):

	nd_arry = np.array(arg)
	sns.distplot(nd_arry)
	plt.show()

ex_18_end = ex_18([7, 4, 9])







	