if __name__ == "__main__":	
	orbits = {}
	total_orbits = 0

	with open("input/6.input", "r") as file:
		for line in file:
			objects = line.strip().split(")")
			orbited_object = objects[0]
			orbiting_object = objects[1]

			orbits[orbiting_object] = orbited_object

	for orbiting_object in orbits.keys():
		current_object = orbiting_object
		while current_object in orbits.keys():
			total_orbits += 1
			current_object = orbits[current_object]
	
	print("Part 1 | total of direct and indirect orbits:", total_orbits)