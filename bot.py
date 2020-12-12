'''
TEMPLATE for creating your own Agent to compete in
'Dungeons and Data Structures' at the Coder One AI Sports Challenge 2020.
For more info and resources, check out: https://bit.ly/aisportschallenge

BIO:
<Tell us about your Agent here>

'''

# import any external packages by un-commenting them
# if you'd like to test / request any additional packages - please check with the Coder One team
import random
import numpy as np
import time
from collections import deque
# import time
# import numpy as np
# import pandas as pd
# import sklearn

class Agent:

	def __init__(self):
		'''
		Place any initialisation code for your agent here (if any)
		'''
		# a list of all the actions your Agent can choose from
		self._actions = ['', 'u', 'd', 'l','r','p']

	def next_move(self, game_state, player_state):

		self._my_id = player_state.id # Getting my id

		# test how long it takes to construct game map
		start_time = time.time()
		self._map = self._get_matrix(game_state)
		end_time = time.time()
		print(f"Time to construct game_map:  {end_time - start_time:.10f}") 
		# about 1/10th of a tick? ~ 0.0005 seconds (depends on system)

		## Agressive Bot Code ##
		opponent_location = game_state.opponents(self._my_id)

		if player_state.ammo >= 1:
			# Find a path to the opponent's location and travel toward it
			# if and when we are within range of placing a bomb, we must place the bomb
			# then as we wait for it to explode we must pick up bombs that are
			# in close vacinity of the opponent.

			action = self._get_next_move(opponent_location)
		else:
			pass
			# If we run out of ammo, we must,
			# prioritize ammo collection until we have 3 bombs

		return action


	def _find_path_to_location(self, location):
		pass

	def _get_matrix(self, game_state):
		# get matrix from here https://www.notion.so/Tips-Tricks-and-Resources-f494e36372df44368f1d8b04e41038c5
		cols = game_state.size[0]
		rows = game_state.size[1]

		game_map = np.zeros((rows, cols)).astype(str)

		for x in range(cols):
			# print(f"x: {x}")
			for y in range(rows):
				entity = game_state.entity_at((x,y))

				if entity is not None:
					game_map[y][x] = entity
				else:
					game_map[y][x] = 9      # using 9 here as 'free' since 0 = Player 1 whaaaat
	
		return game_map

	def _get_direction_of_location(self, location):

		# see where the tile is relative to our current location
		diff = tuple(x-y for x, y in zip(self.location, tile))

		# return the action that moves in the direction of the tile
		if diff == (0,1):
			action = 'd'
		elif diff == (1,0):
			action = 'l'
		elif diff == (0,-1):
			action = 'u'
		elif diff == (-1,0):
			action = 'r'
		else:
			action = ''

		return action

	def _get_next_move(self, location):
		pass
