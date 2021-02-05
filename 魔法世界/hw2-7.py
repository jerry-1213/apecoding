from mcpi.minecraft import Minecraft
mc=Minecraft.create()

a= input('你是誰?')
mc.postToChat('你好'+a+'我送你一棟房子')
x,y,z=mc.player.getPos()
mc.setBlocks(x,y,z,x+20,y+30,z+30,1)
mc.setBlocks(x+1,y+1,z+1,x+19,y+29,z+29,0)






mc.setBlocks(x+6,y+1,z,x+6,y+2,z,0)
mc.setBlocks(x+1,y+4,z+1,x+9,y+4,z+9,20)