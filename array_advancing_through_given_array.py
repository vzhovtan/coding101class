"""
	In the board game, a player has to try to advance through a sequence of positions. 
	Each position has a nonnegative integer associated with it, representing the maximum you can advance from that position in one move.
	Write a program which takes an array of integers, where array[i] denotes the maximum you can advance from index, 
	and returns whether it is possible to advance to the last index starting from the beginning of the array
"""

def furthest(arr: list) -> bool:
	i, largest, last = 0, 0, len(arr)-1
	while largest < last:
		largest = max(largest, i + arr[i])
		# print("i is", i, "largest is", largest, "arr[i] is", arr[i])
		i += 1
	return largest == len(arr)-1


# driver code
if __name__ == "__main__":
	input_array_1 = [2, 4, 1, 1, 0, 1, 3] # True
	print(furthest(input_array_1))
	input_array_2 = [2, 4, 1, 1, 0, 2, 3] # False
	print(furthest(input_array_2))