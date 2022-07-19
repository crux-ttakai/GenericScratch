def StartWork(Button,canvas,showSpriteImg):
    # スプライトをX軸方向に100動かす
    canvas.move(showSpriteImg, 100, 0)
    # 開始ボタンは１度だけ押すことができる
    Button["state"] = "disable"