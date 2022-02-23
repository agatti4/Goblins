# Template by Bruce A Maxwell
# Fall 2018
# CS 152 Project 11
#
# Make an Asteroids-like ship move around
#
# slightly modified by Eric Aaron, Fall 2018, Spring 2019
#
# import useful packages
import math
import time
import graphicsPlus as gr
import physics_objects as pho

# make a ship object, treat it as a ball
# but it needs to be able to rotate
# should probably have a parent rotator class that does most of this for you
class Ship(pho.Thing):
    def __init__(self, win, radius=3, position=[0,0]):
        pho.Thing.__init__(self, win, "ball", position=position)

        self.radius = radius

        # anchor point is by default the center of the ship/circle so we don't need it
        self.angle = 0.
        self.dangle = 0.

        self.shapes = []
        self.drawn = False
        self.render() # call render to set up the vis list properly

        # these are for handling the flicker of the exhaust
        self.flickertime = 6
        self.flicker = False
        self.countdown = 0

    #########
    # these functions are identical to the rotating block
    # a smart coder would make a parent rotator class

    # get and set the angle of the object
    # these are unique to rotators
    def getAngle(self):
        return self.angle

    # setAngle has to update the visualization
    def setAngle(self, a):
        self.angle = a
        self.render()

    # get and set rotational velocity
    def setRotVelocity(self, rv):
        self.dangle = rv # degrees per second

    def getRotVelocity(self):
        return self.dangle

    def getRadius(self):
        return self.radius

    def setRadius(self, r):
        self.radius = r
        self.render()

    # incrementally rotate by da (in degrees)
    # has to update the visualization
    def rotate(self, da):
        self.angle += da
        self.render()

    # special ship methods
    def setFlickerOn(self, countdown = 50):
        self.flicker = True
        self.countdown = countdown

    def setFlickerOff(self):
        self.countdown = 0
        self.flicker = False
        
    # simplified render function since the ship always rotates around its center
    def render(self):

        drawn = self.drawn
        if drawn:
            self.undraw()

        # visualization properties
        # This is a two-part visualization
        # the ship is a triangle
        self.bodypts = [ (self.radius, 0),
                         (- self.radius*0.5,   1.732*self.radius*0.5),
                         (- self.radius*0.5, - 1.732*self.radius*0.5) ]
        # the exhaust is another triangle
        self.flamepts = [ (- self.radius*0.5,   0.5*self.radius),
                          (- self.radius*0.5, - 0.5*self.radius),
                          (- self.radius*1.732, 0) ]


        # get the cos and sin of the current orientation
        theta = math.pi * self.angle / 180.
        cth = math.cos(theta)
        sth = math.sin(theta)

        # rotate each point around the object's center
        pts = []
        for vertex in self.bodypts + self.flamepts:
            # move the object's center to 0, 0, which it is already in model coordinates
            xt = vertex[0]
            yt = vertex[1]

            # rotate the vertex by theta around the Z axis
            xtt = cth*xt - sth*yt
            ytt = sth*xt + cth*yt

            # move the object's center back to its original location
            pos = self.getPosition()
            xf = xtt + pos[0]
            yf = ytt + pos[1]

            # create a point with the screen space coordinates
            pts.append( gr.Point(xf, self.win.getHeight() - yf) )

        # make the two objects
        self.shapes = [ gr.Polygon( pts[:3] ), gr.Polygon( pts[3:] ) ]
        self.shapes[0].setFill("dark blue")
        self.shapes[0].setOutline("dark red")
        self.shapes[1].setOutline("yellow")

        if drawn:
            self.draw()


    # update the various state variables
    # add a unique flicker touch
    def update(self, dt):
        # update the angle based on rotational velocity
        da = self.dangle * dt
        if da != 0.0: # don't bother updating if we don't have to
            self.rotate( da )

        # flicker the flames
        # this should be a field of the object
        if self.flicker and self.countdown > 0:
            if self.countdown % self.flickertime < self.flickertime/2:
                self.shapes[1].setFill( 'yellow' )
            else:
                self.shapes[1].setFill( 'orange' )
            self.countdown -= 1
        else:
            self.shapes[1].setFill( 'white' )

        # call the parent update for the rest of it
        pho.Thing.update(self, dt)

def main():
    # make a window
    win = gr.GraphWin('Ship', 500, 500, False)

    # make ship, draw it, wait for a mouse click
    ship = Ship(win, 30, [250, 250])
    ship.draw()
    
    done = False
    dt = 0.02
    gamma = 10
    delta = 5
    ship.setRotVelocity( 20 )
    
    while not done:
    
        key = win.checkKey()
        if key == 'q':
            done = True
        elif key == 'Left':
            #add something to rot Velocity
            ship.setRotVelocity( ship. getRotVelocity() + gamma )
            ship.setFlickerOn()
        elif key == 'Right':
            ship.setRotVelocity( ship. getRotVelocity() - gamma )
            ship.setFlickerOn()
        elif key == 'space':
            a = ship.getAngle()
            theta = a * math.pi/180.0
            v = ship.getVelocity()
            v[0] += math.cos(theta) * delta
            v[1] += math.sin(theta) * delta
            ship.setVelocity(v)
            ship.setFlickerOn()
        
        movit = False
        p = ship.getPosition()
        
        if p[0] < 0:
            p[0] += win.getWidth()
            movit = True
        elif p[0] > win.getWidth():
            p[0] -= win.Width()
            movit = True
            
        if p[1] < 0:
            p[1] += win.getHeight()
            movit = True
        elif p[1] > win.getHeight():
            p[1] -= win.getHeight()
            movit = True
            
        if movit:
            ship.setPosition( p )
            
        ship.update( dt)
        
        win.update()

    # all done
    win.close()

if __name__ == "__main__":
    main()
