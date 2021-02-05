from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
y=720
z=920
x=755
time.sleep(5)
mc.player.setTilePos(x,y,z)
time.sleep(5)
mc.player.setTilePos(x,y,z+50)
time.sleep(5)
mc.player.setTilePos(x,y-150,z)


