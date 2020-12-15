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

class Node: # For Breadth First Search
	def __init__(self, point, dist):
		self.point = point
		self.dist = dist

class Agent:

	def __init__(self):
		'''
		Place any initialisation code for your agent here (if any)
		'''
		# a list of all the actions your Agent can choose from
		self._actions = ['', 'u', 'd', 'l','r','p']
		self._ROW = 10
		self._COL = 12

	def next_move(self, game_state, player_state):

		self._my_id = player_state.id # Getting my id

		# test how long it takes to construct game map
		start_time = time.time()
		self._map = self._get_matrix(game_state)
		end_time = time.time()
		print(f"Time to construct game_map:  {end_time - start_time:.10f}") 
		# about 1/10th of a tick? ~ 0.0005 seconds (depends on system)

		## Agressive Bot Code ##
		self._game_state = game_state
		opponent_location = game_state.opponents(self._my_id)

		if player_state.ammo >= 1:
			# Find a path to the opponent's location and travel toward it
			# if and when we are within range of placing a bomb, we must place the bomb
			# then as we wait for it to explode we must pick up bombs that are
			# in close vacinity of the opponent.


			action = self._get_next_move(opponent_location)
			s = [[str(e) for e in row] for row in self._find_path_to_location(
														player_state.location,
														opponent_location[1])]
			table = [ "\t".join(x) for x in s]
			print ('\n'.join(table))

		else:
			pass
			# If we run out of ammo, we must,
			# prioritize ammo collection until we have 3 bombs

		return action

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


	def _isValid(self, row: int, col: int):
		return self._game_state.is_in_bounds((row, col)) and (self._game_state.entity_at((row, col)) not in ["ib", "sb", "ob", "b"])

	def _find_path_to_location(self, from_loc, to_loc):
		visited = [[False for i in range(self._COL)] for j in range(self._ROW)]
		distance_mat = [[-1 for i in range(self._COL)] for j in range(self._ROW)]
		print(from_loc)
		print(to_loc)
		visited[from_loc[1]][from_loc[0]] = True
		distance_mat[from_loc[1]][from_loc[0]] = 0
		q = deque()
		rowNum = [-1, 0, 0, 1]
		colNum = [0, -1, 1, 0]
		s = Node(from_loc, 0)
		q.append(s)

		while q:
			curr = q.popleft()

			pt = curr.point
			if pt[0] == to_loc[0] and pt[1] == to_loc[1]:
				distance_mat[to_loc[1]][to_loc[0]] = -2
				return (distance_mat, curr.dist)

			for i in range(4):
				row = pt[1] + rowNum[i]
				col = pt[0] + colNum[i]

				if (self._isValid(col, row) and not visited[row][col]):
					visited[row][col] = True
					adj_cell = Node((col, row), curr.dist + 1)
					distance_mat[row][col] = adj_cell.dist
					q.append(adj_cell)
		return -1


	def _get_direction_of_location(self, location, tile):

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
		return ""
