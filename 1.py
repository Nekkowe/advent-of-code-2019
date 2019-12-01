import math

def getFuelCost(mass):
	"""
	Calculates the fuel required to propel the input mass.
	"""
	return math.floor(mass / 3) - 2

def getRecursiveFuelCost(mass):
	"""
	Calculates the fuel required to propel the input mass, 
	including the fuel required to accomodate the mass of the new fuel etc. until negligible.
	"""
	total = 0
	last_step_cost = getFuelCost(mass)

	while last_step_cost > 0:
		total += last_step_cost
		last_step_cost = getFuelCost(last_step_cost)
	
	return total

if __name__ == "__main__":
	total_part_1 = 0
	total_part_2 = 0

	with open("1.input", "r") as file:
		for line in file:
			mass = int(line)
			total_part_1 += getFuelCost(mass)
			total_part_2 += getRecursiveFuelCost(mass)

	print("Part 1 Total: ", total_part_1)
	print("Part 2 Total: ", total_part_2)