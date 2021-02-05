from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random

x,y,z=mc.player.getPos()

for i in range(10):
    for j in range(10):
       color=random.randrange(0,16)
       mc.setBlock(x+i,y-1,z+j,35,color)