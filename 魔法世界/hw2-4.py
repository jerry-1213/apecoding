from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time
while True:
    x,y,z=mc.player.getPos()
    color=random.randrange(0,9)
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.1)