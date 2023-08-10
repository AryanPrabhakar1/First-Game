# New Draftt


import pygame
import os
pygame.font.init()
pygame.mixer.init()


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aryan First Game")

WHITE = (255 ,255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

YELLOW = (255, 255, 0)
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

# BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', ""))
# BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', ""))

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

ML_WIDTH, ML_HEIGHT = 70, 90

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# MARIO_IMAGE = pygame.image.load("C:\Users\Administrator\Desktop\Python Practice\Aryan First Game\Mario.png")
MARIO_IMAGE = pygame.image.load("Desktop\Python Practice\Aryan First Game\Mario.png")
MARIO = pygame.transform.rotate(pygame.transform.scale(MARIO_IMAGE, (ML_WIDTH, ML_HEIGHT)), 20)
LUIGI_IMAGE = pygame.image.load("Desktop\Python Practice\Aryan First Game\Luigi.png")
LUIGI = pygame.transform.rotate(pygame.transform.scale(LUIGI_IMAGE, (ML_WIDTH, 120)), -20)
# MARIO_IMAGE = pygame.image.load(os.path.join('Mario.png'))
# LUIGI_IMAGE = pygame.image.load(C:\Users\Administrator\Desktop\Python Practice\Aryan's First Game\Luigi.png)

SPACE_IMAGE = pygame.image.load("Desktop\Python Practice\Spaceship game\space-black-hole-interstellar-planet-wallpaper-preview.jpg")
SPACE = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))

# def draw_window(red, yellow, red_bullets, yellow_bullets):
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0,0))
    
    
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    red_health_text = HEALTH_FONT.render("Luigi: " + str(red_health), 1, "Green")
    yellow_health_text = HEALTH_FONT.render("Mario: " + str(yellow_health), 1, RED)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    WIN.blit(MARIO, (yellow.x, yellow.y))
    WIN.blit(LUIGI, (red.x, red.y))
    
    # red_bullets = []
    # yellow_bullets = []
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
        
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update()
    
def mario_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < WIDTH/2 - 30: 
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 20:
        yellow.y += VEL
            
def luigi_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x + VEL > WIDTH/2:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + red.width + VEL < WIDTH - 20:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 30:
        red.y += VEL
            
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH - 20:
            yellow_bullets.remove(bullet)
             
            
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 20:
            red_bullets.remove(bullet) 
            
def draw_winner(text):
    
    draw_text = WINNER_FONT.render(text, 1, "Blue")
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
            
def main():
    red = pygame.Rect(500, 100, ML_WIDTH, ML_HEIGHT)
    yellow = pygame.Rect(100, 300, ML_WIDTH, ML_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    red_health = 10
    yellow_health = 10
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
                
                
                
# def shoot_bullets(red_bullets, yellow_bullets, red, yellow):
    
#     if keys_pressed[pygame.K_c]:
#         bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 5, 10, 5)
#         yellow_bullets.append(bullet)
        
#     if keys_pressed[pygame.K_m]:
#        bullet = pygame.Rect(red.x, red.y + red.height//2 - 5, 10, 5)
#        red_bullets.append(bullet) 
                
             
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    # BULLET_FIRE_SOUND.play()
                    
                    
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)  
                    # BULLET_FIRE_SOUND.play()
    
            if event.type == RED_HIT:
                red_health -= 1
                 # BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1  
                 # BULLET_HIT_SOUND.play()
        
        winner_text = ""        
        if red_health <= 0:
            winner_text = "Mario Wins!"
            
        if yellow_health <= 0:
            winner_text = "Luigi Wins!"
          
        if winner_text != "":
            # pass #SOMEONE WON
            draw_winner(winner_text)
            break   
     
        print(red_bullets, yellow_bullets)
        
        keys_pressed = pygame.key.get_pressed()
        mario_handle_movement(keys_pressed, yellow)
        luigi_handle_movement(keys_pressed, red)
        
        
        # red.x += 1 
        # yellow.y += 1.5     
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        # shoot_bullets(red_bullets, yellow_bullets, red, yellow)
        
        
        # draw_window(red, yellow, red_bullets, yellow_bullets)
        # draw_window(red, yellow, red_bullets, yellow_bullets)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    main()
     
if __name__ == "__main__":
    main()