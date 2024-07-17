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
        image = pygame.image.load(img)
        for x in range(self.screen.get_width()//20):
            for y in range(self.screen.get_height()//20):
                self.screen.blit(image,(x*20,y*20))

    def draw_snack(self, snack):
        for x,y in snack.body:
            pygame.draw.rect(self.screen, self.green,[x,y,config.BLOCK_SIZE,config.BLOCK_SIZE])

    def draw_food(self, food):
        pygame.draw.rect(self.screen, self.red,[food.position[0],food.position[1],config.BLOCK_SIZE,config.BLOCK_SIZE])

    def draw_score(self, score):
        text = self.font.render(f"Score: {score}", True, self.white)
        self.screen.blit(text, (10,10))
    
    def draw_game_over(self):
        text = self.font.render("Game over ya habbeby", True, self.white)
        center_x = config.WIDTH//2 - text.get_width()//2
        center_y = config.HIGHT//2-text.get_height()//2
        self.screen.blit(text, (center_x, center_y))