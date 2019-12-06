def processIntcode(intcode):
	"""Processes an Intcode and returns the resulting output integer."""
	memory = intcode[:]
	i = 0

	while True:
		instruction = memory[i]
		opcode = instruction % 100

		parameter_modes = [int(x) for x in str(instruction // 100)]
		parameter_modes.reverse()
		parameter_modes += [0,0]

		if opcode is 1:
			operand_1 = memory[i+1] if parameter_modes[0] else memory[memory[i+1]]
			operand_2 = memory[i+2] if parameter_modes[1] else memory[memory[i+2]]
			memory[memory[i+3]] = operand_1 + operand_2
			i += 4
		elif opcode is 2:
			operand_1 = memory[i+1] if parameter_modes[0] else memory[memory[i+1]]
			operand_2 = memory[i+2] if parameter_modes[1] else memory[memory[i+2]]
			memory[memory[i+3]] = operand_1 * operand_2
			i += 4
		elif opcode is 3:
			memory[memory[i+1]] = int(input("Input: "))
			i += 2
		elif opcode is 4:
			operand = memory[i+1] if parameter_modes[0] else memory[memory[i+1]]
			print("Position",i,"|",operand)
			i += 2
		elif opcode is 99:
			break
		else:
			raise ValueError("opcode not recognized: " + str(opcode))
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
	with open("input/5.input", "r") as file:
		intcode = parseCommaSeparatedIntegers(file.read())

print(processIntcode(intcode))