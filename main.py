import math
import pygame
import random
import button

# this init line is mandatory
pygame.init()

# highscores
highscore = []


def game_loop():
    screen = pygame.display.set_mode((800, 600))
    back_ground = pygame.image.load('maxresdefault.png')
    game_over = pygame.image.load('gameover.png')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('freestanding.ttf', 100)
    counter = 30
    text_x = 0
    text_y = 0
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)

    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('galaxy.png')
    pygame.display.set_icon(icon)


    def show_timer(x, y):
        timer = font.render(str(counter), True, (0, 128, 0))
        screen.blit(timer, (0, 0))

    meteor_img = []
    met_x = []
    met_y = []
    num_of_met = 6
    for i in range(num_of_met):
        meteor_img.append(pygame.image.load('asteroid.png'))
        met_x.append(random.randint(10, 700))
        met_y.append(random.randint(10, 480))

    def meterorite(x, y, i):
        screen.blit(meteor_img[i], (x, y))

    player_img = pygame.image.load('spaceship.png')
    player_x = 380
    player_y = 500
    player_x_change = 0
    player_y_change = 0

    def player(x, y):
        screen.blit(player_img, (x, y))

    enemy_img = pygame.image.load('spaceship (1).png')
    enemy_x = random.randint(0, 730)
    enemy_y = 50
    enemy_x_change = 15
    enemy_y_change = 10

    def enemy(x, y):
        screen.blit(enemy_img, (x, y))

    def isCollision(a, b, c, d):
        distance = math.sqrt((math.pow(a - c, 2)) +
                             (math.pow(b - d, 2)))
        if distance < 30:
            return True
        else:
            return False

    # score
    score_value = 0
    font = pygame.font.SysFont('freestanding.ttf', 50)

    text_X = 600
    text_Y = 0

    def show_score(x, y):
        score = font.render("Score : " +
                            str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    # Game Loop
    running = True
    while running:
        clock.tick(20)
        screen.fill((93, 151, 251))
        screen.blit(back_ground, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -13
                if event.key == pygame.K_RIGHT:
                    player_x_change = 13
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_y_change = -13
                if event.key == pygame.K_DOWN:
                    player_y_change = 13
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_y_change = 0
            if event.type == timer_event:
                counter -= 1
                text = font.render(str(counter), True, (0, 128, 0))
                if counter == 0:
                    pygame.time.set_timer(timer_event, 0)
                    highscore.append(score_value)
                    pygame.time.wait(3000)
                    running = False
        show_timer(text_x, text_y)
        show_score(text_X, text_Y)
        player_x += player_x_change
        if player_x <= 0:
            player_x = 0
        elif player_x >= 730:
            player_x = 730
        player_y += player_y_change
        if player_y <= 0:
            player_y = 0
        elif player_y >= 500:
            player_y = 500

        enemy(enemy_x, enemy_y)
        enemy_x += enemy_x_change
        enemy_y += enemy_y_change
        if enemy_x <= 0:
            enemy_x = 13
        elif enemy_x >= 736:
            enemy_x = -13

        if enemy_y <= 0:
            enemy_y_change = 10
        elif enemy_y >= 400:
            enemy_y_change = -10
        player(player_x, player_y)
        for i in range(num_of_met):
            meterorite(met_x[i], met_y[i], i)
            if isCollision(met_x[i], met_y[i], player_x, player_y):
                score_value += 1
                met_x[i] = random.randint(10, 600)
                met_y[i] = random.randint(10, 350)

        collision = isCollision(enemy_x, enemy_y, player_x, player_y)
        if collision:
            pygame.time.wait(3000)
            highscore.append(score_value)
            running = False
        # mandatory to update screen
        pygame.display.update()
    return running


def game_over():
    screen = pygame.display.set_mode((800, 600))
    gameover = pygame.image.load('gameover.png')

    run = True
    while run:
        screen.fill((93, 151, 251))
        screen.blit(gameover, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()


def show_highscore():
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont('freestanding.ttf', 100)

    run = True
    while run:
        screen.fill((93, 151, 251))
        scoreee = font.render("Score", True, (255, 255, 255))
        screen.blit(scoreee, (300, 5))
        for element in range(len(highscore)):
            High_score = font.render(str(highscore[element]), True, (255, 255, 255))
            screen.blit(High_score, (350, 80 + (element * 100)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

def main_menu():
    screen = pygame.display.set_mode((800, 600))
    back_ground = pygame.image.load('maxresdefault.png')
    start_img = pygame.image.load('start.png')
    exit_img = pygame.image.load('exit.png')
    score_img = pygame.image.load('customer-satisfaction_9375636.png')
    start = button.Button(250, 50, start_img)
    exit = button.Button(250, 300, exit_img)
    score = button.Button(680, 500, score_img)
    run = True

    while run:
        screen.fill((93, 151, 251))
        start.draw()
        exit.draw()
        score.draw()
        if start.draw():

            if not game_loop():
                game_over()
        if exit.draw():
            run = False
        if score.draw():
            show_highscore()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


if __name__ == '__main__':
    main_menu()
