class Snack:
    def __init__(self, block_size, init_x, init_y):
        self.block_size = block_size
        self.direction = "right"
        self.body = [
    (init_x,init_y),
    (init_x-self.block_size,init_y),
    (init_x-2*self.block_size,init_y)
]
        self.head = self.body[0]


    def move(self):
        head = self.body[0]
        if self.direction == "up":
            new_head = (head[0], head[1]-self.block_size)
        elif self.direction == "down":
            new_head = (head[0], head[1]+self.block_size)
        elif self.direction == "left":
            new_head = (head[0]-self.block_size, head[1])
        elif self.direction == "right":
            new_head = (head[0]+self.block_size, head[1])
        self.body.insert(0, new_head)
        self.head = self.body[0]
        

    def remove_tail(self):
        self.body.pop()