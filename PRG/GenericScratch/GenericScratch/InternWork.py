
# **********編集不可の始め**********
import MakedMethod

def StartWork(Button,canvas,showSpriteImg):
    # メソッド群のインスタンス生成
    pc= MakedMethod.PropertyClass(Button,canvas,showSpriteImg)
    # 開始ボタンは１度だけ押すことができる
    Button["state"] = "disable"
# **********編集不可の終わり**********

    # **********インターン生は以下を編集**********
    pc.Walk(100)

