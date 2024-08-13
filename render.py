import pygame
import config

class Render:
    def __init__(self, screen, bush_img):
        self.screen = screen
        self.width= screen.get_width()
        self.height = screen.get_height()
        self.background = config.COLORS["navy"]
        self.red = config.COLORS["red"]
        self.green = config.COLORS["green"]
        self.white = config.COLORS["white"]
        pygame.font.init()
        self.font = pygame.font.Font(None, 26)
        self.bush_img_buttom = bush_img
        self.bush_img_top = pygame.transform.rotate(bush_img, 180)
        self.bush_img_right = pygame.transform.rotate(bush_img, 90)
        self.bush_img_left = pygame.transform.rotate(bush_img, -90)
        

    def draw_background(self, img, edge_img):
        
        self.screen.fill(self.background)
        for x in range(self.screen.get_width()//20):
            for y in range(self.screen.get_height()//20):
                self.screen.blit(img,(x*20,y*20))

        bush_width = 20
        bush_height = 20
        for x in range(0, config.WIDTH, bush_width):
            self.screen.blit(self.bush_img_buttom, (x, config.HIGHT-bush_height, bush_width, bush_height))
            self.screen.blit(self.bush_img_top, (x, 0, bush_width, bush_height))
        for y in range(0, config.HIGHT, bush_height):
            self.screen.blit(self.bush_img_left, (0, y, bush_width, bush_height))
            self.screen.blit(self.bush_img_right, (config.WIDTH-bush_width, y, bush_width, bush_height))

    def draw_snake(self, snake):
        head_img = self.head_rotation(snake)
        self.screen.blit(head_img,snake.head.topleft)
        for segment in snake.body[1:]:
            self.screen.blit(snake.body_img, segment.topleft)

    def draw_food(self, food):
        self.screen.blit(food.food_img, food.position.topleft)
    
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
    
    def draw_incon(self, value, icon_img, pos):
        text = self.font.render(f"{value}", True, self.white)
        img_rect = icon_img.get_rect()
        img_rect.topleft = pos
        self.screen.blit(icon_img, img_rect)
        self.screen.blit(text, (img_rect.right+10, img_rect.y))
    