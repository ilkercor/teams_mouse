import mouse


# 1
# mouse.click('right')

# 2
# print(mouse.get_position())

# 3
# mouse.drag(0, 0, 50, 50, absolute=True  , duration=0.1)
# print(mouse.get_position())


# mouse.drag(650, 650, 650, 650, absolute=True  , duration=0.1)

#import mouse
import time
import math


def move_half_circle(x_center, y_center, radius=50, duration=0.0001):
    # print(mouse.get_position())

    for angle in range(0, 181, 3):
        x = x_center + radius * math.cos(math.radians(-angle))
        y = y_center + radius * math.sin(math.radians(-angle))
        mouse.move(x, y, absolute=True, duration=0.001)
        time.sleep(duration)



def move_heart():
    # Example usage
    print(mouse.get_position())

    baslangicX = 800 # tested with 500
    baslangicy = 400
    radius = 50

    move_half_circle(baslangicX, baslangicy, radius=radius)
    print(mouse.get_position())
    move_half_circle(baslangicX-(2*radius), baslangicy, radius=radius)
    print(mouse.get_position())

    # legs

    mouse.move(750, baslangicy+radius*1.5, absolute=True, duration=1)
    mouse.move(850, baslangicy, absolute=True, duration=1)

move_heart()

while True:
    time.sleep(300)
    move_heart()

# for _ in range(5):
#     print('moving..')
#     mouse.drag(650, 650, 650, 650, absolute=True  , duration=0.1)

#     time.sleep(1)


# for i in range(400):
#     mouse.click('left')


