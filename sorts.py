import pygame, random

pygame.init()
screen = pygame.display.set_mode((40, 40))
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Sorter")

ball_on_screen = []
width = 20
radius = 20


class Ball:
    def __init__(self, j):
        self.color = 0
        self.size = 10
        self.x = setagridspace(j)
        self.y= 100
        
        
def setagridspace(space):
    positions = [45, 90, 135, 180, 225, 270, 315, 360, 405, 450]
    x = positions[space]
    return x


def createBall():
    ball = Ball(len(ball_on_screen)) 
    ball.color = random.randint(1, 255)
    ball.rect = pygame.draw.circle(win, ball.color, (ball.x, ball.y), radius, width)
    return ball

def bubble():
    run = True
    temp = []
    for i in ball_on_screen:
        temp.append(i.color)
    returnvalue = []
    while run:
        if len(temp) != 0:
            value = 0
            for k in temp:
                if k > value:
                    value = k
            returnvalue.append(value)
            temp.remove(value)   
        else:
            run = False
            return returnvalue
          
def Main():
    run = True
    win.fill((255, 255, 255))
    while run:
        pygame.time.delay(100)
        card_on_screen = []
        for event in pygame.event.get():
            ev = pygame.event.get()
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if len(ball_on_screen) < 10:
                ball = createBall()
                ball_on_screen.append(ball)
                pygame.display.update()
        
        if keys[pygame.K_b]:
            bubbled = bubble()
            win.fill((255, 255, 255))
            for k in bubbled:
                b = setagridspace(bubbled.index(k))
                ball = pygame.draw.circle(win, k, (b, 100), radius, width)
                pygame.display.update()
            

Main()
pygame.quit()




