# Anthony Gatti
# Spring 2020
# Project 10

import graphicsPlus as gr
import math

class Thing:
    '''Parent class for simulated objects'''
    def __init__(self, win, the_type, position = [0,0], velocity=[0,0], acceleration=[0,0], color = 'red', elasticity=0):
        
        self.win = win
        self.the_type = the_type
        self.position = [ position[0], position[1] ]
        self.velocity = [ velocity[0], velocity[1] ]
        self.acceleration = [ acceleration[0], acceleration[1] ]
        self.color = color
        self.elasticity = elasticity
        self.drawn = False
        self.shapes = []
        
    def getType(self):
        return self.the_type
    
    def getPosition(self):
        '''Gets the position of the thing'''
        return self.position[:]

    def getVelocity(self):
        '''Gets the velocity of the thing'''
        return self.velocity[:]
        
    def getAcceleration(self):
        '''Gets the acceleration of the thing'''
        return self.acceleration[:]
        
    def getElasticity(self):
        '''Gets the radius of the thing'''
        return self.elasticity
        
    def getColor(self):
        '''Gets the color of the thing'''
        return self.color

    def draw(self):
        '''Draws the thing if not already drawn'''
        # if the objects are not drawn, draw the Zelle graphics shapes into the window
        drawn = self.drawn
        if not drawn:
            for x in self.shapes:
                x.draw(self.win)
        # set the drawn field to True
        self.drawn = True

    def undraw(self):
        '''Undraws the thing if already drawn'''
        # if the objects are drawn, undraw the Zell graphics objects
        drawn = self.drawn
        if drawn:
            for x in self.shapes:
                x.undraw()
        # set the drawn field to False
        self.drawn = False

    def setPosition(self, pos):
        '''Sets the position of the thing'''
        # assign to x_old the current x position
        '''x_old = self.position[0]'''
        # assign to y_old the current y position
        '''y_old = self.position[1]'''
        old_pos = self.position
        # assign to the x coordinate in self.pos the new x coordinate
        '''self.position[0] = pos[0]'''
        # assign to the y coordinate in self.pos the new y coordinate
        '''self.position[1] = pos[1]'''
        self.position = pos[:]
        
        # assign to dx the new x position - the old x position
        dx = self.position[0] - old_pos[0]
        # assign to dy the new y position - the old y position
        dy = self.position[1] - old_pos[1]

        # for each item in the shapes list field of self
        for x in self.shapes:
            # call the move method of the item, passing in dx and -dy
            x.move( dx, -dy )
            
    def setVelocity(self, vel): # vel is a 2-element list with vx and vy
        '''Sets the velocity of the thing'''
        # code here
        self.velocity = vel[:]
        
    def setAcceleration(self, acc): # vel is a 2-element list with vx and vy
        '''Sets the acceleration of the thing'''
        # code here
        self.acceleration = acc[:]
    
    def setElasticity( self, elas ):
        '''Sets the radius of the thing'''
        # code here: update the ball's radius information then call ball_render
        self.elasticity = elas
        self.render()
        
    def setColor(self, c): # color is a Zelle color or a string
        '''Sets the color of the thing'''
        # code here
        self.color = c
        for x in self.shapes:
            x.setFill(c)

    def update(self, dt):
        '''Updates the thing'''
        # assign to dx the x motion = x_vel*dt + 0.5*x_acc*dt*dt
        dx = self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt
        # assign to dy the y motion = y_vel*dt + 0.5*y_acc*dt*dt
        dy = self.velocity[1]*dt + 0.5*self.acceleration[0]*dt*dt
        
        # increment the x position by dx
        self.position[0] += dx
        # increment the y position by dy
        self.position[1] += dy

        # increment the x velocity by adding the acceleration times dt
        self.velocity[0] += self.acceleration[0]*dt
        # increment the y velocity by adding the acceleration times dt
        self.velocity[1] += self.acceleration[1]*dt

        # for each item in the shapes list
        for x in self.shapes:
            # call the move method of the graphics object with dx and -dy as arguments
            x.move(dx, -dy)

