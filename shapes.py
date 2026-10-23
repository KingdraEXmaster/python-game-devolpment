import pgzrun
WIDTH=600
HEIGHT=400
def draw():
    screen.fill("Black")
    screen.draw.line((20,150),(200,150),"Cyan")
    screen.draw.circle((128,128),13,"orange")
    screen.draw.filled_circle((400,70),20,"Green")
    screen.draw.rect(Rect((0,0),(20,20)), "Yellow")
    screen.draw.filled_rect(Rect((300,0),(500,20)), "White")
    screen.draw.text("Very well asthetically designed shapes in PGzero",(100,200),fontsize=25, color="blue")

pgzrun.go()