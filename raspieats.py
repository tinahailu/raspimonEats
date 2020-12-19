from sense_hat import SenseHat
import time
import random


sense = SenseHat()
sense.clear()

#colors
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
r = (255, 0 , 0)

###NEW

class Game:
    def __init__(self):
        self.player_x = 0
        self.player_y = 0
        self.food_x = 6
        self.food_y = 6
        self.is_hungry = True 
        self.score = 0




    def reset(self):
        sense.clear()
        self.player_x = random.randint(0,7)
        self.player_y = random.randint(0,7)
        same_spot = True
        while same_spot:
            self.food_x = random.randint(0,7)
            self.food_y = random.randint(0,7)
            if self.player_x != self.food_x and self.player_y != self.food_y:
                same_spot = False
                break

        sense.set_pixel(self.player_x,self.player_y, y)
        sense.set_pixel(self.food_x, self.food_y, g)
        print("reset")

    def update(self):
        sense.clear()
        sense.set_pixel(self.player_x,self.player_y, y)
        sense.set_pixel(self.food_x, self.food_y, g)
        print("updated")


    def down(self):
        if self.player_y <7:
            self.player_y += 1
            print("y:" + str(self.player_y))
            self.update()

    def up(self):
        if self.player_y >0:
            self.player_y -= 1
            print("y:" + str(self.player_y))
            self.update()

    def right(self):
        if self.player_x <7:
            self.player_x += 1
            print("y:" + str(self.player_x))
            self.update()

    def left(self):
        if self.player_x >0:
            self.player_x -= 1
            print("y:" + str(self.player_x))
            self.update()
    

    def run(self):
        self.update()
        while self.is_hungry:
            for event in sense.stick.get_events():
                # print(event)

                if event.direction == "down" and event.action == "released":
                    self.down()
                if event.direction == "up" and event.action == "released":
                    self.up()
                if event.direction == "left" and event.action == "released":
                    self.left()
                if event.direction == "right" and event.action == "released":
                    self.right()
                if self.player_x == self.food_x and self.food_y == self.player_y:
                    self.score += 1
                    sense.show_letter(str(self.score))
                    time.sleep(.5)
                    self.reset()
                #    sense.show_message("GAME OVER")

                                                          

# my_game = Game()
# my_game.run()































##OLD

#variables for player & food postioning
# player_x = 0
# player_y = 0
# sense.set_pixel(player_x,player_y,y)

# food_x = 6
# food_y = 6
# sense.set_pixel(food_x,food_y,l)


# is_hungry = True 

# def down():
#     global player_y
#     if player_y <7:
#         player_y += 1
#         print("y:" + str(player_y))
#         update()


# def update():
#     global player_x, player_y
#     sense.clear()
#     sense.set_pixel(player_x,player_y, y)
#     sense.set_pixel(food_x, food_y, g)
#     print("updated")

# while is_hungry:
#     for event in sense.stick.get_events():
#         # print(event)

#         if event.direction == "down" and event.action == "released":
#             down()