class Ball(Thing):

    def __init__(self, win, radius, position=[0,0], velocity=[0,0], acceleration=[0,0], color = 'red', elasticity=1.0):
    
        Thing.__init__( self, win, "ball", position, velocity, acceleration, color, elasticity)
    
        self.radius = radius
        
        self.render()
        
    def render(self):
        '''Renders the Ball object'''
        # Assign the drawn field to a local variable
        drawn = self.drawn
        pt = gr.Point(self.position[0], self.win.getHeight() - self.position[1])

        # if the ball is drawn
        if drawn:
            # call the ball's undraw method (e.g. self.undraw()
            self.undraw()
        # create a new Zelle Circle object using the appropriate position and radius
        circle = gr.Circle(pt, self.radius)
        # set the Circle object's color using the color field
        circle.setFill( self.color )
        # assign to the shapes field the Circle object in a list
        self.shapes = []
        
        self.shapes.append(circle)
        
        # if the ball is drawn
        if drawn:
            # call the ball's draw method
            self.draw()
        
    def getRadius(self):
        '''Gets the radius of the ball'''
        return self.radius
        
    def setRadius( self, rad ):
        '''Sets the radius of the ball'''
        # code here: update the ball's radius information then call ball_render
        self.radius = rad
        self.render()
        
class Block(Thing):

    def __init__(self, win, width, height, position=[0,0], velocity=[0,0], acceleration=[0,0], color = 'red', elasticity=1.0):
    
        Thing.__init__( self, win, "block", position, velocity, acceleration, color, elasticity)
        
        self.width = width
        self.height = height
        
        self.render()
    
    def render(self):
        '''Renders the block'''
        drawn = self.drawn
        if drawn:
            self.undraw()
            
        wid = self.width
        heigh = self.height
        pos = self.position
        posx = pos[0]
        posy = pos[1]
        win = self.win
        pt1 = gr.Point(posx - wid/2, win.getHeight() - (posy - heigh/2))
        pt2 = gr.Point(posx + wid/2, win.getHeight() - (posy + heigh/2))
        
        block = gr.Rectangle( pt1, pt2 )
        
        block.setFill( self.color )

        self.shapes = []

        
        self.shapes.append(block)

        
        if drawn:
            self.draw()
            
    def getWidth(self):
        '''Gets the width of the block'''
        dx = self.width
        return dx

    def getHeight(self):
        '''Gets the height of the block'''
        dy = self.height
        return dy
        
    def setWidth( self, width ):
       '''Sets the width of the block'''
       # code here: update the ball's radius information then call ball_render
       self.width = width
       self.render()
       
    def setHeight( self, height ):
       '''Sets the height of the block'''
       # code here: update the ball's radius information then call ball_render
       self.height = height
       self.render()
       
    def setColor(self, color): # color is a Zelle color or a string
        '''Sets the color of the block'''
        # code here
        self.color = color
        self.render(self.shapes)
        
class Triangle(Thing):
    
    def __init__(self, win, radius, position=[0,0], velocity=[0,0], acceleration=[0,0], color = 'red', elasticity=1.0):

        Thing.__init__( self, win, "triangle", position, velocity, acceleration, color, elasticity)

        self.radius = radius
        self.width = radius
        
        self.render()
        
    def render(self):
        '''Renders the Triangle'''
        drawn = self.drawn
        if drawn:
            self.undraw()
            
        rad = self.radius*2
        wid = self.width
        pos = self.position
        posx = pos[0]
        posy = pos[1]
        win = self.win
        pt1 = gr.Point(posx - rad, win.getHeight() - (posy - rad))
        pt2 = gr.Point(posx + rad, win.getHeight() - (posy - rad))
        pt3 = gr.Point(posx , win.getHeight() - (posy + rad))
        
        triangle = gr.Polygon( pt1, pt2, pt3 )
        
        triangle.setFill( self.color )

        self.shapes = []

        
        self.shapes.append(triangle)

        
        if drawn:
            self.draw()
       
    def setColor(self, color): # color is a Zelle color or a string
        '''Sets the color of the triangle '''
        # code here
        self.color = color
        self.render(self.shapes)
        
    def getRadius(self):
        '''Gets the radius of the triangle'''
        return self.radius
        
    def setRadius( self, rad ):
        '''Sets the radius of the triangle'''
        # code here: update the ball's radius information then call ball_render
        self.radius = rad
        self.render()

