from mcpi.minecraft import Minecraft
mc=Minecraft.create()

Line1=[]
Line2=[]
Line3=[]

for i in range(1,4):
    Line1.append(3*i)
for i in range(1,6):
    Line2.append(4*i)
for i in range(3,9):
    Line3.append(5*i)
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,8,str(Line1),str(Line2),str(Line3))