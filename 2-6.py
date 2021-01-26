from mcpi.minecraft import Minecraft
DD=Minecraft.create()
x,y,z,=DD.player.getTilePos()
answer=int(input("請問要放甚麼方塊:"))
DD.setBlock(x,y,z,answer)