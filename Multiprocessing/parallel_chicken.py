import multiprocessing
import time

def printer(word):
	print(word, end=' ')
	
def chicken():
	
	print()
	print('Why did the chicken cross the road?')
	answer = 'to get to the other side'
	
	pool = multiprocessing.Pool(processes=2)
	pool.map(printer, answer.split())
	pool.close()
	pool.join()
	print()
	
if __name__ == "__main__":
	chicken()