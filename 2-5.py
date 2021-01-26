from mcpi.minecraft import Minecraft
DD=Minecraft.create()
while True:
    x,y,z,=DD.player.getTilePos()
    b1=DD.getBlock(x,y-1,z)
    b2=DD.getBlock(x+1,y-1,z)
    b3=DD.getBlock(x-1,y-1,z)
    b4=DD.getBlock(x,y-1,z+1)
    b5=DD.getBlock(x,y-1,z-1)
    b6=DD.getBlock(x+1,y-1,z+1)
    b7=DD.getBlock(x-1,y-1,z+1)
    b8=DD.getBlock(x+1,y-1,z-1)
    b9=DD.getBlock(x-1,y-1,z-1)
    if b1==8 or b1==9 or b2==9 or b2==8 or b3==9 or b3==8\
    or b4==9 or b4==8 or b5==9 or b5==8 or b6==9 or b6==8\
    or b7==9 or b7==8 or b8==9 or b8==8 or b9==9 or b9==8:
        DD.setBlock(x,y-1,z,79)
        DD.setBlock(x+1,y-1,z,79)
        DD.setBlock(x-1,y-1,z,79)
        DD.setBlock(x,y-1,z-1,79)
        DD.setBlock(x,y-1,z+1,79)
    
