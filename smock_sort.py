import random
from array import array
import time

def smocksort(arr):
	while arr != sorted(arr): #While it isn't sorted, keep shuffling, waiting, repeat.
		random.shuffle(arr)
		print(arr)
		time.sleep(2)
	return arr

numbers = ["3", "2", "1"] #Defines what SmockSort is given to sort.
print(f"Unsorted: {numbers}")

smocksort(numbers)

print(f"Sorted: {numbers}")
