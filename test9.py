#parent class
class Organism:
	name = "Unknown"
	species = "Unknown"
	legs = None
	arms = None
	dna = "Sequence A"
	origin = "Unknown"
	carbon_based = True

	def info(self):
		attrs = [attr for attr in dir(self) if not attr.startswith("__")]
		for prop in attrs:
			print('{}: {}'.format(prop,getattr(x,prop)))

class Game:
	variable1 = 'Hello'
	variable2 = 'World!'

if __name__ == "__main__":
	x = Organism()
	x.info()
