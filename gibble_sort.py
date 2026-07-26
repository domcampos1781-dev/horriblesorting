import random

def gibblesort(arr): #Please ignore how arr is merely decorative.
	values = ["1", "2", "3"] #Defines what the sort should look for and match.

	original_values = list(values)

	print(f"Starting Values: {original_values}") #Prints what was given to GibbleSort

	while True:
		random.shuffle(values) #Shuffles the values and shows the output.
		print(values)

		if values == original_values:
			print("Match!")
			break #When the values match the originals after being shuffled, the program ends.

gibblesort([])
