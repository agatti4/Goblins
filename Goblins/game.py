# Anthony Gatti
# CS 152
# Spring 2020
# Project 11
# Video Game

# To run type python3 game.py into terminal

# Added a point system after feedback from my brother
# Too easy at first because staying on the sides you could get tons of point so I sped up the goblins
# Became too hard after this so I made it 60 sec long instead of 30, which then made it the perfect difficulty

import graphicsPlus as gr
import physics_objects as pho
import collision as coll
import math
import time
import random

def startScreen(win):
    #Creates the start screen that appears upon opening
    win = win

    shapes = []

    #creates the dark red border with a smaller black screen in the middle
    block = pho.Block(win, 500, 500, [250, 250], color="red4")
    block.draw()
    shapes.append(block)

    block2 = pho.Block(win, 480, 480, [250, 250], color="black")
    block2.draw()
    shapes.append(block2)

    #Creates background blocks for the title
    title = pho.Block( win, 300, 100, [250, 410], color='red2' )
    title.draw()
    shapes.append(title)

    title2 = pho.Block( win, 280, 80, [250, 410], color='black' )
    title2.draw()
    shapes.append(title2)
    
    #Creates background blocks for the start, instructions, and exit buttons
    start = pho.Block( win, 200, 40, [250, 300], color='green' )
    start.draw()
    shapes.append(start)

    instructions = pho.Block( win, 200, 40, [250, 200], color='green' )
    instructions.draw()
    shapes.append(instructions)

    exit = pho.Block( win, 200, 40, [250, 100], color='green' )
    exit.draw()
    shapes.append(exit)
    
    #Creates the text for the start screen
    titletxt = gr.Text( gr.Point( 250, 90 ), 'Goblins')
    titletxt.setSize( 36 )
    titletxt.setFill('green4')
    titletxt.setFace('courier')
    titletxt.setStyle('bold')
    titletxt.draw(win)
    shapes.append(titletxt)
    win.update()

    startText = gr.Text( gr.Point( 250, 200 ), 'Start')
    startText.setSize( 24 )
    startText.setFill('red')
    startText.setFace('courier')
    startText.draw(win)
    shapes.append(startText)
    win.update()

    intxt = gr.Text( gr.Point( 250, 300 ), 'Instructions')
    intxt.setSize( 24 )
    intxt.setFill('red')
    intxt.setFace('courier')
    intxt.draw(win)
    shapes.append(intxt)
    win.update()

    extxt = gr.Text( gr.Point( 250, 400 ), 'Exit')
    extxt.setSize( 24 )
    extxt.setFill('red')
    extxt.setFace('courier')
    extxt.draw(win)
    shapes.append(extxt)
    win.update()

    return shapes


