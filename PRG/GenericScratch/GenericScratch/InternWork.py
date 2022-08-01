
# **********編集不可の始め**********
import MakedMethod

def StartWork(root,Button,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight):
    # メソッド群のインスタンス生成
    pc= MakedMethod.PropertyClass(root,Button,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight)
    # 開始ボタンは１度だけ押すことができる
    Button["state"] = "disable"
# **********編集不可の終わり**********

    # **********インターン生は以下を編集の始め**********
    root.after(100,pc.ChangeXCoord,100)
    # **********インターン生は以下を編集の終わり*******




# **********編集不可の始め**********
def StartWorkSprite(root,Button,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight):
    # メソッド群のインスタンス生成
    pc= MakedMethod.PropertyClass(root,Button,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight)
# **********編集不可の終わり**********

    # **********インターン生は以下を編集の始め**********
    pc.ChangeXCoord(100)
    if pc.TouchEdge():
        print("kkkkkkkk")
    else:
        print("bbbbbbbb")
    # **********インターン生は以下を編集の終わり*******

