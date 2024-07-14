import pygame
import config
from food import Food
from snack import Snack
from render import Render

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((config.WIDTH, config.HIGHT))
        pygame.display.set_caption("Snack Game")
        self.clock = pygame.time.Clock()
        self.snack = Snack(config.BLOCK_SIZE, config.WIDTH//2, config.HIGHT//2)
        self.food = Food(self.snack.body)
        self.render = Render(self.screen)
        self.running = True
        self.score = 0


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    self.handle_key_pressed(event.key)
            # draw background
            self.render.draw_background()
            # move the snack
            self.snack.move()
            # check if snack eat food
            if self.did_eat():
                self.score += 1
                self.food.position = self.food.create(self.snack.body)
            else:
                self.snack.remove_tail()

            # collision detection
            self.did_collied()

            # draw snack
            self.render.draw_snack(self.snack)
            # draw food
            self.render.draw_food(self.food)
            # set score
            self.render.draw_score(self.score)

            # check if game is over
            if not self.running:
                self.render.draw_game_over()
                pygame.display.flip()
                pygame.time.wait(3000)

            pygame.display.flip()
            self.clock.tick(config.SPEED)
        pygame.quit()

    def handle_key_pressed(self, key):
        if key == pygame.K_UP and self.snack.direction != "down":
            self.snack.direction = "up"
        elif key == pygame.K_DOWN and self.snack.direction != "up":
            self.snack.direction = "down"
        elif key == pygame.K_LEFT and self.snack.direction != "right":
            self.snack.direction = "left"
        elif key == pygame.K_RIGHT and self.snack.direction != "left":
            self.snack.direction = "right"
    
    def did_eat(self):
        if self.snack.head[0] == self.food.position[0] and self.snack.head[1] == self.food.position[1]:
            return True
    
    def did_collied(self):
        head = self.snack.body[0]
        if ((head[0] <0 or head[0]>=config.WIDTH) or
        (head[1]<0 or head[1]>=config.HIGHT) or
        head in self.snack.body[1:]):
            self.running = False
