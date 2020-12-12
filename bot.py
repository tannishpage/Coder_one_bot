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
		## Agressive Bot Code ##
		opponent_location = game_state.opponents(self._my_id)

		if player_state.ammo >= 1:
			# Find a path to the opponent's location and travel toward it
			# if and when we are within range of placing a bomb, we must place the bomb
			# then as we wait for it to explode we must pick up bombs that are
			# in close vacinity of the opponent.

			action = self._get_next_move()
		else:
			# If we run out of ammo, we must,
			# prioritize ammo collection until we have 3 bombs

		return action


	def _find_path_to_location(self, location):
		pass

	def _get_matrix_

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
