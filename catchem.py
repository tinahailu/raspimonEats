from sense_emu import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

game_over = False

catcher_x = 0
berry_x = 0
berry_y = 0

score = 0

r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) #blank
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen


#Intro text or animation
# 3,2,1 countdown
def move_left():
  global catcher_x
  if catcher_x >= 1:
      catcher_x -= 1
      

def move_right():
    global catcher_x
    if catcher_x <= 7:
        catcher_x += 1

def berry_fall():
    global berry_y, game_over
    if berry_y < 7:
        berry_y += 1
        sleep(0.2)
        print(berry_y)
    else:
        sense.show_message("GAME OVER")
        game_over = True 
        print("game over")


#update function
def update():
    global berry_x, berry_y, catcher_x, game_over
    sense.clear()
    #berry_fall()
    if berry_y < 7:
       berry_y += 1
       sense.set_pixel(berry_x, berry_y, r)
    else:
        sense.show_message("GAME OVER")
        game_over = True 
        print("game over")
    sense.set_pixel(catcher_x, 7, d)
    #sense.set_pixel(berry_x, berry_y, r)
   # prsint(berry_x, berry_y)



while game_over == False:
    
  
    for event in sense.stick.get_events():
        print(event)
    
        if event.action =="pressed" and event.direction == "left":
            move_left()
        elif event.action == "pressed" and event.direction == "right":
            move_right()


    if catcher_x == berry_x and berry_y == 7:
        print("you caught one!")

    update()
    sleep(1)