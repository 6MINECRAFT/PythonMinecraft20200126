from mcpi.minecraft import Minecraft
DD=Minecraft.create()

x,y,z,=DD.player.getTilePos()
DD.setSign(x+2,y,z,63,0,"我愛MIinecraft,也愛Python")