from agent import Agent
class Leisure(Agent):

	def __init_(self, availability, offerings, contact, events, reviews):
		self.availability = availability #when the agents available to do system functions
		self.offerings = offerings #what the agent offers
		self.contact = contact #how to contact the agent
		self.events = events #what events the agent already has planne
		self.reviews = reviews #reviews for the agent

	#allows the agent to send events to advertise on the system
	def advertise(ad):
		return

	#allows a message to be sent to the agent
	def messageContact(message):
		return

	#allows an offered event to be accepted or denied
	def acceptEvent(acceptbool):
		return
