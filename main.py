
# Pip install pygame
import pygame
import random
pygame.init()

# Colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0, 255, 0)


# creating window
screen_width = 900
screen_hiegth = 600
gameWindow = pygame.display.set_mode((screen_width,screen_hiegth))

# game title
pygame.display.set_caption("Snake game by Aashir")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def score_on_screen(score,colour,x,y):
    Score_on_sreen = font.render(score,True,colour)
    gameWindow.blit(Score_on_sreen,[x,y])

def plot_snake(gameWindow, black ,snake_list, snake_size):

    for x,y in snake_list:
        pygame.draw.rect(gameWindow,black,[x,y,snake_size,snake_size])

def game_loop():
    
# game specific veriable
    exit_game = False
    game_over = False
    snake_x = 60
    snake_y = 60
    velocity_x = 0
    velocity_y = 0
    int_velocity = 10
    score = 0
    circle_x = random.randint(10,screen_width)
    circle_y = random.randint(10,screen_hiegth)
    snake_size = 25
    food_x = circle_x + snake_size // 2
    food_y = circle_y + snake_size // 2
    radius = snake_size // 2
    fps = 30
    
    snake_list = []
    snake_length = 1


    #game Loop
    while not exit_game:
        if game_over:
            gameWindow.fill(green)
            score_on_screen("Game Over! Press Enter to Continue", red,135,235)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:      
                    if event.key == pygame.K_RIGHT:
                        velocity_x += int_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x -=int_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y -=int_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y +=int_velocity
                        velocity_x = 0       
            
            snake_x +=velocity_x
            snake_y +=velocity_y

            if abs (snake_x-food_x)<15 and abs (snake_y-food_y)<15:
                score+=1
                food_x = random.randint(30,screen_width)
                food_y = random.randint(30,screen_hiegth)
                snake_length += 1

            gameWindow.fill(green)
            score_on_screen("score: "+ str(score),red,5,5)
            pygame.draw.circle(gameWindow, red, (food_x, food_y), radius)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]
            
            if head in snake_list[:-1]:
                game_over = True

            if snake_x<=0 or snake_x>=screen_width or snake_y<=0 or snake_y>=screen_hiegth:
                game_over=True
              
            plot_snake(gameWindow, black ,snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

game_loop()