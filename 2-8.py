from mcpi.minecraft import Minecraft
DD=Minecraft.create()

userName=input("請輸入姓名")
message=input("輸入發言")
DD.postToChat(" <"+userName + "> " + message)