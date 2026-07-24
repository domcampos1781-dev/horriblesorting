import random

def gibblesort(arr):
	values = ["1", "2", "3"] #Defines what the sort should look for and match.

	original_values = list(values)

	print(f"Starting Values: {original_values}")

	while True:
		random.shuffle(values) #Shuffles the values and shows the output.
		print(values)

		if values == original_values:
			print("Match!")
			break #When the values match the originals after being shuffled, the program ends.

gibblesort([])
