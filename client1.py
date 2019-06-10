import pygame

from network import  Network

width = 600
height = 600

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Client')

clientnumber = 0


class Player():
    def __init__(self,x,y,width, height, color):
        self.x = x
        self.y = y
        #print(self.y,y)
        self.height = height
        self.width = width
        self.color = color
        self.rect = (x,y,width, height)
        self.vel = 1

    def draw(self,screen):
        print(self.rect)
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x,self.y,self.width,self.height)

def read_pos(str):
    str = str.split(',')
    return int(str[0]),int(str[1])

def make_pos(tmp):
    return str(tmp[0]) + ',' + str(tmp[1])


#p2 = Player(0,0,100,100,(0,255,0))
def redrawScreen(screen, p1, p2):
    screen.fill((255,255,255))
    p2.draw(screen)


#def redraw():
#    screen.fill((255,255,255))
    p1.draw(screen)
    pygame.display.update()


def main():
    run = True
    n = Network()

    startpos = read_pos(n.getPod())
    p2 = Player(0, 0, 100, 100, (0, 255, 0))
    p1 = Player(startpos[0], startpos[1], 100, 100, (0, 255, 0))

    while run:
        p2Pos = read_pos(make_pos((p1.x, p1.y)))
        #print('pspos=',p2Pos)
        p2.x ,p2.y = p2Pos
        #print('p2=',p2.x,p2.y)
        p2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p1.move()

        redrawScreen(screen,p1,p2)
main()