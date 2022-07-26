# **********編集不可の始め**********
import MakedMethod

def StartWork(root,Button,canvas,showSpriteImg,spriteImg):
    # メソッド群のインスタンス生成
    pc= MakedMethod.PropertyClass(root,Button,canvas,showSpriteImg,spriteImg)
    # 開始ボタンは１度だけ押すことができる
    Button["state"] = "disable"
# **********編集不可の終わり**********

    # **********インターン生は以下を編集**********
    #pc.DownloadSprite()
    pc.SetBackground("IMAGE\image.png")
    pc.Walk(100)
    pc.AddSprite("IMAGE\elephant.png")