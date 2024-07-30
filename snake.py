import pygame
class snake:
    def __init__(self, head_img, body_img,block_size, init_x, init_y):
        self.init_x = init_x
        self.init_y = init_y
        self.head_img = head_img
        self.body_img = body_img
        self.body_width = body_img.get_width()
        self.body_height = body_img.get_height()
        self.block_size = block_size
        self.direction = "right"
        self.head = pygame.rect.Rect(init_x,init_y,self.body_width,self.body_height)
        self.body = [
            self.head,
            pygame.rect.Rect(init_x-self.body_width,init_y,self.body_width, self.body_height),
            pygame.rect.Rect(init_x-2*self.body_width,init_y,self.body_width, self.body_height)
        ]

    def move(self):
        if self.direction == "up":
            new_head = pygame.rect.Rect(self.head.x, self.head.y-self.body_height,self.body_width,self.body_height)
        elif self.direction == "down":
            new_head = pygame.rect.Rect(self.head.x, self.head.y+self.body_height,self.body_width,self.body_height)
        elif self.direction == "left":
            new_head = pygame.rect.Rect(self.head.x-self.body_width, self.head.y,self.body_width,self.body_height)
        elif self.direction == "right":
            new_head = pygame.rect.Rect(self.head.x+self.body_width, self.head.y,self.body_width,self.body_height)
        self.body.insert(0, new_head)
        self.head = self.body[0]
        

    def remove_tail(self):
        self.body.pop()