def gameScreen(win):
    #Creates the game screen

    win = win
    
    shapes = []
    
    #creates the dark red border with a smaller black screen in the middle
    block = pho.Block(win, 500, 500, [250, 250], color="red4")
    block.draw()
    shapes.append(block)
    
    block2 = pho.Block(win, 480, 480, [250, 250], color="black")
    block2.draw()
    shapes.append(block2)
    
    #Creates the blue block which is the character
    player = pho.Block(win, 20, 20, [250, 21], color="blue")
    player.draw()
    shapes.append(player)
    
    #Creates the block goblin
    goblin1 = pho.Block(win, 40, 40, [250, 275], color="green")
    goblin1.setVelocity([20, 0])
    goblin1.draw()
    shapes.append(goblin1)

    #Creates the triangle goblin
    goblin2 = pho.Triangle(win, 10, [250, 350], color="green")
    goblin2.setVelocity([-30, 0])
    goblin2.draw()
    shapes.append(goblin2)
    
    #Creates the ball goblin
    goblin3 = pho.Ball(win, 15, [250, 400], color="green")
    goblin3.setVelocity([100, 0])
    goblin3.draw()
    shapes.append(goblin3)
    
    #Creates the rectangle goblin
    goblin4 = pho.Block(win, 60, 10, [250, 475], color="green")
    goblin4.setVelocity([200, 0])
    goblin4.draw()
    shapes.append(goblin4)
    
    #Creates the 4 dark red rotating block obstacles in the middle of the gamescreen
    obstacle1 = pho.RotatingBlock( win, 50, 20, [100, 200], color='red4' )
    obstacle1.setRotVelocity(-120)
    obstacle1.draw()
    shapes.append(obstacle1)
    
    obstacle2 = pho.RotatingBlock( win, 50, 20, [200, 200], color='red4' )
    obstacle2.setRotVelocity(-120)
    obstacle2.draw()
    shapes.append(obstacle2)
    
    obstacle3 = pho.RotatingBlock( win, 50, 20, [300, 200], color='red4' )
    obstacle3.setRotVelocity(-120)
    obstacle3.draw()
    shapes.append(obstacle3)
    
    obstacle4 = pho.RotatingBlock( win, 50, 20, [400, 200], color='red4' )
    obstacle4.setRotVelocity(-120)
    obstacle4.draw()
    shapes.append(obstacle4)
    
    #creates the bullet that the shooter shoots to kill goblins
    bullet = pho.Ball(win, 5, [250, 31], color="yellow")
    bullet.draw()
    shapes.append(bullet)

    #Creates the point system
    pointsys = 'Pts: ' + str(0)
    
    pointtxt = gr.Text( gr.Point( 400, 50 ), pointsys)
    pointtxt.setSize( 36 )
    pointtxt.setFill('yellow4')
    pointtxt.setFace('courier')
    pointtxt.draw(win)
    shapes.append(pointtxt)
    win.update()
    
    '''timershow = 'Time ' + str(30)'''
    
    '''pointtxt = gr.Text( gr.Point( 100, 50 ), timershow)
    pointtxt.setSize( 36 )
    pointtxt.setFill('yellow4')
    pointtxt.setFace('courier')
    pointtxt.draw(win)
    shapes.append(pointtxt)
    win.update()'''
    
    return shapes
    
def endScreen(win):
    #Creates the end screen
    
    win = win

    shapes = []

    #creates the dark red border with a smaller black screen in the middle
    block = pho.Block(win, 500, 500, [250, 250], color="red4")
    block.draw()
    shapes.append(block)

    block2 = pho.Block(win, 480, 480, [250, 250], color="black")
    block2.draw()
    shapes.append(block2)

    #Creates background blocks for the results title
    title = pho.Block( win, 300, 100, [250, 410], color='red2' )
    title.draw()
    shapes.append(title)

    title2 = pho.Block( win, 280, 80, [250, 410], color='black' )
    title2.draw()
    shapes.append(title2)

    #Creates the results text
    titletxt = gr.Text( gr.Point( 250, 90 ), 'Results')
    titletxt.setSize( 36 )
    titletxt.setFill('green4')
    titletxt.setFace('courier')
    titletxt.setStyle('bold')
    titletxt.draw(win)
    shapes.append(titletxt)
    win.update()

    return shapes


