import pygame
windows_width =800
windows_height =500

# init screen
pygame.init()
size = (windows_width, windows_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game')
# fill sceeen ans show
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREY = (182,182,182)
PINK= (255,20,147)
screen.fill(GREY)
pygame.mouse.set_visible(False) # hide the mouse
pygame.display.flip()

#  set mouse keywords
LEFT =1
SCROLL = 2
RIGHT = 3

#setting sound files
pygame.mixer.init()
SOUND_FILE = 'C:\\Users\\eranra\\Documents\\PY\OOP\\scifi-weapon.mp3'
SOUND_FILE_RIGHT = 'C:\\Users\\eranra\\Documents\\PY\OOP\\vibrating-wobble.mp3'

finish = False
IMAGE = 'C:\\Users\\eranra\\Documents\\PY\OOP\\logo.jpg'


img = pygame.image.load(IMAGE)
screen.blit(img,(0,0)) ##0,0 - location on top left
#pygame.draw.line(screen, BLACK, [160,490],[660,490], width =1)
player_image = pygame.image.load('C:\\Users\\eranra\\Documents\\PY\OOP\\airplane.png').convert()
player_image.set_colorkey(PINK)
screen.blit(player_image,[220,300])
pygame.display.flip()

clock = pygame.time.Clock()
refresh_rate = 60


mouse_pos_list =[]
# ball_x_pos = 0
# ball_y_pos = 0
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            mouse_pos_list.append(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
            pygame.mixer.music.load(SOUND_FILE_RIGHT)
            pygame.mixer.music.play()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: # pressing a
                pygame.mixer.music.load(SOUND_FILE)
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                mouse_pos_list.clear()






    screen.blit(img,(10,10))
    mouse_point = pygame.mouse.get_pos()
    screen.blit(player_image, mouse_point)

    for loc in mouse_pos_list:
        screen.blit(player_image, loc)
    pygame.display.flip()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            mouse_point = pygame.mouse.get_pos() 
            new_mouse_point = (mouse_point[1], mouse_point[1] +100)
            screen.blit(player_image, new_mouse_point)
        pygame.display.flip()

    clock.tick(refresh_rate)