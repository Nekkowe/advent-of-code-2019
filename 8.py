import numpy as np

def countDigits(layer):
	digits = {}
	
	for digit in layer:
		digits[digit] = 1 if (digit not in digits.keys()) else digits[digit] + 1 

	return digits

def getLayerWithFewestZeroes(layers):
	digit_tallies = [
		{
			"index": i, 
			"digits": countDigits(layer)
		} for (i, layer) in enumerate(layers)
	]

	digit_tallies.sort(key=lambda x: x["digits"][0])
	
	layer_index = digit_tallies[0]["index"]
	return layers[layer_index]

if __name__ == "__main__":
	width = 25
	height = 6

	with open("input/8.input", "r") as file:
		input_string = file.read()
		image_data = [int(digit) for digit in input_string]
		assert len(image_data) % (width * height) == 0

	layers = np.reshape(image_data, (-1, width * height)).tolist()
	
	# Part 1

	part_1_layer = getLayerWithFewestZeroes(layers)
	part_1_digits = countDigits(part_1_layer)
	part_1_result = part_1_digits[1] * part_1_digits[2]
	print("Part 1 | result of multiplying # of digits:", part_1_result)
	

