'''
  打印一个五行五列的正方形
'''

firstLayer = 1 

while firstLayer <= 5:
  stars = ''
  for star in range(1, 6):
    stars = stars + " *"
  print(stars)
  print("\n")
  firstLayer += 1

