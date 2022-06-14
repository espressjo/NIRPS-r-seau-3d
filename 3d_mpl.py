#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:11:41 2022

@author: noboru
"""
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib.patches import FancyArrowPatch

import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)
def make_pln(pt1,pt2,pt3,pt4,c='g'):
    plt.plot([pt1[0],pt2[0]],[pt1[1],pt2[1]],zs=[pt1[2],pt2[2]],c=c)
    plt.plot([pt2[0],pt3[0]],[pt2[1],pt3[1]],zs=[pt2[2],pt3[2]],c=c)
    plt.plot([pt3[0],pt4[0]],[pt3[1],pt4[1]],zs=[pt3[2],pt4[2]],c=c)
    plt.plot([pt4[0],pt1[0]],[pt4[1],pt1[1]],zs=[pt4[2],pt1[2]],c=c)
    
arrow_prop_dict = dict(mutation_scale=20, arrowstyle='->', shrinkA=0, shrinkB=0)



a = Arrow3D([0, 25], [0, 0], [0, 0], **arrow_prop_dict, color='r')
ax.add_artist(a)
a = Arrow3D([0, 0], [0, 75], [0, 0], **arrow_prop_dict, color='b')
ax.add_artist(a)
a = Arrow3D([0, 0], [0, 0], [0, 8], **arrow_prop_dict, color='g')
ax.add_artist(a)

#plt.ylim([0,0.5])
plt.xlim([-150,10])
ax.set_zlim([-50,1])

#Left Plan

f = 100

#measured left
pt1 = [-88.496,f*0.074,-12.505]
pt2 = [-88.495,f*0.074,-2.504]
pt4 = [ -2.497,f*0.004,-12.507]
pt3 = [ -2.496,f*0.004,-2.505]
make_pln(pt1,pt2,pt3,pt4,c='b')
#theoritical left

pt1 = [-90.152,0.0,-15]
pt2 = [-90.152,0.0,0]
pt4 = [ 0,0.0,-15]
pt3 = [ 0,0.0,0]
make_pln(pt1,pt2,pt3,pt4,c='g')

#theoritical bottom
pt1 = [0,0.0,0]
pt2 = [0,291.912,0]
pt3 = [ 0,291.912,-15]
pt4 = [ 0,0.0,-15.0]
make_pln(pt1,pt2,pt3,pt4,c='g')

#measured bottom
pt1 = [f*-0.011,2.497,-12.505]
pt2 = [f*-0.002,2.497,-2.506]
pt4 = [f*-0.028,290.493,-12.505]
pt3 = [ f*-0.018,290.492,-2.505]
make_pln(pt1,pt2,pt3,pt4,c='b')

#measured top
pt1 = [-90.152+f* (-90.161+90.152),2.496,-12.505]
pt2 = [-90.152+f* (-90.171+90.152),2.497,-2.505]
pt4 = [-90.152+f*(-90.157+90.152),290.490,-12.506]
pt3 = [ -90.152+f* (-90.166+90.152),290.491,-2.505]
make_pln(pt1,pt2,pt3,pt4,c='b')

#theoritical top
pt1 = [ -90.152,0,0]
pt2 = [ -90.152,  291.912,0]
pt3 = [ -90.152,291.912,-15]
pt4 = [ -90.152,0.0,-15.0]
make_pln(pt1,pt2,pt3,pt4,c='g')

#theoritical right

pt1 = [-90.152,291.912,-15]
pt2 = [-90.152,291.912,0]
pt4 = [ 0,291.912,-15]
pt3 = [ 0,291.912,0]
make_pln(pt1,pt2,pt3,pt4,c='g')

#measured right

pt1 = [-88.495,291.912+f*(291.982-291.912),-12.505]
pt2 = [-88.495,291.912+f*(291.987-291.912),-2.504]
pt4 = [ -2.497,291.912+f*(291.914-291.912),-12.505]
pt3 = [ -2.497,291.912+f*(291.916-291.912),-2.505]
make_pln(pt1,pt2,pt3,pt4,c='b')
plt.tight_layout()



plt.show()