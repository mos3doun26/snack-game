import random
import config
import pygame
class Food:
    def __init__(self, food_img, snake):
        self.food_img = food_img
        self.food_width = self.food_img.get_width()
        self.food_height = self.food_img.get_height()
        self.position = self.create(snake)

    def create(self, snake):
        while True:
            x = random.randint(4,(config.WIDTH-config.BLOCK_SIZE)//config.BLOCK_SIZE) * config.BLOCK_SIZE
            y = random.randint(4,(config.HIGHT-config.BLOCK_SIZE)//config.BLOCK_SIZE) * config.BLOCK_SIZE
            snake_segments_positions = [segment.topleft for segment in snake.body]
            if (x,y) not in snake_segments_positions:
                return pygame.rect.Rect(x-self.food_width,y-self.food_height,self.food_width,self.food_height)