def instructPage(win):
    #Creates the instruct page
    
    win = win
    
    shapes = []
    
    #creates the dark red border with a smaller black screen in the middle
    block = pho.Block(win, 500, 500, [250, 250], color="red4")
    block.draw()
    shapes.append(block)
    
    block2 = pho.Block(win, 480, 480, [250, 250], color="black")
    block2.draw()
    shapes.append(block2)
    
    #Creates the Exit button for instruct page
    back = pho.Block( win, 200, 40, [250, 100], color='green' )
    back.draw()
    shapes.append(back)
    
    #Creates the text for the instructions page
    titletxt = gr.Text( gr.Point( 250, 90 ), 'Instructions')
    titletxt.setSize( 36 )
    titletxt.setFill('green4')
    titletxt.setFace('courier')
    titletxt.setStyle('bold')
    titletxt.draw(win)
    shapes.append(titletxt)
    win.update()
    
    titletxt = gr.Text( gr.Point( 250, 120 ), 'You must kill enough goblins to reach')
    titletxt.setSize( 16 )
    titletxt.setFill('green4')
    titletxt.setFace('courier')
    titletxt.draw(win)
    shapes.append(titletxt)
    win.update()
    
    titletxt = gr.Text( gr.Point( 250, 140 ), '1000 points before 60 sec run out')
    titletxt.setSize( 16 )
    titletxt.setFill('green4')
    titletxt.setFace('courier')
    titletxt.draw(win)
    shapes.append(titletxt)
    win.update()
    
    titletxt = gr.Text( gr.Point( 250, 170 ), 'Left and Right to move, Space to fire')
    titletxt.setSize( 16 )
    titletxt.setFill('green4')
    titletxt.setFace('courier')
    titletxt.draw(win)
    shapes.append(titletxt)
    win.update()
    
    goblin1 = pho.Block(win, 40, 40, [90, 295], color="green")
    goblin1.draw()
    
    gob1 = gr.Text( gr.Point( 250, 205 ), 'Square Goblin - 10 Points')
    gob1.setSize( 16 )
    gob1.setFill('green4')
    gob1.setFace('courier')
    gob1.draw(win)
    shapes.append(gob1)
    win.update()

    goblin2 = pho.Triangle(win, 10, [90, 245], color="green")
    goblin2.draw()
    
    gob2 = gr.Text( gr.Point( 250, 255 ), 'Triangle Goblin - 20 Points')
    gob2.setSize( 16 )
    gob2.setFill('green4')
    gob2.setFace('courier')
    gob2.draw(win)
    shapes.append(gob2)
    win.update()
    
    goblin3 = pho.Ball(win, 15, [90, 195], color="green")
    goblin3.draw()
    
    gob3 = gr.Text( gr.Point( 250, 305 ), 'Ball Goblin - 50 Points')
    gob3.setSize( 16 )
    gob3.setFill('green4')
    gob3.setFace('courier')
    gob3.draw(win)
    shapes.append(gob3)
    win.update()
    
    goblin4 = pho.Block(win, 60, 10, [90, 145], color="green")
    goblin4.draw()
    
    gob4 = gr.Text( gr.Point( 275, 355 ), 'Rectangle Goblin - 100 Points')
    gob4.setSize( 16 )
    gob4.setFill('green4')
    gob4.setFace('courier')
    gob4.draw(win)
    shapes.append(gob4)
    win.update()
    
    extxt = gr.Text( gr.Point( 250, 400 ), 'Exit')
    extxt.setSize( 24 )
    extxt.setFill('red')
    extxt.setFace('courier')
    extxt.draw(win)
    shapes.append(extxt)
    win.update()
    
    return shapes

def inStart(pt, block):
    #Checks if clicked in the start button
    dx = pt.getX() - block.getPosition()[0]
    dy = -(pt.getY() - block.getPosition()[1])

    return dx >= -100 and dx <= 100 and dy >= 80 and dy <= 120

def inInstructions(pt, block):
    #Checks if clicked in the instructions button
    dx = pt.getX() - block.getPosition()[0]
    dy = pt.getY() - block.getPosition()[1]

    return dx >= -100 and dx <= 100 and dy >= 80 and dy <= 120

def inExit(pt, block):
    #Checks if clicked in the exit button
    dx = pt.getX() - block.getPosition()[0]
    dy = pt.getY() - block.getPosition()[1]
    
    return dx >= -100 and dx <= 100 and dy >= 280 and dy <= 320
    
'''def timedown():
    timer = 31
    timer -= 1
    return timer'''
    
