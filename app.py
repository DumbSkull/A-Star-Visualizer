import pygame

pygame.init()

main_text = "Select the starting point"

screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("A-Star Path Finding Algorithm")
font = pygame.font.SysFont('arial', 44)

is_start_selected = False
is_end_selected = False
is_obstacles_drawn = False

start_mouse_index = (-1, -1)
end_mouse_index = (-1, -1)
obstacle_mouse_indices = []

while True:
    quit = False
    for event in pygame.event.get():

        # if the event is the QUIT event, ie., the user has clicked 'x' of the window to close:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit = True
            break

        # if the event is that of a mouse click:
        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()

            # if start node hasn't been selected:
            if not is_start_selected:
                x = int(mouse_position[0]/25)
                y = int(mouse_position[1]/25)
                start_mouse_index = (x, y)
                is_start_selected = True
                main_text = "Enter the ending point"

            # if end node hasn't been selected:
            elif not is_end_selected and is_start_selected:
                x = int(mouse_position[0]/25)
                y = int(mouse_position[1]/25)
                end_mouse_index = (x, y)
                is_end_selected = True
                main_text = "Draw the obstacles"

            # if the obstacles haven't been drawn:
            elif not is_obstacles_drawn and is_start_selected and is_end_selected:
                x = int(mouse_position[0]/25)
                y = int(mouse_position[1]/25)
                obstacle_mouse_index = (x, y)
                obstacle_mouse_indices.append(obstacle_mouse_index)

    # if the user has clicked the close button:
    if quit == True:
        break

    # the main text on top (displaying "select start node" etc etc)
    # to clear the background before the text is written
    pygame.draw.rect(screen, (0, 0, 0), [0, 0, 800, 75])
    text = font.render(main_text, True, (235, 207, 196))
    screen.blit(text, (0, 0))

    # drawing the grids:
    for x in range(int(800/25)):
        for y in range(3, int(800/25)):  # starts from 3 to leave space for the text on top

            # if the node is a start node:
            if x == start_mouse_index[0] and y == start_mouse_index[1]:
                pygame.draw.rect(screen, (144, 136, 212), [x*25, y*25, 25, 25])
                continue

            # if the node is an end node:
            elif x == end_mouse_index[0] and y == end_mouse_index[1]:
                pygame.draw.rect(screen, (144, 136, 212), [x*25, y*25, 25, 25])
                continue

            # if the node is is an obstacle:
            elif (x, y) in obstacle_mouse_indices:
                pygame.draw.rect(screen, (229, 218, 203), [x*25, y*25, 25, 25])
                continue

            # if the node is a normal empty node:
            else:
                pygame.draw.rect(screen, (0, 0, 0), [x*25, y*25, 25, 25])
                pygame.draw.rect(screen, (56, 52, 75), [x*25, y*25, 25, 25], 2)

    # updating the pygame display window:
    pygame.display.update()
