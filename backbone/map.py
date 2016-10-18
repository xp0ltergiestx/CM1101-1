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
				
room_reception = room("Reception", 
"""You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",
{"south": "Admins", "east": "Tutor", "west": "Parking"}, [item_biscuits, item_handbook], "", "")
 
room_admins = room("MJ and Simon's room",
"""You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",
{"north": "Reception"}, [], "", "")

room_tutor = room("your personal tutor's office",
"""You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",
{"west": "Reception"},[], "", "")

room_parking = room("the parking lot",
"""You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",
{"east": "Office", "south": "Reception"}, [], "", "")

room_office = room("the general office", 
"""You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",
{"west": "Parking"}, [item_pen], "", "")

rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}
