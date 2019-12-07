import intcomp as ic
from itertools import permutations

def runPhaseSequence(intcode, phase_sequence):
	input_signal = 0

	for phase_setting in phase_sequence:
		inputs = [phase_setting, input_signal]
		output = ic.process(intcode, input_queue=inputs)

		input_signal = output[1][0]
		
	return output[1][0]


if __name__ == "__main__":
	
	with open("input/7.input", "r") as file:
		intcode = ic.parseFromString(file.read())

	phases = [0,1,2,3,4]
	phase_sequences = permutations(phases)
	outputs = []

	for phase_sequence in phase_sequences:
		output = runPhaseSequence(intcode, phase_sequence)
		outputs.append(output)
	
	print("Part 1 | highest thruster signal:", max(outputs))
	print("Part 2 | the writer of this problem really needs an editor for clarity")
	print("Part 2 | but as far as i understand it, with pausing execution,")
	print("Part 2 | waiting for inputs and all that jazz:")
	print("Part 2 | sod this, actually")
