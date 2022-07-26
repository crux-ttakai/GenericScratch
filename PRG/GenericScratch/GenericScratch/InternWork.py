#def StartWork(Button,canvas,showSpriteImg):
    # スプライトをX軸方向に100動かす
    #canvas.move(showSpriteImg, 100, 0)
    # 開始ボタンは１度だけ押すことができる
    #Button["state"] = "disable"


import tkinter
import time
from PIL import Image,ImageTk

def ChangeXCoord(Button,canvas,showSpriteImg,ChangeCoord):
    #スプライトをX座標方向に受け取った引数分(ChangeCoord)移動する
    canvas.move(showSpriteImg,ChangeCoord,0)
    # 開始ボタンは１度だけ押すことができる
    Button["state"] = "disable"

def ChangeYCoord(Button,canvas,showSpriteImg,ChangeCoord):
    #スプライトをY座標方向に受け取った引数分(ChangeCoord)移動する
    canvas.move(showSpriteImg,0,ChangeCoord)
    # 開始ボタンは１度だけ押すことができる
    Button["state"] = "disable"



def ChangeSize(Button,canvas,showSpriteImg,spriteImg,size,root):
    #画像ファイルを開く（GenericScratchファイルから持ってくる）
    img = Image.open(spriteImg)
    #サイズの拡大縮小処理
    img_process = img.resize((size,size))
    #PhotoImageに変換
    img_PhotoImage = ImageTk.PhotoImage(img_process)
    #元あった画像ファイルを削除
    canvas.delete(showSpriteImg)
    #拡大縮小処理した画像ファイルを表示
    canvas.create_image(0,0,image=img_PhotoImage,anchor=tkinter.NW)
    #ボタンを非活性
    Button["state"] = "disable"
    #ページの更新
    root.mainloop()


    


def Rebound(Button,canvas,showSpriteImg,spriteImg,root):
    #画像ファイルを開く（上メソッドと同様、引数として受け取り）
    img = Image.open(spriteImg)
    #左右反転処理
    img_process = img.transpose(Image.FLIP_LEFT_RIGHT)
    #PhotoImageに変換
    img_PhotoImage = ImageTk.PhotoImage(img_process)
    #元あった画像ファイルを削除
    canvas.delete(showSpriteImg)
    #左右反転処理した画像ファイルを表示
    canvas.create_image(0,0,image=img_PhotoImage, anchor=tkinter.NW)
    #ボタンを非活性
    Button["state"] = "disable"
    #ページの更新
    root.mainloop()
    

def Turn(Button,canvas,showSpriteImg,spriteImg,angle,root):
    #画像ファイルを開く（上メソッドと同様、引数として受け取り）
    img = Image.open(spriteImg)
    #時計回りに90度回転
    img_process = img.rotate(angle*-1)
    #PhotoImageに変換
    img_PhotoImage = ImageTk.PhotoImage(img_process)
    #元あった画像ファイルを削除
    canvas.delete(showSpriteImg)
    #回転させた画像ファイルを表示
    canvas.create_image(0,0,image=img_PhotoImage, anchor=tkinter.NW)
    #ボタンを非活性
    Button["state"] = "disable"
    #ページの更新
    root.mainloop()
    