from agent import Agent
class Vehicle(Agent):

	def __init_(self, currentDirections,Gas, Speed, Location):
		self.currentDirections = currentDirections
		self.Gas = Gas
		self.Speed = Speed
		self.Location = Location

	def acceptDirections():
		return True
	def getDirections():
		return currentDirections