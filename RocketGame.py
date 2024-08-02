import thumby
import time
import math

# BITMAP: width: 7, height: 8
rocketMap1 = bytearray([64, 32, 126, 191, 126, 32, 64])

# BITMAP: width: 4, height: 40
planetMap = bytearray([6, 15, 15, 6])

# Make a sprite object using bytearray
rocketSprite1 = thumby.Sprite(7, 8, rocketMap1)
rocketSprite2 = thumby.Sprite(7, 8, rocketMap1)  # Second rocket
planetSprite = thumby.Sprite(4, 4, planetMap)

# Set the FPS
thumby.display.setFPS(60)

# Screen size constants
Xo = thumby.display.width 
Yo = thumby.display.height

# Set planet position at center
planetSprite.x = Xo // 2 - planetSprite.width // 2
planetSprite.y = Yo // 2 - planetSprite.height // 2

# Initial positions and velocities and defin gravity
x1, y1 = 0, 10
Vx1, Vy1 = 0, 0

theirPlayerPos = bytearray([0, 0])

x2, y2 = 0, -10
Vx2, Vy2 = 0, 0

G = 2

while True:
    t0 = time.ticks_ms()  # Get current time in ms
    thumby.display.fill(0)  # Clear the display

    # Update rocket 1 position and velocity
    d2_1 = x1 * x1 + y1 * y1
    if d2_1 < 1:
        d2_1 = 1

    Grav1 = G / d2_1
    GravX1 = (-x1 / math.sqrt(d2_1)) * Grav1
    GravY1 = (-y1 / math.sqrt(d2_1)) * Grav1

    Ax1, Ay1 = GravX1, GravY1
    if thumby.buttonU.pressed():
        Ay1 += 1
    if thumby.buttonL.pressed():
        Ax1 -= 1
    if thumby.buttonD.pressed():
        Ay1 -= 1
    if thumby.buttonR.pressed():
        Ax1 += 1
    if thumby.buttonB.pressed():
        x1, y1, Vx1, Vy1 = 0, 10, 0, 0  # Reset rocket 1 position and velocity

    Vx1 += Ax1 / 60
    Vy1 += Ay1 / 60
    x1 += Vx1 / 40
    y1 += Vy1 / 40

    rocketSprite1.x = int(x1 + Xo // 2)
    rocketSprite1.y = int(Yo - (y1 + Yo // 2))

    # rocket 2 in/out
    rocketSprite2.x = (theirPlayerPos[0])
    rocketSprite2.y = (theirPlayerPos[1])


    # Draw sprites on the display
    thumby.display.drawSprite(rocketSprite1)
    thumby.display.drawSprite(rocketSprite2)
    thumby.display.drawSprite(planetSprite)
    thumby.display.update()

    # Print positions for debugging
    #print(f"Rocket 1: {x1}, {y1}")
    #print(f"Rocket 2: {x2}, {y2}")

    # Maintain consistent FPS
    t1 = time.ticks_ms()
    sleep_time = max(0, int(1000 / 60 - (t1 - t0)))
    time.sleep_ms(sleep_time)

    # communication between rockets
    myPlayerPos = bytearray([ rocketSprite1.x.to_bytes(1, 'little')[0] , rocketSprite1.y.to_bytes(1, 'little')[0]])
    print(myPlayerPos)

    thumby.link.send(myPlayerPos)
    received = thumby.link.receive()
    
    if received != None:
        theirPlayerPos = received
