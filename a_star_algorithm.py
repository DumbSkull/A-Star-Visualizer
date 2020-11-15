import math
from queue import PriorityQueue

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]  # example grid ^^

MAX_VALUE = 999999


def A_Star_Algorithm(grid, start_position, end_position):

    # g-value is the least number of steps taken to reach the current node
    # h-value is the heuristic value (the euclidean distance from the current node to the end node)

    # defining each block to contain informations regarding it's position,
    # it's parents' position, its g-value, and its h-value
    class Block():
        def __init__(self, current_position=(-1, -1), parent_position=(-1, -1), g_value=MAX_VALUE):
            self.current_position = current_position
            self.parent_position = parent_position
            self.g_value = g_value
            self.h_value = math.sqrt(math.pow(current_position[0]-end_position[0], 2) + math.pow(
                current_position[1]-end_position[1], 2))  # heuristic function
            self.f_value = self.g_value + self.h_value

    def find_least_f(list):
        smallest = list[0]
        for x in list[1:]:
            if x.f_value < smallest.f_value:
                smallest = x
        return smallest

    def find_if_coordinates_in_list(list, coordinates):
        for x in list:
            if x.current_position == coordinates:
                return True
        return False

    open_list = []
    close_list = []

    first_block = Block(current_position=(
        0, 0), parent_position=(-1, -1), g_value=0)

    open_list.append(first_block)

    while not len(open_list) == 0:
        # getting and popping the node with the smallest f-value:
        current_node = find_least_f(open_list)
        open_list.remove(current_node)

        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for neighbour in neighbours:
            position = (current_node.current_position[0] + neighbour[0],
                        current_node.current_position[1] + neighbour[0])
            if(position[0] < 0 or position[0] > len(grid) or position[1] < 0 or position[1] > len(grid[0])):
                continue
            if not find_if_coordinates_in_list(open_list, position) and not find_if_coordinates_in_list(close_list, position):
                # open_list.append(
                #   Block(position, current_node.current_position, current_node.g_value+1))


A_Star_Algorithm(grid, (0, 0), (5, 5))
