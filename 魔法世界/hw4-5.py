from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange

answer=randrange(0,16)
myID=mc.getPlayerEntityId('jerry213')

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hits=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        
        if data>answer:
            mc.postToChat('你錯了')
        elif data<answer:
            mc.postToChat('你錯了')
        elif:
            mc.st
            mc.postToChat('你錯了')
        
            