def main():
    #Main function

    dt = 0.02

    win = gr.GraphWin('Goblins', 500, 500, False)
    
    # Phase 1: start screen
    # game loads with the start screen
    shapes = startScreen(win)
    
    #Event loop for the start screen
    
    while True:
        clickPoint = win.getMouse()
        print(clickPoint)
        if inStart(clickPoint, shapes[4]):
            # break out of the start screen loop and loads game
            break
        if inInstructions(clickPoint, shapes[5]):
            #if clicked on instructions button instruction page loads
            x = instructPage(win)
            clickPoint = win.getMouse()
        if inExit(clickPoint, shapes[6]):
            #if clicked on exit button closes program
            win.close()
            return
            
            
    # undraw the start screen shapes
    for shape in shapes:
        shape.undraw()
    # Phase 2: pay the game
    # calls the gameScreen function
    gameScreen(win)
    objs = gameScreen(win)
    #initializes timer and point system
    pointvalue = 0
    starttime = time.time()
    timeleft = 60
    timeleft2 = 60
    timertime = 60
    
    
    '''if ((time.time() - starttime) < timeleft):
        timeleft -= 1
        objs[13].setText('Time ' + str(timeleft))
    if ((time.time() - starttime) < timeleft):
        timeleft -= 1
        objs[13].setText('Time ' + str(timeleft))'''
    
    #Event loop for the game to respond to actions in the game screen
    while True:
       # run game here
        key = win.checkKey()
        
        #makes the obstacles rotate and goblins move
        objs[7].update(dt)
        objs[8].update(dt)
        objs[9].update(dt)
        objs[10].update(dt)
        
        objs[3].update(dt)
        objs[4].update(dt)
        objs[5].update(dt)
        objs[6].update(dt)
        
        '''if ((time.time() - starttime) > timeleft):
            timeleft2 -= 1
            objs[13].setText('Time ' + str(timeleft2))'''
        
        #timer that stops the game after 60 seconds
        current = time.time()
        passed = current - starttime
        if passed > timertime:
            timeleft -= 60
            '''objs[13].setText('Time ' + str(timeleft))'''
        
        if key == 'Right':
            #if the right key is pressed the player moves to the right
            objs[2].setVelocity([100, 0])
            objs[2].setAcceleration([0, 0])
            if objs[11].getPosition()[1] == 31:
                objs[11].setVelocity([100, 0])
                objs[11].setAcceleration([0, 0])
        objs[2].update(dt)
        objs[11].update(dt)
            
        if key == 'Left':
            #if the left key is pressed the player moves to the left
            objs[2].setVelocity([-100, 0])
            objs[2].setAcceleration([0, 0])
            if objs[11].getPosition()[1] == 31:
                objs[11].setVelocity([-100, 0])
                objs[11].setAcceleration([0, 0])
        objs[2].update(dt)
        objs[11].update(dt)
            
        if key == 'space':
            #if space key is pressed the bullet is fired up
            objs[11].setVelocity([0, 200])
            objs[11].setAcceleration([0, 20])
        objs[2].update(dt)
        objs[11].update(dt)
        
        p = objs[2].getPosition()
            
        if p[0] > 500:
            #if player hits the edge it stops it from going out
            objs[2].setPosition([480, 21])
            objs[2].setVelocity([0, 0])
            objs[2].setAcceleration([0, 0])
            objs[2].update(dt)
            if objs[11].getPosition()[1] == 31:
                objs[11].setPosition([480, 31])
                objs[11].setVelocity([0, 0])
                objs[11].setAcceleration([0, 0])
                objs[11].update(dt)
        
        if p[0] < 0:
            #if player hits the edge it stops it from going out
            objs[2].setPosition([20, 21])
            objs[2].setVelocity([0, 0])
            objs[2].setAcceleration([0, 0])
            objs[2].update(dt)
            if objs[11].getPosition()[1] == 31:
                objs[11].setPosition([20, 31])
                objs[11].setVelocity([0, 0])
                objs[11].setAcceleration([0, 0])
                objs[11].update(dt)
            
        
        op = objs[2].getPosition()[0]
        ov = objs[2].getVelocity()
        oa = objs[2].getAcceleration()
        
        if coll.collision(objs[11], objs[7], dt):
            #Checks collision and resets bullet
            objs[11].setPosition([op, 31])
            objs[11].setVelocity(ov)
            objs[11].setAcceleration(oa)
            objs[2].update(dt)
            objs[11].update(dt)
            
        if coll.collision(objs[11], objs[8], dt):
            #Checks collision and resets bullet
            objs[11].setPosition([op, 31])
            objs[11].setVelocity(ov)
            objs[11].setAcceleration(oa)
            objs[2].update(dt)
            objs[11].update(dt)
            
        if coll.collision(objs[11], objs[9], dt):
            #Checks collision and resets bullet
            objs[11].setPosition([op, 31])
            objs[11].setVelocity(ov)
            objs[11].setAcceleration(oa)
            objs[2].update(dt)
            objs[11].update(dt)
        
        if coll.collision(objs[11], objs[10], dt):
            #Checks collision and resets bullet
            objs[11].setPosition([op, 31])
            objs[11].setVelocity(ov)
            objs[11].setAcceleration(oa)
            objs[2].update(dt)
            objs[11].update(dt)
            
        bp = objs[11].getPosition()
        
        if bp[1] > 490:
            #resets bullet if hits edge
            objs[11].setPosition([op, 31])
            objs[11].setVelocity(ov)
            objs[11].setAcceleration(oa)
            objs[2].update(dt)
            objs[11].update(dt)
            
        #Makes the square goblin bounce back and forth
        goblin1p = objs[3].getPosition()
        
        if goblin1p[0] < 30:
            objs[3].setPosition([30, 275])
            objs[3].setVelocity([20, 0])
            objs[3].setAcceleration([0, 0])
            objs[3].update(dt)
            
        if goblin1p[0] > 470:
            objs[3].setPosition([470, 275])
            objs[3].setVelocity([-20, 0])
            objs[3].setAcceleration([0, 0])
            objs[3].update(dt)
            
        #Makes the triangle goblin bounce back and forth
        goblin2p = objs[4].getPosition()
        
        if goblin2p[0] < 30:
            objs[4].setPosition([30, 350])
            objs[4].setVelocity([30, 0])
            objs[4].setAcceleration([0, 0])
            objs[4].update(dt)
            
        if goblin2p[0] > 470:
            objs[4].setPosition([470, 350])
            objs[4].setVelocity([-30, 0])
            objs[4].setAcceleration([0, 0])
            objs[4].update(dt)
        
        #Makes the ball goblin bounce back and forth
        goblin3p = objs[5].getPosition()
        
        if goblin3p[0] < 20:
            objs[5].setPosition([20, 400])
            objs[5].setVelocity([100, 0])
            objs[5].setAcceleration([0, 0])
            objs[5].update(dt)
            
        if goblin3p[0] > 480:
            objs[5].setPosition([480, 400])
            objs[5].setVelocity([-100, 0])
            objs[5].setAcceleration([0, 0])
            objs[5].update(dt)
        
        #Makes the rectangle goblin bounce back and forth
        goblin4p = objs[6].getPosition()
        
        if goblin4p[0] < 40:
            objs[6].setPosition([40, 475])
            objs[6].setVelocity([200, 0])
            objs[6].setAcceleration([0, 0])
            objs[6].update(dt)
            
        if goblin4p[0] > 460:
            objs[6].setPosition([460, 475])
            objs[6].setVelocity([-200, 0])
            objs[6].setAcceleration([0, 0])
            objs[6].update(dt)

        #Undraws the square goblin when hit by bullet
        if coll.collision(objs[11], objs[3], dt):
            objs[11].setPosition([op, 31])
            objs[11].setVelocity(ov)
            objs[11].setAcceleration(oa)
            objs[3].undraw()
            objs[11].update(dt)
            pointvalue += 10
            objs[12].setText('Pts: ' + str(pointvalue) )
            objs[3].setPosition([30, 275])
            objs[3].setVelocity([20, 0])
            objs[3].setAcceleration([0, 0])
            objs[3].draw()
            objs[3].update(dt)

        #Undraws the triangle goblin when hit by bullet
        if coll.collision(objs[11], objs[4], dt):
            objs[11].setPosition([op, 31])
            objs[11].setVelocity(ov)
            objs[11].setAcceleration(oa)
            objs[4].undraw()
            objs[11].update(dt)
            pointvalue += 20
            objs[12].setText('Pts: ' + str(pointvalue) )
            objs[4].setPosition([470, 350])
            objs[4].setVelocity([-30, 0])
            objs[4].setAcceleration([0, 0])
            objs[4].draw()
            objs[4].update(dt)

        #Undraws the ball goblin when hit by bullet
        if coll.collision(objs[11], objs[5], dt):
            objs[11].setPosition([op, 31])
            objs[11].setVelocity(ov)
            objs[11].setAcceleration(oa)
            objs[5].undraw()
            objs[11].update(dt)
            pointvalue += 50
            objs[12].setText('Pts: ' + str(pointvalue) )
            objs[5].setPosition([20, 400])
            objs[5].setVelocity([100, 0])
            objs[5].setAcceleration([0, 0])
            objs[5].draw()
            objs[5].update(dt)

        #Undraws the rectangle goblin when hit by bullet
        if coll.collision(objs[11], objs[6], dt):
            objs[11].setPosition([op, 31])
            objs[11].setVelocity(ov)
            objs[11].setAcceleration(oa)
            objs[6].undraw()
            objs[11].update(dt)
            pointvalue += 100
            objs[12].setText('Pts: ' + str(pointvalue) )
            objs[6].setPosition([460, 475])
            objs[6].setVelocity([-200, 0])
            objs[6].setAcceleration([0, 0])
            objs[6].draw()
            objs[6].update(dt)
            
        #objs[13].setText('Time ' + str(timedown()))
            
        if timeleft <= 0:
            #if time runs out game ends
            break

        if pointvalue >= 1000:
            #if points reach 1000 or more game ends
            break
        
        if win.checkKey() == 'q': # did the user type a 'q'?
            break
        
        if win.checkMouse(): # did the user click the mouse?
            break
            
        win.update()
    
    # undraw the game screen objects
    for shape in objs:
        shape.undraw()
    
    # Phase 3: draw the final screen
    endScreen(win)
    if pointvalue >= 1000:
        #if player got 1000 points prints a win screen
        intxt = gr.Text( gr.Point( 250, 200 ), 'You Win!')
        intxt.setSize( 24 )
        intxt.setFill('green3')
        intxt.setFace('courier')
        intxt.draw(win)
        shapes.append(intxt)
        win.update()
        intxt2 = gr.Text( gr.Point( 250, 300 ), 'Final Score: ' + str(pointvalue))
        intxt2.setSize( 24 )
        intxt2.setFill('red')
        intxt2.setFace('courier')
        intxt2.draw(win)
        shapes.append(intxt2)
        win.update()
        intxt2 = gr.Text( gr.Point( 250, 400 ), 'Press Anywhere To Quit')
        intxt2.setSize( 24 )
        intxt2.setFill('yellow4')
        intxt2.setFace('courier')
        intxt2.draw(win)
        shapes.append(intxt2)
        win.update()
    if timeleft <= 0:
        #if time ran out prints lose screen
        intxt = gr.Text( gr.Point( 250, 200 ), 'Time Run Out: You Lose!')
        intxt.setSize( 24 )
        intxt.setFill('red4')
        intxt.setFace('courier')
        intxt.draw(win)
        shapes.append(intxt)
        win.update()
        intxt2 = gr.Text( gr.Point( 250, 300 ), 'Final Score: ' + str(pointvalue))
        intxt2.setSize( 24 )
        intxt2.setFill('red')
        intxt2.setFace('courier')
        intxt2.draw(win)
        shapes.append(intxt2)
        win.update()
        intxt2 = gr.Text( gr.Point( 250, 400 ), 'Press Anywhere To Quit')
        intxt2.setSize( 24 )
        intxt2.setFill('yellow4')
        intxt2.setFace('courier')
        intxt2.draw(win)
        shapes.append(intxt2)
        win.update()
        
    # create the final screen
    # wait for a mouse click
    while True:
        clickPoint = win.getMouse()
        if clickPoint: # did the user click the mouse?
            break
    # close and exit
    win.close()

if __name__ == "__main__":
    main()


