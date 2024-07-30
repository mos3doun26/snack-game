import pygame
import config
from food import Food
from snake import snake
from render import Render
import config

class Game:
    def __init__(self):
        # load images
        self.background_img = pygame.image.load(config.background_img)
        self.snake_head_img = pygame.image.load(config.snake_head_img)
        self.snake_body_img = pygame.image.load(config.snake_body_img)
        self.food_img = pygame.image.load(config.food_img)
        # seting screen
        self.screen = pygame.display.set_mode((config.WIDTH, config.HIGHT))
        pygame.display.set_caption("snake Game")
        # create elements
        self.clock = pygame.time.Clock()
        self.snake = snake(self.snake_head_img, self.snake_body_img,config.BLOCK_SIZE, config.WIDTH//2, config.HIGHT//2)
        self.food = Food(self.food_img,self.snake)
        self.render = Render(self.screen)
        self.running = True
        self.score = 0
        
    def run(self):
        while self.running:
            self.handle_events()
            # draw background
            self.render.draw_background(self.background_img)
            # move the snake
            self.snake.move()
            # check if snake eat food
            if self.did_eat():
                self.score += 1
                self.food.position = self.food.create(self.snake)
            else:
                self.snake.remove_tail()
            # draw snake
            self.render.draw_snake(self.snake)
            # draw food
            self.render.draw_food(self.food)
            # set score
            self.render.draw_score(self.score)
            # check wall collisions
            self.check_collions_happend()
            
            # check if game is over
            self.check_game_over()

            pygame.display.flip()
            self.clock.tick(config.SPEED)
        pygame.quit()

    def handle_key_pressed(self, key):
        if key == pygame.K_UP and self.snake.direction != "down":
            self.snake.direction = "up"
        elif key == pygame.K_DOWN and self.snake.direction != "up":
            self.snake.direction = "down"
        elif key == pygame.K_LEFT and self.snake.direction != "right":
            self.snake.direction = "left"
        elif key == pygame.K_RIGHT and self.snake.direction != "left":
            self.snake.direction = "right"
    
    def did_eat(self):
        if (self.snake.head.colliderect(self.food.position)):
            return True

    def check_collions_happend(self):
        if self.did_collied():
            self.running = False
    
    def check_game_over(self):
        if not self.running:
            self.running = False
            self.render.draw_game_over()
            pygame.display.flip()
            pygame.time.wait(3000)
 
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_key_pressed(event.key)

    def did_collied(self):
        bush_width = 20
        bush_height = 20
        return(
            self.snake.head.left <  bush_width
            or self.snake.head.right > self.screen.get_width()-self.snake.head.width
            or self.snake.head.top < bush_height
            or self.snake.head.bottom > self.screen.get_height() - self.snake.head.height
            # or self.snake.head in self.snake.body[1:]
        )

game = Game()
print(game.food_img.get_width())