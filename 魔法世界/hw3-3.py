from mcpi.minecraft import Minecraft
mc=Minecraft.create()

for i in range(20):
    x,y,z=mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,20)
x,y,z=mc.player.getPos()
mc.setBlocks(x+20,y,z,x+30,y+15,z+10,57)
mc.setBlocks(x+21,y+1,z+1,x+29,y+14,z+9,0)