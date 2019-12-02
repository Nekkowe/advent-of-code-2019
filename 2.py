def processIntcode(intcode):
	"""Processes an Intcode and returns the result."""
	memory = intcode[:]
	i = 0
	while memory[i] is not 99:
		if memory[i] is 1:
			memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i+2]]
			i += 4
		elif memory[i] is 2:
			memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]
			i += 4
	return memory

def processIntcodeWithInputs(intcode, noun, verb):
	"""Processes an Intcode, with given parameters replacing positions 1 (noun) and 2 (verb), and returns the result."""
	memory = intcode[:]
	memory[1] = noun
	memory[2] = verb
	return processIntcode(memory)

if __name__ == "__main__":
	# Part 1
	with open("2.input", "r") as file:
		intcode = list(map(int, file.read().split(',')))
	intcode[1] = 12
	intcode[2] = 2
	print("Output of Intcode: ", processIntcode(intcode))

	# Part 2
	target_output = 19690720

	for noun in range(100):
		for verb in range(100):
			output = processIntcodeWithInputs(intcode, noun, verb)[0]
			if output == target_output:
				print("Target output", target_output, "reached with Noun:", noun, "Verb:", verb, "Result:", (100*noun + verb))
	print("All possible noun/verb combinations searched.")