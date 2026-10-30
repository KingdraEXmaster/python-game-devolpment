import pgzrun
import random
WIDTH=600
HEIGHT=400
TITLE="Alien Shooter"
message=""
alien=Actor("alien")
def draw():
    screen.fill("Black")
    alien.draw()
    screen.draw.text(message,(20,20),fontsize=30,color="Blue")


def placealien():
    alien.x=random.randint(50,550)
    alien.y=random.randint(50,350)
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Good shot"
        placealien()
    else:
        message="Better luck next time"
        placealien()
placealien()
pgzrun.go()