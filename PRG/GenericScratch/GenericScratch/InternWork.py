
# **********編集不可の始め**********
import MakedMethod

def StartWork(root,Button,canvas,showSpriteImg,spriteImg):
    # メソッド群のインスタンス生成
    pc= MakedMethod.PropertyClass(root,Button,canvas,showSpriteImg,spriteImg)
    # 開始ボタンは１度だけ押すことができる
    Button["state"] = "disable"
# **********編集不可の終わり**********

    # **********インターン生は以下を編集**********
    root.after(100,pc.Walk,100)

