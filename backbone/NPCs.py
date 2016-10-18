class NPC():
	"""The base class for all NPCs"""
	def __init__(self, id, name, description, dialogue):
		self.id = id
		self.name = name
		self.description = description
		self.dialogue = dialogue

#THESE EXAMPLES ARE ONLY HERE TO GIVE YOU AN IDEA ON HOW THIS CLASS WORKS, DELETE THEM WHEN YOU DON'T NEED THEM ANYMORE
				
example_NPC = NPC("kirill", "Dr. Kirill", "The best lecturer.", {"memes":"I love memes.", "wu":"She's okay."})

#as you can see there's a dictionary within a class, this dictionary will enable us to use a 'talk' command in the main code
#this talk command will parse in a topic, if the topic exists the function will nicely return the name of the NPC and the 
#dialogue itself, if the topic is not present within their dialogue dictionary  add a function which returns something like
#Dr. Kirill looks confused. or something to indicate the NPC can't/won't respond to that topic

#print(example_NPC.id)
#print(example_NPC.name)
#print(example_NPC.description)
#print(example_NPC.dialogue["memes"])
#print(example_NPC.dialogue["wu"])