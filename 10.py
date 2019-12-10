import math
import numpy as np

def testAngles():
	base = {'x': 0, 'y': 0}
	testeroids = [
		{'x': 0, 'y': 2}, 
		{'x': 1, 'y': 2}, 
		{'x': 2, 'y': 2},
		{'x': 2, 'y': 1},

		{'x': 2, 'y':  0}, 
		{'x': 2, 'y': -1},
		{'x': 2, 'y': -2}, 
		{'x': 1, 'y': -2},

		{'x':  0, 'y': -2}, 
		{'x': -1, 'y': -2}, 
		{'x': -2, 'y': -2}, 
		{'x': -2, 'y': -1},

		{'x': -2, 'y': 0}, 
		{'x': -2, 'y': 1}, 
		{'x': -2, 'y': 2}, 
		{'x': -1, 'y': 2},

		##################

		{'x': 0, 'y': 1},
		{'x': 1, 'y': 1},
		{'x': 1, 'y': 0},
		{'x': 1, 'y': -1},
		{'x': 0, 'y': -1},
		{'x': -1, 'y': -1},
		{'x': -1, 'y': 0},
		{'x': -1, 'y': 1}, 
	]

	for asteroid in testeroids:
		print(getAngle(base, asteroid))


def getAngle(p1, p2):
	dx = p2["x"] - p1["x"]
	dy = p2["y"] - p1["y"]
	
	h = math.sqrt(dx**2 + dy**2)

	angle = math.asin(dx/h)
	
	if dx >= 0 and dy > 0:
		radians = math.asin(dx/h)
		angle = math.degrees(radians)
	elif dx > 0 and dy <= 0:
		radians = math.acos(dx/h)
		angle = math.degrees(radians) + 90
	elif dx <= 0 and dy < 0:
		radians = math.asin(abs(dx)/h)
		angle = math.degrees(radians) + 180
	elif dx <= 0 and dy >= 0:
		radians = math.acos(abs(dx)/h)
		angle = math.degrees(radians) + 270

	return round(angle,2)

def getDistance(p1, p2):
	dx = p2["x"] - p1["x"]
	dy = p2["y"] - p1["y"]
	
	h = math.sqrt(dx**2 + dy**2)

	return h

if __name__ == "__main__":
	with open("input/10.input", "r") as file:
		asteroids = []
		for y, line in enumerate(file):
			for x, char in enumerate(line):
				if char is "#":
					asteroids.append({"x": x, "y": -y})

	base_fitnesses = []

	for base in asteroids:
		detected_asteroids_count = 0
		detected_asteroids_angles = []

		for asteroid in asteroids:
			if asteroid is not base:
				angle = getAngle(base, asteroid)
				if angle not in detected_asteroids_angles:
					detected_asteroids_angles.append(angle)
					detected_asteroids_count += 1
		
		base_fitnesses.append({
			"coords": base,
			"asteroids": detected_asteroids_count
		})

	base_fitnesses.sort(key=lambda entry: entry["asteroids"], reverse=True)

	ideal_base = base_fitnesses[0]

	print("Part 1 | most asteroids spotted from a base:", ideal_base["asteroids"])

	base = ideal_base["coords"]

	asteroids_by_angle = {}
	for asteroid in asteroids:
		if asteroid is not base:
			
			angle = getAngle(base, asteroid)
			distance = getDistance(base, asteroid)

			entry = {
				"distance": distance,
				"coords": asteroid
			}

			if angle in asteroids_by_angle.keys():
				asteroids_by_angle[angle].append(entry)
			else:
				asteroids_by_angle[angle] = [entry]
	
	vaporized = 0

	while True:

		for angle in sorted(asteroids_by_angle):
			asteroids = asteroids_by_angle[angle]
			
			if len(asteroids):
				asteroids.sort(key=lambda asteroid: asteroid["distance"])

				vaporized_asteroid = asteroids[0]
				asteroids.remove(vaporized_asteroid)

				vaporized += 1

				if vaporized is 200:
					print("Part 2 | 200th vaporized asteroid:", vaporized_asteroid["coords"])
					break
