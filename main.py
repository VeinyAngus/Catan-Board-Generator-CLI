import random
import os


# ------------------- BASE TILE OBJECT -------------------- #

class Tile:
	# Gets passed tile type character from list comprehensions below.
	# Number from list of numbers below. Shuffled 100 times and popped off end of list.
	def __init__(self, tile_type, number):
		self.tile_type = tile_type
		self.number = number

	def __repr__(self):
		# Returns tile type with number in format <tiletype(number)>
		if self.tile_type != 'D':
			return f'{self.tile_type}({self.number})'
		else:
			# If tile is of type desert, number not passed, instead "NA"
			return f'{self.tile_type}(NA)'


# --------------------- CONSTANTS ------------------------- #

# Number of tiles per board (base game)

WHEAT = 4
FOREST = 4
SHEEP = 4
BRICK = 3
MOUNTAIN = 3
DESERT = 1


# ------------------- BOARD GENERATOR --------------------- #


def generate_new():
	# All number tiles shuffled 100 times for max random (pseudo obviously)
	numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
	for _ in range(100):
		random.shuffle(numbers)


	# Base tile list and tile lists for each tile type
	all_tiles = list()
	wheat_tiles = [Tile('W', numbers.pop()) for i in range(WHEAT)]
	forest_tiles = [Tile('F', numbers.pop()) for i in range(FOREST)]
	sheep_tiles = [Tile('S', numbers.pop()) for i in range(SHEEP)]
	brick_tiles = [Tile('B', numbers.pop()) for i in range(BRICK)]
	mountain_tiles = [Tile('M', numbers.pop()) for i in range(MOUNTAIN)]
	desert_tiles = [Tile('D', None)]

	#Iterate over each tile list and append the tiles to the base tile list
	for t in wheat_tiles:
		all_tiles.append(t)

	for t in forest_tiles:
		all_tiles.append(t)

	for t in sheep_tiles:
		all_tiles.append(t)

	for t in brick_tiles:
		all_tiles.append(t)

	for t in mountain_tiles:
		all_tiles.append(t)

	for t in desert_tiles:
		all_tiles.append(t)

	# Shuffle the tiles
	for _ in range(100):
		random.shuffle(all_tiles)


	# Program output. Formatting is a bit wonky with the tiles but it works. Added a key for tile identification	
	print('--------------- Random Catan Board Generator (Base Game) -----------------')
	print()
	print('W = Wheat | M = Mountain | F = Forest | S = Sheep | B = Brick | D = Desert')
	print('--------------------------------------------------------------------------')
	print()
	print(f'	 <{all_tiles.pop()}>|<{all_tiles.pop()}>|<{all_tiles.pop()}>\n')
	print(f'      <{all_tiles.pop()}>|<{all_tiles.pop()}>|<{all_tiles.pop()}>|<{all_tiles.pop()}>\n')
	print(f'  <{all_tiles.pop()}>|<{all_tiles.pop()}>|<{all_tiles.pop()}>|<{all_tiles.pop()}>|<{all_tiles.pop()}>\n')
	print(f'     <{all_tiles.pop()}>|<{all_tiles.pop()}>|<{all_tiles.pop()}>|<{all_tiles.pop()}>\n')
	print(f'	 <{all_tiles.pop()}>|<{all_tiles.pop()}>|<{all_tiles.pop()}>\n')


# --------------------- PROGRAM LOOP --------------------- #


while True:
	# Tries to clear screen with linux command, then windows if that fails
	res = os.system('clear')
	if res == 1:
		os.system('cls')
	generate_new()  # After screen clearing, runs generator function
	user_choice = input('(R)estart | (E)xit | >: ').upper()  # User chooses to restart or quit
	if user_choice == 'R':
		continue
	elif user_choice == 'E':
		break
