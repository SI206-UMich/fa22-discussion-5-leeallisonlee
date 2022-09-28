import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in str(sentence):
		if i == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		maxItem = self.items[0]
		for x in range(len(self.items) - 1):
			if self.items[x].stock < self.items[x + 1].stock:
				maxItem = self.items[x + 1]
		return maxItem
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		maxItem = self.items[0]
		for x in range(len(self.items) - 1):
			if self.items[x].price < self.items[x + 1].price:
				maxItem = self.items[x + 1]
		return maxItem
	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("aaaa"), 4, "Test aaaa")
		self.assertEqual(count_a("Beer"), 0, "Test Beer")
		self.assertEqual(count_a(""), 0, "Test ")
		self.assertEqual(count_a("bear"), 1, "Test bear")



	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		warehouse1 = Warehouse() #create new object
		warehouse1.add_item(self.item1) #add item
		print("Beer") 
		self.assertEqual(warehouse1.items, [self.item1], "Check if Item 1 inside")

		warehouse1.add_item(self.item2)
		self.assertEqual(warehouse1.items, [self.item1, self.item2], "Check if Item 1 and 2 inside")

		warehouse1.add_item(self.item3)
		warehouse1.add_item(self.item4)
		warehouse1.add_item(self.item5)
		self.assertEqual(warehouse1.items, [self.item1, self.item2, self.item3, self.item4, self.item5], "Check if all items inside")

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		warehouse1 = Warehouse()
		warehouse1.add_item(self.item1)
		warehouse1.add_item(self.item2)
		print(warehouse1.get_max_stock())
		print("I'm here")
		max_item = warehouse1.get_max_stock()
		self.assertEqual(max_item, self.item2, "Check if item2 returns")

		warehouse1.add_item(self.item3)
		warehouse1.add_item(self.item4)
		warehouse1.add_item(self.item5)
		print(warehouse1.get_max_stock())
		max_item = warehouse1.get_max_stock()
		self.assertEqual(max_item, self.item3, "Check if item3 returns")


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		warehouse1 = Warehouse()
		warehouse1.add_item(self.item1)
		warehouse1.add_item(self.item2)
		print(warehouse1.get_max_price())
		max_item = warehouse1.get_max_price()
		self.assertEqual(max_item, self.item1, "Check if item1 returns")
		

	
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()