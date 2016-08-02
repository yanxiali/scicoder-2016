from fizzbuzz import fizzbuzz

def test_fizzbuzz_1():
	assert fizzbuzz(1) == 1

def test_fizzbuzz_2():
	assert fizzbuzz(2) == 2

def test_fizzbuzz_3():
	assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_4():
	assert fizzbuzz(4) == 4

def test_fizzbuzz_5():
	assert fizzbuzz(5) == 'buzz'

def test_fizzbuzz_10():
	assert fizzbuzz(10) == 'buzz'

def test_fizzbuzz_11():
	assert fizzbuzz(11) == 11

def test_fizzbuzz_15():
	assert fizzbuzz(15) == 'fizzbuzz'

def test_fizzbuzz_20():
	assert fizzbuzz(20) == 'buzz'
	
def test_fizzbuzz_23():
	assert fizzbuzz(23) == 23

def test_fizzbuzz_42():
	assert fizzbuzz(42) == 'fizz'


