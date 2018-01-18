from agent import Agent
class Pedestrian(Agent):

	def __init_(self, satisfaction, personality, motivation, currentDestination):
		self.satisfaction = satisfaction
		self.personality = personality
		self.motivation = motivation
		self.currentDirections = currentDirections

	def acceptSuggestions(suggestion):
		return True

	def querySystem(qury):
		return 