#reference https://qiita.com/nnahito/items/ad1428a30738b3d93762
#reference https://nnahito.gitbooks.io/tkinter/content/helloworld/30dc-30bf-30f3-3092-shi-3063-3066-307f-308b/button3092-she-zhi-3057-3066-307f-308b.html
#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import tkinter.font
import InternWork


# ボタンクリック関数
def btn_click():
    # InternWork.py ファイルでスプライトを動かす
    # 引数に🏁ボタン、キャンバス、スプライトを渡す
    InternWork.ChangeSize(Button,canvas,showSpriteImg,spriteImg,500,root)

# スプライトとして使用する猫の画像
spriteImg = "IMAGE\catSprite.png"

root = tkinter.Tk()
# ウィンドウのタイトル
root.title(u"Software Title")
# ウィンドウのサイズ
root.geometry("800x600")
# フォント設定
font = tkinter.font.Font(
    root,
    size = 20)

# ラベルを表示
#Static1 = tkinter.Label(text=u'test')
#Static1.pack()

# テキストボックスを表示
#EditBox = tkinter.Entry()
#EditBox.pack()

# ボタンを表示
Button = tkinter.Button(text=u'🏁',font = font,command=btn_click)
Button.place(x=0,y=0)

# キャンバス作成
canvas = tkinter.Canvas(root, bg="#FFFFFF", height=554, width=800)
# キャンバス表示
canvas.place(x=-2, y=46)

# イメージ作成
img = tkinter.PhotoImage(file=spriteImg, width=200, height=200)

# キャンバスにイメージを表示
showSpriteImg = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)

root.mainloop()