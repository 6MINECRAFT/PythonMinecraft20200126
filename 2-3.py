from mcpi.minecraft import Minecraft
DD=Minecraft.create()

import random,time
while True:
    x,y,z=DD.player.getTilePos()
    color=random.randrange(0,16)
    DD.setBlocks(x+6,y-1,z+10,x-6,y-1,z-10,95,color)
    time.sleep(0.5)
                                                              
