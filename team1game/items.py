#going to be using classes because making new ones is easier and faster than using dictionaries
class item():
	"""The base class for all items"""
	def __init__(self, id, name, description):
		self.id = id
		self.name = name
		self.description = description

#THESE EXAMPLES ARE ONLY HERE TO GIVE YOU AN IDEA ON HOW THIS CLASS WORKS, DELETE THEM WHEN YOU DON'T NEED THEM ANYMORE

example_item = item("example", "example item", "this item is an example") #example is an item

#print(example_item.id)
#print(example_item.name)
#print(example_item.description)