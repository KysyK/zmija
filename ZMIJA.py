import random#fkfkfkkf

import pygame

pygame.init()
win_width = 500
win_height = 500
FPS = 3
back = (154, 205, 50)
mw = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
kybeks = pygame.sprite.Group()

class Apple:
    def __init__(self, image, x, y, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def teleport(self):
        self.rect.x = random.randint(0, (win_width - self.rect.width) // self.rect.width) * self.rect.width
        self.rect.y = random.randint(0, (win_height - self.rect.height) // self.rect.height) * self.rect.height

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Snake:
    def __init__(self, x, y, size, color=(200, 100, 255)):
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.color = color
        self.last_pos = [x, y]
        self.direction = 'right'
        self.step = size

    def goto(self, x, y):
        self.last_pos = [self.rect.x, self.rect.y]
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        pygame.draw.rect(mw, self.color, self.rect)


class Kubek(pygame.sprite.Sprite):
    def __init__(self, image, size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (size, size))
        self.rect = self.image.get_rect()
        self.teleport()

    def teleport(self):
        self.rect.x = random.randint(0, (win_width - self.rect.width) // self.rect.width) * self.rect.width
        self.rect.y = random.randint(0, (win_height - self.rect.height) // self.rect.height) * self.rect.height

    def reset(self):
        mw.blit(self.image, self.rect)


SIZE = 25
delay = 200
snakes = []
apple = Apple('JABLYKO.jpg', 0, 0, SIZE, SIZE)
apple.teleport()
head = Snake(100, 100, SIZE, color=(100, 100, 100))
snakes.append(head)
scores = 0
q = pygame.font.SysFont("Arial", 20)
score_text = q.render(str(scores), True, (100, 100, 100))
scores_label = q.render("RAXYNOK", True, (100, 100, 100))


def move(x, y):
    lx, ly = x, y
    for w in snakes:
        w.goto(lx, ly)
        lx, ly = w.last_pos[0], w.last_pos[1]


run = True
while run:
    pygame.time.delay(delay)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:

                if head.direction != 'DOWN':
                    head.direction = 'up'
                    break
            elif event.key == pygame.K_s:
                if head.direction != 'up':
                    head.direction = 'DOWN'
                    break
            elif event.key == pygame.K_a:
                if head.direction != 'right':
                    head.direction = 'left'
                    break
            elif event.key == pygame.K_d:
                if head.direction != 'left':
                    head.direction = 'right'
                    break
    if head.direction == 'up':
        move(head.rect.x, head.rect.y - head.step)
    if head.direction == 'DOWN':
        move(head.rect.x, head.rect.y + head.step)
    if head.direction == 'right':
        move(head.rect.x + head.step, head.rect.y)
    if head.direction == 'left':
        move(head.rect.x - head.step, head.rect.y)

    if apple.rect.colliderect(head.rect):
        kybek = Kubek("Kybasik.png", SIZE)
        kybeks.add(kybek)
        scores += 1
        score_text = q.render(str(scores), True, (100, 100, 100))
        apple.teleport()
        last_pos = snakes[-1].last_pos
        snakes.append(Snake(last_pos[0], last_pos[1], SIZE))
    mw.fill(back)
    apple.draw()
    kybeks.draw(mw)
    mw.blit(score_text, (100, 0))
    mw.blit(scores_label, (0, 0))
    for snake in snakes:
        if head.rect.colliderect(snake.rect) and snakes.index(snake) >= 2:
            text = pygame.font.SysFont("Arial", 50).render("YOU LOSE", True, (0, 0, 0))
            mw.blit(text, (200, 200))
            snake.color = (250, 100, 100)
            run = False
        snake.draw()
    if head.rect.y + head.rect.height > win_height or head.rect.y < 0 or head.rect.x + head.rect.width > win_width or head.rect.x < 0:
        text = pygame.font.SysFont("Arial", 50).render("YOU LOSE", True, (0, 0, 0))
        mw.blit(text, (200, 200))
        run = False
    if pygame.sprite.spritecollide(head,kybeks,False):
        text = pygame.font.SysFont("Arial", 50).render("YOU LOSE", True, (0, 0, 0))
        mw.blit(text, (200, 200))
        run = False
    pygame.display.update()
