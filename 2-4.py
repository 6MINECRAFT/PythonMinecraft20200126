from mcpi.minecraft import Minecraft
DD=Minecraft.create()
x,y,z,=DD.player.getTilePos()

long=10
big=9
high=6

block=46
air=0

DD.setBlocks(x,y,z,x+long,y+big,z+high,46)
DD.setBlocks(x+1,y+1,z+1,x+long-1,y+big-1,z+high-1,air)