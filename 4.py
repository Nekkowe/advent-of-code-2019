def isPasswordValid(password):
	has_repeat_digit = False
	last_digit = "0"

	for i, digit in enumerate(str(password)):
		if i == 0:
			last_digit = digit
			continue
		
		if digit < last_digit:
			return False
		elif digit == last_digit:
			has_repeat_digit = True
		
		last_digit = digit

	return has_repeat_digit

def getRunLengths(password):
	runs = []
	run_length = 1
	last_digit = None

	for i, digit in enumerate(str(password)):
		
		if i == 0:
			last_digit = digit
			continue

		if digit == last_digit:
			run_length += 1
		else:
			runs.append(run_length)
			run_length = 1
			last_digit = digit
	
	runs.append(run_length)
	return runs

if __name__ == "__main__":

	with open("input/4.input", "r") as file:
		lower_bound = int(file.readline())
		upper_bound = int(file.readline())

	valid_passwords = [password for password in range(lower_bound,upper_bound+1) if isPasswordValid(password)]
	print("Part 1 | possible passwords:",len(valid_passwords))

	still_valid_passwords = [password for password in valid_passwords if (2 in getRunLengths(password))]
	print("Part 2 | possible passwords:",len(still_valid_passwords))