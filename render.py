import pygame
import config

class Render:
    def __init__(self, screen):
        self.screen = screen
        self.background = config.COLORS["navy"]
        self.red = config.COLORS["red"]
        self.green = config.COLORS["green"]
        self.white = config.COLORS["white"]
        pygame.font.init()
        self.font = pygame.font.Font(None, 24)


    def draw_background(self, img):
        self.screen.fill(self.background)
        for x in range(self.screen.get_width()//20):
            for y in range(self.screen.get_height()//20):
                self.screen.blit(img,(x*20,y*20))

    def draw_snake(self, snake):
        head_img = self.head_rotation(snake)
        self.screen.blit(head_img,snake.head.topleft)
        for segment in snake.body[1:]:
            self.screen.blit(snake.body_img, segment.topleft)

    def draw_food(self, food):
        self.screen.blit(food.food_img, food.position.topleft)

    def draw_score(self, score):
        text = self.font.render(f"Score: {score}", True, self.white)
        self.screen.blit(text, (10,10))
    
    def draw_game_over(self):
        text = self.font.render("Game over ya habbeby", True, self.white)
        center_x = config.WIDTH//2 - text.get_width()//2
        center_y = config.HIGHT//2-text.get_height()//2
        self.screen.blit(text, (center_x, center_y))


    def head_rotation(self, snake):
        if snake.direction == "left":
            return pygame.transform.rotate(snake.head_img, 180)
        elif snake.direction == "up":
            return pygame.transform.rotate(snake.head_img, 90)
        elif snake.direction == "down":
            return pygame.transform.rotate(snake.head_img, -90)
        return snake.head_img
    