'''
双色球选号
'''
import random
def select():
    red_balls = [str(i) for i in range(1, 34)]
    blue_balls = [str(i) for i in range(1, 17)]
    red = random.sample(red_balls, 6)
    blue = random.sample(blue_balls, 1)
    return sorted(red) + sorted(blue)
print(select())
