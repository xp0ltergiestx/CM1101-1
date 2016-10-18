
class class_item():
	"""The base class for all items."""
	def __init__(self, id, name, description):
		self.id = id
		self.name = name
		self.description = description

item_id = class_item("id", "id card", "Your new shiny student ID card. Expires 1 June 2017. You wonder why they have printed a suicide hotline number on it?...")
item_laptop = class_item("laptop", "laptop", "It has seen better days. At least it has a WiFi card!")
item_money = class_item("money", "money", "This wad of cash is barely enough to pay your tuition fees.")
item_biscuits = class_item("biscuits", "a pack of biscuits", "a pack of biscuits.")
item_pen = class_item("pen", "a pen", "a basic ballpoint pen.")
item_handbook = class_item("handbook", "a student handbook", "This student handbook explains everything. Seriously.")