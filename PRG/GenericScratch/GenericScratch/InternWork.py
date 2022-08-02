
# **********編集不可の始め**********
import MakedMethod

def StartWork(root,Button,label,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight):
    # メソッド群のインスタンス生成
    pc= MakedMethod.PropertyClass(root,Button,label,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight)
    # 開始ボタンは１度だけ押すことができる
    Button["state"] = "disable"
# **********編集不可の終わり**********

    # **********インターン生は以下を編集の始め**********
    root.after(100,pc.ChangeXCoord,100)
    # 1秒後にタイマーを進め始める
    root.after(1000, pc.repeat_func)
    # **********インターン生は以下を編集の終わり*******




# **********編集不可の始め**********
def StartWorkSprite(root,Button,label,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight):
    # メソッド群のインスタンス生成
    pc= MakedMethod.PropertyClass(root,Button,label,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight)
# **********編集不可の終わり**********

    # **********インターン生は以下を編集の始め**********
    pc.DownPen()
    pc.ChangePenColor("Blue")
    pc.ChangePenSize(10)
    pc.ChangeXCoord(100)
    pc.ChangePenColor("Red")
    pc.ChangePenSize(2)
    pc.ChangeYCoord(100)
    pc.UpPen()
    if pc.TouchEdge():
        print("kkkkkkkk")
    else:
        print("bbbbbbbb")
    # **********インターン生は以下を編集の終わり*******

