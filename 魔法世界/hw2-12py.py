from mcpi.minecraft import Minecraft
import random
import time
mc=Minecraft.create()
x,y,z=mc.player.getPos()
y-=1

while True:
    color=random.randrange(0,16)
    mc.setBlocks(x-10,y,z-10,x+10,y,z+10,95,color)
    mc.setBlocks(x-10,y,z-10,x+10,y,z+10,95,color)
    time.sleep(5)