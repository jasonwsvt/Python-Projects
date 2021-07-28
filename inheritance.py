class Bird():
	size = None
	wingspan = None

	def move():
		print("Bounce!")

	def sing():
		print("Whistle whistle!")

class Birb(Bird):
	size = "small"
	roundedness = "medium"
	cuteness = "high"
	fluffiness = None
	disheveledness: None

	def move():
		print("Hop!")

	def sing():
		print("Chirp!")

class Borb(Bird):
	roundedness = "high"
	cuteness = "medium"
	muppetness = None

	def move():
		print("Waddle waddle!")

	def sing():
		print("Graaak!")