class RotatingBlock(Thing):
    
    def __init__(self, win, width, height, pos=[0,0], anchor = None, color ='black'):
            
        Thing.__init__( self, win, "rotating block", pos, color=color )
        
        self.win = win
        self.pos = pos[:]
        self.width = width
        self.height = height
        if anchor != None:
            self.anchor = anchor[:]
        else:
            self.anchor = pos[:]
        self.points = []
        self.angle = 0
        self.rvel = 0
        self.color = color
        
        self.render()
            
    def render(self):

    # assign to a local variable (e.g. drawn) the value in self.drawn
        drawn = self.drawn
      # if drawn
        if drawn:
          # call the undraw method
            self.undraw()

      # assign to self.points a list with two 2-element sublists that
      #      define the end points of the line relative to the position
      #      The endpoints will be [(-width/2, -height/2), (width/2, -height/2), (width/2, height/2), (-width/2, height/2)]
        self.points = [(-self.width/2, -self.height/2), (self.width/2, -self.height/2), (self.width/2, self.height/2), (-self.width/2, self.height/2)]

      # assign to theta the result of converting self.angle from degrees to radians
        theta = self.angle*math.pi/180.0
      # assign to cth the cosine of theta
        cth = math.cos(theta)
      # assign to sth the sine of theta
        sth = math.sin(theta)
      # assign to pts the empty list
        pts = []
      
      # for each vertex in self.points
        for pt in self.points:
        # (2 lines of code): assign to x and y the result of adding the vertex to self.pos and subtracting self.anchor
            x = pt[0] + self.pos[0] - self.anchor[0]
            y = pt[1] + self.pos[1] - self.anchor[1]

        # assign to xt the calculation x * cos(theta) - y * sin(theta) using your precomputed cos/sin values above
            xt = x * math.cos(theta) - y * math.sin(theta)
            # assign to yt the calculation x * sin(theta) + y * cos(theta)
            yt = x * math.sin(theta) + y * math.cos(theta)
            # (2 lines of code): assign to x and y the result of adding xt and yt to self.anchor
            x = xt + self.anchor[0]
            y = yt + self.anchor[1]

            # append to pts a Point object with coordinates (x, self.win.getHeight() - y)
            pts.append(gr.Point(x, self.win.getHeight() - y))

          # assign to self.shapes a list containing a Zelle graphics Line object using the Point objects in pts
        self.shapes = [gr.Polygon(pts[0], pts[1], pts[2], pts[3])]
        self.shapes[0].setFill(self.color)

      # if drawn
        if drawn:
          # call the draw method
            self.draw()
            
    def getWin(self):
        '''Gets the window'''
        return self.win
        
    def setColor(self, color): # color is a Zelle color or a string
        '''Sets the color of the rotating block '''
        # code here
        self.color = color
        self.render()

    def getAngle(self):
        '''Gets the angle of the rotating block'''
        return self.angle
        
    def getAnchor(self):
        '''Gets the anchor of the rotating block'''
        return self.anchor[:]
        
    def getRotVelocity(self):
        '''Gets the rotating velocity of the rotating block'''
        return self.rvel

    def getWidth(self):
        '''Gets the width of the rotating block'''
        dx = self.width
        return dx

    def getHeight(self):
        '''Gets the height of the rotating block'''
        dy = self.height
        return dy
        
    def setAngle(self, angle):
        '''Sets the angle of the rotating block'''
        self.angle = angle
        self.render()
        
    def setAnchor(self, anchor):
        '''Sets the anchor of the rotating block'''
        self.anchor = anchor
        self.render()
        
    def setRotVelocity(self, vel):
        '''Sets the velocity of the rotating block'''
        self.rvel = vel
        
    def setWidth( self, width ):
       '''Sets the width of the rotating block'''
       # code here: update the ball's radius information then call ball_render
       self.width = width
       self.render()
       
    def setHeight( self, height ):
       '''Sets the height of the rotating block'''
       # code here: update the ball's radius information then call ball_render
       self.height = height
       self.render()
       
    def rotate(self, da):
        '''Rotates the rotating block by said amount'''
        self.angle += da
        self.render()

    def update(self, dt):
        '''Updates the Rotating Block'''
        da = self.rvel * dt
        if da != 0:
            self.rotate(da)
            Thing.update(self, dt)
       
