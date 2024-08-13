import pygame
pygame.init()
running = True
screen = pygame.display.set_mode((500,500))
head = pygame.image.load(r"images\snake_head_updated.png")
body = pygame.image.load(r"images\snake_body_updated.png")
bush = pygame.image.load(r"images\bush_updated.png")
position = (screen.get_width()//2, screen.get_height()//2)
clock = pygame.time.Clock()

snake = [
    pygame.rect.Rect(position[0],position[1],10,10),
    pygame.rect.Rect(position[0]-body.get_width(),position[1],10,10),
    pygame.rect.Rect(position[0]-2 * body.get_width(),position[1],10,10)
]

def render(img, snake):
    head_img = pygame.transform.rotate(head, 0)
    screen.blit(head_img, snake[0].topleft)
    for segment in snake[1:]:
        screen.blit(img, segment.topleft)

def move(snake):
    for segment in snake:
        segment.x += body.get_width()

def draw_bush(bush_img):
    bush_width = bush_img.get_width()
    img = pygame.transform.rotate(bush_img, 180)
    for i in range(screen.get_width()//bush_width):
        screen.blit(img, (i*bush_width, 1))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("dark gray")
    move(snake)
    render(body, snake)
    draw_bush(bush)
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
