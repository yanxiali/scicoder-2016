"""Do the fizzbuzz test"""

def fizzbuzz(x):
	y = ''
	if x%3 == 0:
		y=y+'fizz'
		
	if x%5 == 0:
		y=y+'buzz'
	
	if y == '':
		y = x
	return y
	