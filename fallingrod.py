Web VPython 3.2
# For those testing out the program, you can change the following variables: theta, lenrod, mass, and increment 

theta = .1# angle measured from the vertical 
thetrad = theta * (pi/180)
lenrod = 1 # length of the rod 
mass = 7.7 # mass of the rod

# ground coordinates
ground = box(pos = vector(0,-5,0), size = vector(10,0.2,1), color = vec(0,1,0))

# coordinates for the pivot of the rod 
base = vector(0,-5,0)

# coordinates for the ball (located at the rightmost end of the rod)
ball = sphere(color = vector(1,0,0), radius = 0.5, opacity = 0)
ball.pos.x = base.x + (lenrod * sin(thetrad))
ball.pos.y = base.y + (lenrod * cos(thetrad))
ball_pos = vector(ball.pos.x, ball.pos.y, 0)

# coordinates for the ENTIRE rod 
rod = cylinder(pos = base, axis = ball.pos-base, radius = 0.20)


increment = 0.01 # how much the angle changes as the rod falls 
changeinangle = increment * (pi/180)
angularvelocity = 0 #INITIAL angular velocity 
g = 9.8
totaltime = 0 
angle = theta 
time = 0
sleep(5)
print("Start")
t1= clock() # gets the current time of the computer (before the loop)

while angle <= 90: # loop that represents the falling rod 
  anglerad = angle * (pi/180)
  angacc = (1.5 * g * sin(anglerad) * mass)/(lenrod * mass) # calculates angular acceleration in the angle interval
  finalangvel = sqrt((angularvelocity*angularvelocity) + (2 * angacc * changeinangle)) # calculates final angular velocity in the angle interval
  time = (finalangvel - angularvelocity)/angacc # calculates time for the rod to fall in each angle interval 
  sleep(time) # program will wait before position of the rod changes 
  
  # lines 42-45: changing the position of the rod 
  if ball.pos.y > base.y:
      ball.pos.x = base.x + (lenrod * sin(anglerad))
      ball.pos.y = base.y + (lenrod * cos(anglerad))
  rod.axis = ball.pos-base
  
  angularvelocity = finalangvel # updating the angular velocity 
  totaltime = totaltime + time # keeping track of the total time for rod to fall to the ground 
  angle = angle + increment # angle measured from the vertical changes

print("actual time of rod falling: ", totaltime, "s")

t2 = clock() # gets the current time of the computer (after the loop)
print("computer program execution time: ", t2-t1, "s")

