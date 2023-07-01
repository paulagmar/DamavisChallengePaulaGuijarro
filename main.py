# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:43:06 2023

@author: PaulaGuijarroMartinez
"""
# Call test function. In order to test the code with other labyrinth, change testLabyrinth function
from testLabyrinth import testLabyrinth

# ==========DEINE NECESSARY FUNCTIONS=======
def isPositionBlocked(labyrinth, orientation, head):
    # INFO: Function to check if the cells are blocked or out of range

    rows = len(labyrinth)
    columns = len(labyrinth[0])
    x, y = head[0], head[1] # head coordinates to check if blocked or not

    # 1. Check orientation and see if all cells that would occupy are free
    if orientation == 'horizontal':
        if (x < 0) or (y < 0) or (x >= rows) or (y-2 < 0) or (y >= columns): # see if it is out of range 
            return False
        if (labyrinth[x][y] != '.') or (labyrinth[x][y - 1] != '.') or (labyrinth[x][y - 2] != '.'): # see if the rod is in a blocked cell
            return False
    else:
        if (x < 0) or (y < 0) or (x - 2 < 0) or (x >= rows) or (y >= columns):
            return False
        if (labyrinth[x][y] != '.') or (labyrinth[x - 1][y] != '.') or (labyrinth[x - 2][y] != '.'):
            return False

    return True


def canChangeOrientation(labyrinth, orientation, head): 
    # INFO: Function to check if all cells in 3x3 range are available or blocked
    rows = len(labyrinth)
    cols = len(labyrinth[0])

    # Check if head is out of bounds
    if head[0] < 0 or head[0] >= rows or head[1] < 0 or head[1] >= cols:
        return False

    # center of the rod depending on the head position and its orientation
    center = [head[0] - 1, head[1]]
    if (orientation == 'horizontal'):
        center = [head[0], head[1] - 1]

    else:
        return False
    
    # check if surrounding cells are blocked or out of limits
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if (center[0] + x < 0 or center[1] + y < 0):
                return False
            if (center[0] + x >= len(labyrinth) or center[1] + y >= len(labyrinth[0])):
                return False
            if labyrinth[center[0] + x][center[1] + y] != '.':
                return False
    return True


def getNewPositions(labyrinth, orientation, head):
    # INFO: Funtion to get all possible positions after moving up, down, left or righ
    positions = []
    x, y = head[0], head[1] # head coordinates
    
    # 1. Get all possible new heads (up, down, right, left)
    new_heads = [[x - 1, y],
            [x + 1, y],
            [x, y - 1],
            [x, y + 1]] # possible cells the head would be after moving
    
    # 2. Filter the ones that are blocked or out of limits
    for new_head in new_heads:
        if (isPositionBlocked(labyrinth, orientation, new_head)):
            positions.append({'orientation': orientation, 'head_position': new_head})
            
    # 3. Add possitions if rotation is possible too
    if canChangeOrientation(labyrinth, orientation, head): # add change orientation if it is legal
        if orientation =='horizontal':
            pos = {'orientation': 'vertical', 'head_position': [head[0] + 1, head[1] - 1]}
        else:
            pos = {'orientation': 'horizontal', 'head_position': [head[0] - 1, head[1] + 1]}
        positions.append(pos)
        
    return positions


# =========INITIALIZATION============
test_number = int(input('Select a test from 1 to 4: ')) # user select a test from 1-4
labyrinth = testLabyrinth(test_number)
    
# 1. Position of the start and end of the labyrinth
start = {'orientation': 'horizontal', 'head_position': [0, 2]} # start at the head 
end = [len(labyrinth) - 1, len(labyrinth[0]) - 1] # end at the botton right corner

# 2. Positions already seen (for not returning back)
visitedPositions = {'horizontal': [[0, 2]], 'vertical': []}

# 3. While loop: until we reached the end of the labyrinth or no more path possibilities are left
steps = 0
reached_goal = False
possible_paths = [start]


# ================MAIN LOOP=====================
while (not reached_goal):
    steps += 1
    new_paths = []
    
    # 1. Analyze all possible paths 
    
    for path in possible_paths:
        
        # 2. For each possible new cell calculate the new paths
        newPositions = getNewPositions(labyrinth, path['orientation'], path['head_position'])
        
        # 3. Check if it has reached the goal
        for position in newPositions:
            if position['head_position'] == end:
                reached_goal = True
            
            # avoid moving in circles
            if position['head_position'] in visitedPositions[position['orientation']]:
                continue
            
            new_paths.append(position)
            visitedPositions[position['orientation']].append(position['head_position'])
            
    possible_paths = new_paths
    
    # 4. If there are no more possible paths
    if len(possible_paths) == 0:
        steps = -1
        reached_goal = True
            
            
# ======Display the results=======
if steps != -1:
    print(f"Number of moves required: {steps}")
else:
    print(f"No valid path exists. Movements: {steps}")





















