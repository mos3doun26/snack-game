import random
import config
class Food:
    def __init__(self, snack_body):
        self.position = self.create(snack_body)

    def create(self, snack_body):
        while True:
            x = random.randint(0,(config.WIDTH-config.BLOCK_SIZE)//config.BLOCK_SIZE) * config.BLOCK_SIZE
            y = random.randint(0,(config.HIGHT-config.BLOCK_SIZE)//config.BLOCK_SIZE) * config.BLOCK_SIZE
            if (x,y) not in snack_body:
                return (x,y)
        