import pygame

pygame.init() 

screen_width = 500
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("C:\\Users\\heejo\\Desktop\\희주코딩\\background.png")
pygame.display.set_caption('justgame')

character = pygame.image.load("C:\\Users\\heejo\\Desktop\\코딩\\929fd0c5ed77d3b.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height
to_x = 0
to_y = 0
character_speed = 1

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
            elif event.key == pygame.K_UP:
                to_y -= 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K.LEFT or event.key == pygame.K.RIGHT:
                to_x = 0
            if event.key == pygame.K.DOWN or event.key == pygame.K.UP:
                to_y = 0
    character_x_pos += to_x *60
    character_y_pos -= to_x *60

    screen.blit(background, (0,0))
    pygame.display.update()

    if character_x_pos < 0:
        character_x_pos = 0
    
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

pygame.quit()
