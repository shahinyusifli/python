from matplotlib import pyplot as plt 
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

slope, intercept, p, r, std_err = stats.linregress(x, y)

def find_y(x):
	return slope*x +intercept

new_y = find_y(6)


if(abs(r) < 0.5):
	print('{} is not valid. Its validness is not over 50 precent'.format(new_y))
else:
	print('{} can be valid. Its validness is over 50 precent'.format(new_y))