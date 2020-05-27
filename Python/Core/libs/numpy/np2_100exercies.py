#Exercies are in -- https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.md --

#Ex 1
import numpy as np
from PIL import Image

#Ex 2
def ex_2():
 	print('Numpy version is {} and conf is {}'.format(np.__version__, np.show_config())) 

ex_2_end = ex_2()


#Ex 3
def ex_3():
	null_vec = np.zeros(10)
	print(null_vec)

ex_3_end = ex_3()


#Ex 4
def ex_4():
	ex_4_np = np.zeros(10)
	print("%d bytes" % (ex_4_np.size* ex_4_np.itemsize))

ex_4_end = ex_4()


#Ex 6
def ex_6():
	ex_6_z = np.zeros(10)
	ex_6_z[4] = 1
	print(ex_6_z)

ex_6_end = ex_6()


#Ex 7
def ex_7():

	my_7 = np.arange(10,50)
	print(my_7)

ex_7_end = ex_7()


#Ex 8
def ex_8():
	
	my_8 = np.random.randint(1,10,20)
	my_8_mew = my_8[::-1]
	print('{} is last array and {} is new array'.format(my_8,my_8_mew))

ex_8_end = ex_8()


#Ex 9
def ex_9():
	
	my_9 = np.arange(0,9).reshape(3,3)
	print(my_9)

ex_9_new = ex_9()


#Ex 10
def ex_10(arg):
	
	my_10 = np.array(arg)
	print(my_10[my_10 != 0])

ex_10_end = ex_10([1, 2, 0, 0, 4, 0])


#Ex 11
def ex_11():
	
	my_11 = np.eye(3)
	print(my_11)

ex_11_new = ex_11()


#Ex 12
def ex_12():
	
	my_12 = np.random.random((3, 3, 3))
	print(my_12)

ex_12_new = ex_12()


#Ex 13
def ex_13():
	
	my_13 = np.random.random((10,10))
	print('{} is max of array and {} is min of array also {} is array'.format(np.max(my_13), np.min(my_13), my_13))

ex_13_new = ex_13()


#Ex 14
def ex_14():
	
	my_14 = np.random.random(30)
	print(my_14.mean())

ex_14_new = ex_14()


#Ex 15
def ex_15():

	my_15 = np.ones((10,10))
	my_15[1 : -1, 1 : -1] = 0
	print(my_15)

ex_15_end = ex_15()


#Ex 16
def ex_16():
	
	my_16 = np.ones((5,5))
	my_16_new = np.pad(my_16, ((1,1), (1,1)))
	print(my_16_new)

ex_16_end = ex_16()


#Ex 17
def ex_17():
	print(0 * np.nan,np.nan == np.nan, np.inf > np.nan, 
		np.nan - np.nan, np.nan in set([np.nan]), 
		0.3 == 3 * 0.1)

ex_17_end = ex_17()


#Ex 18
def ex_18():

	ex_18 = np.diag(1 + np.arange(4), k = -1)
	print(ex_18)

ex_18_end = ex_18()


#Ex 19
def ex_19():
	
	ex_19 = np.zeros((8,8), dtype = int)
	ex_19[1::2, ::2] = 1
	ex_19[::2, 1::2] = 1
	print(ex_19)

ex_19_end = ex_19()


#Ex 20
def ex_20():
	
	ex_20 = np.unravel_index(100, (6, 7, 8))
	print(ex_20)

ex_20_end = ex_20()


#Ex 22
def ex_22():
	
	ex_22 = np.random.random((5,5))
	nor_ex_22 = np.mean(ex_22) / np.std(ex_22)
	print(nor_ex_22)

ex_22_end = ex_22()


#Ex 23
def ex_23():
	
	color = np.dtype([("r", np.ubyte, 1), ("g", np.ubyte, 1), ("b", np.ubyte, 1), ("a", np.ubyte, 1)])
	print(color)

ex_23_end = ex_23()



#Ex 24
def ex_24():
	
	ex_24_1 = np.random.randint(10, 30, (5,3))
	ex_24_2 = np.random.randint(10, 30, (3,2))
	mul_ex_24 = np.dot(ex_24_1, ex_24_2)
	print(mul_ex_24)

