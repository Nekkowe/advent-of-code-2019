import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return str((self.x, self.y))

	def __hash__(self):
		return hash((self.x, self.y))
	
	def __eq__(self, other):
		return (self.x, self.y) == (other.x, other.y)
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def manhattanDistance(self, point):
		"""Returns the Manhattan distance to another point."""
		return abs(self.x - point.x) + abs(self.y - point.y)

class WireSegment:
	def __init__(self, starting_point, direction, distance):
		assert direction in {"U", "D", "L", "R"}, "Invalid direction"
		self.starting_point = starting_point
		self.direction = direction
		self.distance = distance
	
	def __repr__(self):
		return "WireSegment(" + str(self.starting_point) + ", " + self.direction + ", " + str(self.distance) + ")"

	def isVertical(self):
		"""Returns whether the WireSegment is aligned vertically."""
		return (self.direction in {"U", "D"})
	
	def isHorizontal(self):
		"""Returns whether the WireSegment is aligned horizontally."""
		return not self.isVertical()

	def getStartingPoint(self):
		"""Returns the starting point of the WireSegment."""
		return self.starting_point

	def getEndPoint(self):
		"""Returns the ending point of the WireSegment."""
		x = self.starting_point.x
		y = self.starting_point.y

		if self.direction is "L":
			return Point(x - self.distance, y)
		elif self.direction is "R":
			return Point(x + self.distance, y)
		elif self.direction is "U":
			return Point(x, y + self.distance)
		elif self.direction is "D":
			return Point(x, y - self.distance)
	
	def getPoints(self):
		"""Returns all grid points touched by the WireSegment."""
		start = self.starting_point
		end = self.getEndPoint()

		if self.direction is "L":
			return {Point(x, start.y) for x in range(end.x, start.x + 1)}
		elif self.direction is "R":
			return {Point(x, start.y) for x in range(start.x, end.x + 1)}
		elif self.direction is "U":
			return {Point(start.x, y) for y in range(start.y, end.y + 1)}
		elif self.direction is "D":
			return {Point(start.x, y) for y in range(end.y, start.y + 1)}

	def getIntersections(self, segment):
		"""Checks against another WireSegment and returns the set of all intersections."""
		a1 = self.getStartingPoint()
		a2 = self.getEndPoint()
		b1 = segment.getStartingPoint()
		b2 = segment.getEndPoint()

		if (
			min(a1.x, a2.x) > max(b1.x, b2.x) or
			max(a1.x, a2.x) < min(b1.x, b2.x) or
			min(a1.y, a2.y) > max(b1.y, b2.y) or
			max(a1.y, a2.y) < min(b1.y, b2.y)
		):
			return set()
		else:
			return self.getPoints().intersection(segment.getPoints())
	
	def stepsToReachPoint(self, point):
		"""Returns the number of steps along the WireSegment it takes to reach the given Point."""
		#assert point in self.getPoints()
		return self.starting_point.manhattanDistance(point)
		

class Wire:
	def __init__(self, segments):
		self.segments = segments
		self.starting_point = segments[0].starting_point

	def isContinuous(self):
		"""Returns whether all consecutive WireSegments of the Wire are connected."""
		cursor = self.starting_point
		for segment in self.segments:
			if cursor == segment.getStartingPoint():
				cursor = segment.getEndPoint()
			else:
				return False
		return True

	def getPoints(self):
		"""Returns all grid points touched by the Wire."""
		points = set()
		for segment in self.segments:
			points = points.union(segment.getPoints())
		return points

	def getIntersections(self, wire):
		"""Checks against another Wire or WireSegment and returns the set of all intersections."""
		return set.intersection(self.getPoints(), wire.getPoints())
	
	def stepsToReachPoint(self, point):
		"""Returns the number of steps along the Wire it takes to reach the given Point."""
		#assert point in self.getPoints()
		steps = 0
		for segment in self.segments:
			if point in segment.getPoints():
				steps += segment.stepsToReachPoint(point)
				break
			else:
				steps += segment.distance
		return steps


if __name__ == "__main__":
	with open("3.input", "r") as file:

		wires = []

		for line in file:
			wire = line.strip().split(",")
			wire = [(x[0], x[1:]) for x in wire]

			cursor = Point(0,0)
			segments = []

			for part in wire:
				direction = part[0]
				distance = int(part[1])

				segment = WireSegment(cursor, direction, distance)
				segments.append(segment)

				cursor = segment.getEndPoint()
			
			wires.append(Wire(segments))

	central_port = Point(0,0)

	wire_a = wires[0]
	wire_b = wires[1]

	intersections = Wire.getIntersections(wire_a, wire_b)
	intersections.remove(central_port)
	
	# Part 1

	closestDistance = min([central_port.manhattanDistance(point) for point in intersections])
	print(closestDistance)

	# Part 2

	fewestCombinedSteps = min([wire_a.stepsToReachPoint(point) + wire_b.stepsToReachPoint(point) for point in intersections])
	print(fewestCombinedSteps)