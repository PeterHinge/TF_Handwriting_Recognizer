def Draw():
    import pygame
    import numpy as np

    """Initializing Pygame."""
    pygame.init()

    """Title of window."""
    pygame.display.set_caption('Pygame Draw')

    """Binary color setup."""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    """Interface parameters setup"""
    screen = pygame.display.set_mode((112, 112))
    screen.fill(WHITE)
    mouse = pygame.mouse

    """Drawing interface."""
    program_exit = False
    while not program_exit:
        left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_exit = True
            elif left_pressed:
                pygame.draw.circle(screen, BLACK, (pygame.mouse.get_pos()), 5)
        pygame.display.update()

    """Grabs a 2d array of the pixels of the drawing interface."""
    screen_array = pygame.surfarray.pixels2d(screen)

    """Modifying the array (from 112x112 to 28x28 pixels) and turning it into a 1d list."""
    lst = []
    row_col_num = [i for i in range(1, 29)]
    for j in row_col_num:
        for i in row_col_num:
            lst.append((1 - (sum(sum(screen_array[i*4-4:i*4, j*4-4:j*4])) / 16 / 16777215)))

    """Turning the list into a np.array and reshape it into a 2d 28x28 array (desired output)."""
    array = np.array(lst)
    new_array = np.reshape(array, (28, 28))

    """Quitting Pygame."""
    pygame.quit()

    return new_array

