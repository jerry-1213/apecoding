from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
numder=1

time.sleep(5)
for i in range(4):
    for i in range(numder):
        mc.spawnEntity(x,y,z,32)
        numder*=2