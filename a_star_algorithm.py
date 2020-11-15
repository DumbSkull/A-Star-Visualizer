import math
from os import close
from queue import PriorityQueue

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]  # example grid ^^

MAX_VALUE = 999999


def find_if_coordinates_in_list(list, coordinates):
    for x in list:
        if x.current_position == coordinates:
            return True
    return False


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

    def return_node_with_coordinates(list, coordinates):
        for x in list:
            if x.current_position == coordinates:
                return x

    open_list = []
    close_list = []

    first_block = Block(current_position=start_position,
                        parent_position=(-1, -1), g_value=0)

    open_list.append(first_block)

    while not len(open_list) == 0:
        # getting and popping the node with the smallest f-value:
        current_node = find_least_f(open_list)
        # print("current_node: ",
        #      current_node.current_position[0], current_node.current_position[1])
        open_list.remove(current_node)

        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for neighbour in neighbours:
            position = (current_node.current_position[0] + neighbour[0],
                        current_node.current_position[1] + neighbour[1])
            #print("neighposition before: ", position[0], position[1])
            # skip if the area is blocked, ie, the grid is 1
            if grid[position[0]][position[1]] == 1:
                continue

            if end_position == position:
                close_list.append(
                    Block(position, current_node.current_position, current_node.g_value+1))
                open_list.clear()
                break
            # checking if out of boundary:
            if(position[0] < 0 or position[0] > len(grid) or position[1] < 0 or position[1] > len(grid[0]) or (position[0] == current_node.current_position[0] and position[1] == current_node.current_position[1])):
                continue
            #print("neighposition: ", position[0], position[1])
            # checking if not in open list or closed list:
            current_position_node = Block(
                position, current_node.current_position, current_node.g_value+1)
            if not find_if_coordinates_in_list(open_list, position) and not find_if_coordinates_in_list(close_list, position):
                open_list.append(current_position_node)

            elif not find_if_coordinates_in_list(open_list, position) and find_if_coordinates_in_list(close_list, position):
                prev_occured_node = return_node_with_coordinates(
                    close_list, position)
                if prev_occured_node.f_value > current_position_node.f_value:
                    close_list.remove(prev_occured_node)
                    close_list.append(current_position_node)

            elif find_if_coordinates_in_list(open_list, position) and not find_if_coordinates_in_list(close_list, position):
                prev_occured_node = return_node_with_coordinates(
                    open_list, position)
                if prev_occured_node.f_value > current_position_node.f_value:
                    open_list.remove(prev_occured_node)
                    open_list.append(current_position_node)

            # also make conditions to check if area is blocked or not
        close_list.append(current_node)
        # print("open_list: ")
        # for x in close_list:
        #     print("position: ", x.current_position[0], x.current_position[1],
        #           "parent: ", x.parent_position[0], x.parent_position[1])
    print("close_list: ")
    for x in close_list:
        print("position: ", x.current_position[0], x.current_position[1],
              "parent: ", x.parent_position[0], x.parent_position[1])

    return close_list


def traversal_list_from_close_list(close_list, start_position, end_position):
    if not find_if_coordinates_in_list(close_list, end_position):
        print("Couldn't find a destination! ")
        return []
    next_coordinates = end_position
    traversal_stack = []
    while next_coordinates != (-1, -1):
        for x in close_list:
            if x.current_position == next_coordinates:
                traversal_stack.append(x)
                close_list.remove(x)  # this is for optimization
                next_coordinates = x.parent_position
    return traversal_stack


close_list = A_Star_Algorithm(grid, (0, 0), (5, 5))
traversal_stack = traversal_list_from_close_list(close_list, (0, 0), (5, 5))


print()
while not len(traversal_stack) == 0:
    last = traversal_stack.pop()
    grid[last.current_position[0]][last.current_position[1]] = 2
