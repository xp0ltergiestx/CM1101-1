from items import *
from encounter import *
from NPCs import *

class room():
	"""The base class for all rooms"""
	def __init__(self, name, description, exits, items, encounter, NPCs):
		self.name = name
		self.description = description
		self.exits = exits
		self.items = items
		self.encounter = encounter
		self.NPCs = NPCs
				
#probably implement another rooms dictionary as with the templates
#add a condition/item needed to get into the room?

#THESE EXAMPLES ARE ONLY HERE TO GIVE YOU AN IDEA ON HOW THIS CLASS WORKS, DELETE THEM WHEN YOU DON'T NEED THEM ANYMORE

example_room1 = ("Kirill's Office", "There's mountain dew and doritos scattered throughout the room. Also the occasional book.", {"south":"wu"}, example_item, "TO BE ADDED", example_NPC)
example_room2 = ("Wu's Office", "There's nothing here. Not even hope.", {"north":"kirill"}, [], "TO BE ADDED", [])

rooms = {
"wu":example_room2,
"kirill":example_room1
}

#print(rooms["kirill"])
#print("")
#print(rooms["wu"])
#print("")