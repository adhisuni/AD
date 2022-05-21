One dimensional model of Earth-Moon Collision
""" 
me = mass of the earth
mm = mass of the moon
re = radius of the earth
rm = radius of the moon
Xe = position of the earth from center of mass of the system
Xm = position of the moon from center of mass of the system

"""
import numpy as np
from math import *
import vpython as vp
from scipy.constants import G, pi

### the parameters we know regarding Earth and Moon are:

me = 5.97 * 10**24

mm = 7.35 * 10**22
re = 6.4 * 10**6
rm = 1.35 * 10**6
Xe = vp.vec(4.69*10**6,0,0)
Xm = vp.vec(3.181*10**8,0,0)

R_apo = 4.054 * 10**8
R_peri = 3.62*10**8
### We need to think about the vector and dimensions while creating this simulation. So, for acceleration or velocity we need to focus on vectors
### Condition given by question:
t = 0
dt = 0.5
T = 27.3               ## average period of moon to orbit the earth

scene = vp.canvas()
ve = vp.vec(0,0,0) # this is the earth's initial velocity when the earth is not moving at all
vm = vp.vec(0,0,0)

F = - G * me * mm / vp.mag(Xm)**2 #### this is force of gravitation formula which will further assis us to find 'a'

ae = vp.vec(-G*mm/vp.mag(Xm-Xe)**2,0,0)
am = vp.vec(-G*me/vp.mag(Xm-Xe)**2, 0, 0)
### Creating graphs for the moon's displacement vs earth's displacement:

Position_plot = vp.graph( x=0, y=0, width=600, height=600,
                       xmin=-4.5e8, xmax=4.5e8,
                       ymin=-4.5e8, ymax=4.5e8,
                       foreground=vp.color.black,
                       background=vp.color.white,
                       title='Xm(t) vs. t',
                       xtitle='Xm',
                       ytitle='t')

f1= vp.gcurve(color = vp.color.black)

Position_plot2 = vp.graph( x=0, y=0, width=600, height=600,
                       xmin=-3.1e8, xmax=3.1e8,
                       ymin=-3.1e8, ymax=3.1e8,
                       foreground=vp.color.black,
                       background=vp.color.white,
                       title='Xe vs. t',
                       xtitle='Xe',
                       ytitle='t')
f2 = vp.gcurve(color = vp.color.red)
###Designing objects such as earth and moon

Earth =vp.sphere(pos=Xe,
              vel=ve,
              acc=ae,
              texture=vp.textures.earth,
              radius=re)
#### Designing the moon
Moon = vp.sphere(pos = Xm,
                vel=vm,
                acc=am,
                textures=vp.textures.rock,
                radius=rm)

while True:
    
    vp.rate(7000)
   
    
    F_m= ((F/mm)/vp.mag(Moon.pos)**2,0,0)
    Moon.acc = vp.vec(-G*me/vp.mag(Xm-Xe)**2, 0, 0) 
    Moon.vel = Moon.vel + Moon.acc * dt
    Moon.pos = Moon.pos + Moon.vel * dt
    F_e= ((F/me)/vp.mag(Xe)**2,0,0)
    Earth.acc = vp.vec(-G*mm/vp.mag(Xm-Xe)**2,0,0)
    Earth.vel = Earth.vel + Earth.acc * dt
    Earth.pos = Earth.pos + Earth.vel * dt
    
   
    t = t + dt 


####    f1.plot(t, Moon.pos)
 ####   f2.plot(t, Earth.pos) these plots are supposed to be inside the while loop right above the t = t+dt.
### there is some isssues that everytime I put them into their right place in the loop, python detects error on vp.rate.
## But vp.rate is already working when I don't put plot functions inside the loop. I did not understand what's going on.
    
### I left like this, at least, I have a complete code along with simulation. My next project shows that I can do graphs as 
## well.
