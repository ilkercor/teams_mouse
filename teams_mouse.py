import mouse
import time
import math
import webbrowser

def play_video():
    youtube_URL = "https://www.youtube.com/watch?v=U_KrB31T84g"
    webbrowser.open(youtube_URL)

def move_half_circle(x_center, y_center, radius=50, duration=0.0001):
    for angle in range(0, 181, 3):
        x = x_center + radius * math.cos(math.radians(-angle))
        y = y_center + radius * math.sin(math.radians(-angle))
        mouse.move(x, y, absolute=True, duration=0.001)
        time.sleep(duration)

def move_heart():
    # Example usage
    print(mouse.get_position())

    baslangicX = 800 #tested with 500
    baslangicy = 400
    radius = 50

    move_half_circle(baslangicX, baslangicy, radius=radius)
    print(mouse.get_position())
    move_half_circle(baslangicX-(2*radius), baslangicy, radius=radius)
    print(mouse.get_position())

    # legs
    mouse.move(750, baslangicy+radius*1.5, absolute=True, duration=1)
    mouse.move(850, baslangicy, absolute=True, duration=1)

play_video()
move_heart()

while True:
    time.sleep(300)
    move_heart()