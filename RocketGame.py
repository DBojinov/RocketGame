import time
import thumby
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

# Initial positions and velocities
x1, y1 = 0, 10
Vx1, Vy1 = 0, 0

x2, y2 = 0, -10
Vx2, Vy2 = 0, 0

G = 2

while True:
    t0 = time.ticks_ms()  # Get current time in ms
    thumby.display.fill(0)  # Clear the display

    # Update and display sprites
    thumby.display.drawSprite(rocketSprite1)
    thumby.display.drawSprite(rocketSprite2)
    thumby.display.drawSprite(planetSprite)
    thumby.display.update()

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

    rocketSprite1.x = x1 + Xo // 2
    rocketSprite1.y = Yo - (y1 + Yo // 2)

    # Update rocket 2 position and velocity
    d2_2 = x2 * x2 + y2 * y2
    if d2_2 < 1:
        d2_2 = 1

    Grav2 = G / d2_2
    GravX2 = (-x2 / math.sqrt(d2_2)) * Grav2
    GravY2 = (-y2 / math.sqrt(d2_2)) * Grav2

    Ax2, Ay2 = GravX2, GravY2
    if thumby.buttonA.pressed():
        Ay2 += 1
    if thumby.buttonL.pressed() and not thumby.buttonR.pressed():  # Avoid conflict with rocket 1
        Ax2 -= 1
    if thumby.buttonD.pressed() and not thumby.buttonU.pressed():  # Avoid conflict with rocket 1
        Ay2 -= 1
    if thumby.buttonR.pressed() and not thumby.buttonL.pressed():  # Avoid conflict with rocket 1
        Ax2 += 1
    if thumby.buttonB.pressed() and thumby.buttonA.pressed():  # Combined button press to reset rocket 2
        x2, y2, Vx2, Vy2 = 0, -10, 0, 0  # Reset rocket 2 position and velocity

    Vx2 += Ax2 / 60
    Vy2 += Ay2 / 60
    x2 += Vx2 / 40
    y2 += Vy2 / 40

    rocketSprite2.x = x2 + Xo // 2
    rocketSprite2.y = Yo - (y2 + Yo // 2)

    print(f"Rocket 1: {x1}, {y1}")
    print(f"Rocket 2: {x2}, {y2}")
