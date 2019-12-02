def processIntcode(intcode):
	"""Processes an Intcode and returns the resulting output integer."""
	memory = intcode[:]
	i = 0
	while memory[i] is not 99:
		if memory[i] is 1:
			memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i+2]]
			i += 4
		elif memory[i] is 2:
			memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]
			i += 4
	return memory[0]

def processIntcodeWithInputs(intcode, noun, verb):
	"""Processes an Intcode, with given parameters substituted for positions 1 (noun) and 2 (verb), and returns the resulting output integer."""
	memory = intcode[:]
	memory[1] = noun
	memory[2] = verb
	return processIntcode(memory)

def parseCommaSeparatedIntegers(string):
	"""Takes a string of comma-separated integers and returns an integer list."""
	return list(map(int, string.split(',')))

if __name__ == "__main__":
	with open("2.input", "r") as file:
		intcode = parseCommaSeparatedIntegers(file.read())

	# Part 1
	print("PART 1 | Output of Intcode: ", processIntcodeWithInputs(intcode, 12, 2))

	# Part 2
	target_output = 19690720

	for noun in range(100):
		for verb in range(100):
			output = processIntcodeWithInputs(intcode, noun, verb)
			if output == target_output:
				print("PART 2 | Target output", target_output, "reached with Noun:", noun, "Verb:", verb, "Result:", (100*noun + verb))
	print("PART 2 | All possible noun/verb combinations searched.")