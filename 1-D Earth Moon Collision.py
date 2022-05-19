#!/usr/bin/env python
# coding: utf-8

# Name: Sunil Adhikari
# 
# 
# This project was fun; I love doing it. There was a time when I spent entire night on figuring out what I did wrong inside the while loop because I was getting some errors. Then, I learnt something new that we can not multiply float with string. Also, realized that to get my model done in vpython, I have to assume a 3-D putting the unrelated axis zero. Changing non vector to vector and multiplying magnitude of the vector only. Second challenging thing I encountered was getting the texture of the moon. I do not know how to get the real moon's texture like I did for the earth. Thus, I assumed the texture of the moon as that of the rock. At first, I had my vp.rate the real one, which is very slow to observe in the class. It would take 5 days to see if the moon hits the earth. Tehn, I changed it to 10,000. Now, the motion of the moon is pretty observable. We can see the collision within a few seconds. 
# While doing this project I learnt how to worite vectors quantity in python. The formula we got from physics is also a good reminder for me about the attraction force between moon and earth. But that is the basic thing we all already knew about it. However, I learnt how python reads the mathematical formula.
# The graph part, I still did not get it right. I tried everything I knew, still did not work. I tried same logic to Moon orbiting earth project to generate graphs, it worked there but due to some reasons, my vp.rate is giving me issue. If I do not use vp on my rate, that means, if I use rat(500), I can see my simulation. But as soon as I put vp.rate, there is no simulation, and forget about the graph. Graph part have become mystery to me for this project only though.

# In[1]:



""" 
me = mass of the earth
mm = mass of the moon
re = radius of the earth
rm = radius of the moon
Xe = position of the earth from center of mass of the system
Xm = position of the moon from center of mass of the system

"""



# In[ ]:


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





    


# In[ ]:





# In[ ]:




