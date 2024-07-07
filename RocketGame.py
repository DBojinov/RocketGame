import time
import thumby
import math

# BITMAP: width: 7, height: 8
rocketMap1 = bytearray([64, 32, 126, 191, 126, 32, 64])

# BITMAP: width: 4, height: 40
planetMap = bytearray([6, 15, 15, 6])



# Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
rocketSprite1 = thumby.Sprite(7, 8, rocketMap1)
planetSprite = thumby.Sprite(4, 4, planetMap)


# Set the FPS (without this call, the default fps is 30)
thumby.display.setFPS(60)


#names constants for screen size
Xo = thumby.display.width 
Yo = thumby.display.height


#sets planet at "0,0"
planetSprite.x = Xo/2
planetSprite.y = Yo/2


#set speed and pos to 0
x = 0
y = 10
Vx = 0
Vy = 0
G = 2




while(1):
    t0 = time.ticks_ms()   # Get time (ms)
    thumby.display.fill(0) # Fill canvas to black

    # Display the bitmap using bitmap data, position, and bitmap dimensions
    thumby.display.drawSprite(rocketSprite1)
    thumby.display.drawSprite(planetSprite)
    thumby.display.update()

    d2 = x*x + y*y
    
    if d2 < 1: 
        d2 = 1

    Grav = G/(d2)
    
    GravX = (-x/math.sqrt(d2)) * Grav
    GravY = (-y/math.sqrt(d2)) * Grav
    
    
    Ax = GravX
    Ay = GravY
    if thumby.buttonU.pressed():
        Ay += 1
    if thumby.buttonL.pressed():
        Ax += -1
    if thumby.buttonD.pressed():
        Ay += -1
    if thumby.buttonR.pressed():
        Ax += 1
    if thumby.buttonB.pressed():
        x = 0
        y = 0
        Vx = 0
        Vy = 0
    
    Vx += Ax/60
    Vy += Ay/60
    x += Vx/40
    y += Vy/40
    
    rocketSprite1.x = x + Xo/2
    rocketSprite1.y = Yo - (y + Yo/2)
    print(x)
    print(y)
