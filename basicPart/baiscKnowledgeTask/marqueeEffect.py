import os
import time

# 跑马灯效果
def marquee_text(text, width):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # 三目运算符
        print(text[:width])
        text = text[1:] + text[0]
        time.sleep(0.2)

text = "Hello Everyone, this is a marquee text effect! "
width = 20
marquee_text(text, width)