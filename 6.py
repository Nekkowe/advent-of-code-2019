def getConnectedObjects(object_id, orbits):
	forward_lookup = [orbits[object_id] if object_id in orbits.keys() else None]
	reverse_lookup = [key for key in orbits if (orbits[key] == object_id)]
	return forward_lookup + reverse_lookup

def generateDjikstraMap(orbits, destination):
	queue = [destination]
	djikstra_map = {destination: 0}

	while len(queue):
		current_object = queue.pop(0)
		distance = djikstra_map[current_object]
		connected_objects = getConnectedObjects(current_object, orbits)
		
		for object_id in connected_objects:
			if object_id not in djikstra_map.keys():
				djikstra_map[object_id] = distance + 1
				queue.append(object_id)
	
	return djikstra_map

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

	start = orbits["YOU"]
	destination = orbits["SAN"]
	djikstra_map = generateDjikstraMap(orbits, destination)

	print("Part 2 | minimum req. # of orbital transfers:", djikstra_map[start])

	path = [start]
	while destination not in path:
		cursor = path[-1]
		connected_objects = getConnectedObjects(cursor, orbits)

		weighted_connections = [(djikstra_map[object_id], object_id) for object_id in connected_objects]
		weighted_connections.sort()
		path.append(weighted_connections[0][1])

	print("Bonus! | exact path:",path)
