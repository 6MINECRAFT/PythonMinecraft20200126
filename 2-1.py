from mcpi.minecraft import Minecraft
DD=Minecraft.create()

x,y,z=DD.player.getTilePos()
DD.setBlock(x,y,z+1,57)
DD.setBlock(x,y,z-1,57)
DD.setBlock(x+1,y,z+1,57)
DD.setBlock(x-1,y,z+1,57)
DD.setBlock(x-1,y,z-1,57)
DD.setBlock(x+1,y,z-1,57)
DD.setBlock(x-1,y,z,57)
DD.setBlock(x+1,y,z,57)