def process(intcode, noun=None, verb=None):
	"""
	Processes an Intcode and returns the resulting output integer.
	Given parameters substituted for positions 1 (noun) and 2 (verb).
	"""
	memory = intcode[:]

	memory[1] = noun if noun is not None else memory[1]
	memory[2] = verb if verb is not None else memory[2]

	i = 0

	while True:
		instruction = memory[i]
		opcode = instruction % 100

		chunk_size = (
			1 if opcode in [99] else
			2 if opcode in [3,4] else
			3 if opcode in [5,6] else
			4 if opcode in [1,2,7,8] else
			0)

		chunk = memory[i : i + chunk_size]
		operands = getOperands(chunk, memory)

		if opcode is 1:
			write_position = chunk[3]
			memory[write_position] = operands[0] + operands[1]
		elif opcode is 2:
			write_position = chunk[3]
			memory[write_position] = operands[0] * operands[1]
		elif opcode is 3:
			write_position = chunk[1]
			memory[write_position] = int(input("Input: "))
		elif opcode is 4:
			print("Position",i,"|",operands[0])
		elif opcode is 5:
			i = operands[1] if operands[0] else (i + chunk_size)
		elif opcode is 6:
			i = (i + chunk_size) if operands[0] else operands[1]
		elif opcode is 7:
			write_position = chunk[3]
			memory[write_position] = 1 if operands[0] < operands[1] else 0
		elif opcode is 8:
			write_position = chunk[3]
			memory[write_position] = 1 if operands[0] == operands[1] else 0
		elif opcode is 99:
			break
		else:
			raise ValueError("opcode not recognized: " + str(opcode))
		
		if opcode not in [5,6]:
			i += chunk_size
		
	return memory[0]

def getParameterModes(chunk):
	"""Returns the list of parameter modes contained in the chunk."""
	instruction = chunk[0]

	parameter_modes = [int(x) for x in str(instruction // 100)]
	parameter_modes.reverse()
	parameter_modes += [0] * (len(chunk) - len(parameter_modes))

	return parameter_modes

def getOperands(chunk, memory):
	operands = []
	parameter_modes = getParameterModes(chunk)

	for i in range(1, len(chunk)):
		operand = chunk[i] if parameter_modes[i-1] else memory[chunk[i]]
		operands.append(operand)
	
	return operands

def parseFromString(string):
	"""Takes an Intcode string of comma-separated integers and returns it as an integer list."""
	return list(map(int, string.split(',')))

if __name__ == "__main__":
	with open("input/5.input", "r") as file:
		intcode = parseFromString(file.read())

	print(
		"1: Air Conditioning Unit (Part 1)",
		"5: Thermal Radiator Controller (Part 2)",
		sep="\n",
	)

	process(intcode)
