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
    InternWork.StartWork(root,Button,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight)

# スプライトクリック関数
def pressedSprite(event):
    # InternWork.py ファイルでスプライトを動かす
    # 引数に🏁ボタン、キャンバス、スプライトを渡す
    InternWork.StartWorkSprite(root,Button,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight)
    print("aaa")

# スプライトとして使用する猫の画像
spriteImg = "IMAGE\catSprite.png"
# 画面幅
WindowWidth = 800
# 画面高さ
WindowHeight = 600
# スプライト幅
SpriteWidth = 200
# スプライト高さ
SpriteHeight = 200

root = tkinter.Tk()
# ウィンドウのタイトル
root.title(u"Software Title")
# ウィンドウのサイズ
root.geometry("{0}x{1}".format(WindowWidth, WindowHeight))
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
img = tkinter.PhotoImage(file=spriteImg, width=SpriteWidth, height=SpriteHeight)

# キャンバスにイメージを表示
showSpriteImg = canvas.create_image(0, 0, image=img, anchor=tkinter.NW, tags="sprite")
# スプライトがクリックされたとき
canvas.tag_bind("sprite", "<ButtonPress-1>", pressedSprite)

root.mainloop()