ex_24_end = ex_24()


#Ex 25
def ex_25():
	
	ex_25 = np.arange(1, 11)
	ex_25[(3 <= ex_25) & (ex_25 <= 8)] *= 0
	print(ex_25)

ex_25_end = ex_25()


#Ex 26
def ex_26():

	print(sum(range(5),-1))
	print(sum(range(5),-1))

ex_26_end = ex_26()


#Ex 28
def ex_28():

	print(np.array(0) / np.array(0))
	print(np.array(0) // np.array(0))
	print(np.array([np.nan]).astype(int).astype(float))
	
ex_28_end = ex_28()


#Ex 29
def ex_29():
	
	ex_29 = np.random.uniform(-10, 10, 10)
	a = np.copysign(np.ceil(np.abs(ex_29)), ex_29)
	print(a)

ex_29_end = ex_29()


#Ex 30
def ex_30():
	
	ex_30_1 = np.random.randint(2, 20, 20)
	ex_30_2 = np.random.randint(3, 30, 30)
	print(np.intersect1d(ex_30_1, ex_30_2))

ex_30_end = ex_30()


#Ex 31
def ex_31():
	
	avoid_err = np.seterr(all = 'ignore')
	ex_31 = np.random.rand(3) / 0
	print(ex_31)

ex_31_end = ex_31()


#Ex 32
def ex_32():
	
	ex_32 = (np.sqrt(-1) == np.emath.sqrt(-1))
	if ex_32 is not False:
		print(True)
	else:
		print(False)

ex_32_end = ex_32()


#Ex 33
def ex_33():
	
	today = np.datetime64('2020-05', 'D')
	tomorrow = today  + np.timedelta64(1, 'D')
	yesterday = today - np.timedelta64(1, 'D')


	print(today, tomorrow, yesterday)

ex_33_end = ex_33()


#Ex 34
def ex_34():
	
	days = np.arange('2016-07', 'today', dtype = 'datetime64[D]')
	print(days)

ex_34_end = ex_34()


#Ex 35
def ex_35():

	#((A+B)*(-A/2))
	a = np.ones(10) * 4
	b = np.ones(10) * 3

	np.add(a, b, out = b)
	np.negative(a, out = a)
	np.divide(a, 2, out = a)
	np.multiply(b, a, out = b)

	print(b)

ex_35_end = ex_35()


#Ex 37
def ex_37():
	ex_37_zero = np.zeros((5,5))
	ex_37_zero += np.arange(5)
	print(ex_37_zero)

ex_37_end = ex_37()


#Ex 38
def ex_38():

	ex_38_list = []
	for x in range(1,10):
		ex_38_list.append(x)

	ex_38 = np.array(ex_38_list)
	print(ex_38)

ex_38_end = ex_38()
	

#Ex 39
def ex_39():
	
	ex_39 = np.random.rand(11)
	print(ex_39)

ex_39_end = ex_39()


#Ex 40
def ex_40():
	
	ex_40 = np.random.randint(10, 20, 10)
	print('{} is unsorted array and {} is sorted array'.format(ex_40, np.sort(ex_40)))

ex_40_end = ex_40()


#Ex 41
def ex_41():
	
	ex_41 = np.random.randint(1, 10, 5)
	print(np.add.reduce(ex_41))

ex_41_end = ex_41()


#Ex 42
def ex_42():
	
	ex_42_1 = np.arange(1, 10, 5)
	ex_42_2 = np.arange(1, 10, 5)

	if np.array_equal(ex_42_1, ex_42_2) == True:
		print('This two arrays are equal without any tolerance for the comparison of values')
	else:
		print('They are not equal')

ex_42_end = ex_42() 


#Ex 43
def ex_43():

	ex_43 = np.ones((3, 3))
	ex_43.flags.writeable = False
	#ex_43[(1,2)] = 0
	
ex_43_end = ex_43()


#Ex 45
def ex_45():
	
	ex_45 = np.random.randint(1, 10, 5)
	ex_45[ex_45.argmax()] = 0
	print('{} is converted max value of {}'.format(ex_45[np.where(ex_45 == 0)], ex_45))

ex_45_end = ex_45()
