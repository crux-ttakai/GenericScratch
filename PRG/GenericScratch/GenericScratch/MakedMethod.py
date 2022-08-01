from telnetlib import EL
from tkinter import Image
from PIL import Image,ImageTk
import tkinter
from pickle import FALSE
import winsound
import time
from tkinter import messagebox
import tkinter.simpledialog

class PropertyClass:
    # インスタンス生成時にプロパティに🏁ボタン、キャンバス、スプライトを設定
    def __init__(self,root,button,canvas,showSpriteImg,spriteImg,windowWidth,windowHeight,spriteWidth,spriteHeight):
        self.root = root
        self.button = button
        self.canvas = canvas
        self.showSpriteImg = showSpriteImg
        self.spriteImg = spriteImg
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.spriteWidth = spriteWidth
        self.spriteHeight = spriteHeight
    
    # プロパティ
    @property
    def root(self):
        return self.__root
    @root.setter
    def root(self, value):
        if value != '':
            self.__root = value

    @property
    def button(self):
        return self.__button
    @button.setter
    def button(self, value):
        if value != '':
            self.__button = value
    
    @property
    def canvas(self):
        return self.__canvas
    @canvas.setter
    def canvas(self, value):
        if value != '':
            self.__canvas = value
    
    @property
    def showSpriteImg(self):
        return self.__showSpriteImg
    @showSpriteImg.setter
    def showSpriteImg(self, value):
        if value != '':
            self.__showSpriteImg = value
    
    @property
    def spriteImg(self):
        return self.__spriteImg
    @spriteImg.setter
    def spriteImg(self, value):
        if value != '':
            self.__spriteImg = value

    @property
    def spriteImg(self):
        return self.__spriteImg
    @spriteImg.setter
    def spriteImg(self, value):
        if value != '':
            self.__spriteImg = value

    @property
    def flgMessage(self):
        return self.__flgMessage
    @flgMessage.setter
    def flgMessage(self, value):
        if value != '':
            self.__flgMessage = value

    @property
    def windowWidth(self):
        return self.__windowWidth
    @windowWidth.setter
    def windowWidth(self, value):
        if value != '':
            self.__windowWidth = value

    @property
    def windowHeight(self):
        return self.__windowHeight
    @windowHeight.setter
    def windowHeight(self, value):
        if value != '':
            self.__windowHeight = value

    @property
    def spriteWidth(self):
        return self.__spriteWidth
    @spriteWidth.setter
    def spriteWidth(self, value):
        if value != '':
            self.__spriteWidth = value

    @property
    def spriteHeight(self):
        return self.__spriteHeight
    @spriteHeight.setter
    def spriteHeight(self, value):
        if value != '':
            self.__spriteHeight = value

    # **********以下、作成メソッド**********
    # 各パーツは以下の書き方で参照
    # 🏁ボタン：self.button
    # キャンバス：self.canvas
    # スプライト：self.showSpriteImg

    def ChangeXCoord(self,ChangeCoord):
        #スプライトをX座標方向に受け取った引数分(ChangeCoord)移動する
        self.canvas.move(self.showSpriteImg,ChangeCoord,0)

    def ChangeYCoord(self,ChangeCoord):
        #スプライトをX座標方向に受け取った引数分(ChangeCoord)移動する
        self.canvas.move(self.showSpriteImg,0,ChangeCoord)

    def ChangeSize(self,size):
        #画像ファイルを開く（GenericScratchファイルから持ってくる）
        img = Image.open(self.spriteImg)
        #サイズの拡大縮小処理
        img_process = img.resize((size,size))
        #PhotoImageに変換
        img_PhotoImage = ImageTk.PhotoImage(img_process)
        #元あった画像ファイルを削除
        self.canvas.delete(self.showSpriteImg)
        #拡大縮小処理した画像ファイルを表示
        self.canvas.create_image(0,0,image=img_PhotoImage,anchor=tkinter.NW)
        #ページの更新
        self.root.mainloop()
        
    def Rebound(self):
        #画像ファイルを開く（上メソッドと同様、引数として受け取り）
        img = Image.open(self.spriteImg)
        #左右反転処理
        img_process = img.transpose(Image.FLIP_LEFT_RIGHT)
        #PhotoImageに変換
        img_PhotoImage = ImageTk.PhotoImage(img_process)
        #元あった画像ファイルを削除
        self.canvas.delete(self.showSpriteImg)
        #左右反転処理した画像ファイルを表示
        self.canvas.create_image(0,0,image=img_PhotoImage, anchor=tkinter.NW)
        #ページの更新
        self.root.mainloop()

    def Turn(self,angle):
        #画像ファイルを開く（上メソッドと同様、引数として受け取り）
        img = Image.open(self.spriteImg)
        #時計回りに90度回転
        img_process = img.rotate(angle*-1)
        #PhotoImageに変換
        img_PhotoImage = ImageTk.PhotoImage(img_process)
        #元あった画像ファイルを削除
        self.canvas.delete(self.showSpriteImg)
        #回転させた画像ファイルを表示
        self.canvas.create_image(0,0,image=img_PhotoImage, anchor=tkinter.NW)
        #ページの更新
        self.root.mainloop()
        # 引数で受け取った音声ファイルを再生する

        
    def AddSprite(self,splite):
        # イメージ作成
        addImg = tkinter.PhotoImage(file=splite, width=200, height=200)
        # キャンバスにイメージを表示
        showAddSpriteImg = self.canvas.create_image(0, 200, image=addImg, anchor=tkinter.NW)
        self.root.mainloop()

    def DownloadSprite(self):
        #ファイル選択ダイアログ表示
        filename = filedialog.askopenfilename()
        if filename !="":
            #指定ファイルをIMAGEフォルダにコピー
            shutil.copy(filename, 'IMAGE/')

    def SetBackground(self,background):
        #キャンバスに生成されているオブジェクトを全て削除する
        self.canvas.delete('all')
        # イメージ作成
        img = tkinter.PhotoImage(file=self.spriteImg, width=200, height=200)
        addImg = tkinter.PhotoImage(file=background, width=800, height=600)
        # キャンバスにイメージを表示（背景→スプライト）
        showBackground = self.canvas.create_image(0, 0, image=addImg, anchor=tkinter.NW)
        showSpriteImg = self.canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
        self.showSpriteImg = showSpriteImg
        self.root.mainloop()

    # 引数　music：\03_GenericScratch\PRG\GenericScratch\GenericScratch　直下のwav形式音声ファイル
    def Ring(self,music):
        winsound.PlaySound(music, winsound.SND_FILENAME)

    # spriteがmessageを表示
    # 引数　sprite：画像の名前
    # 引数　message：メッセージ内容
    def Message(self,sprite,message):
        # メッセージボックス
        messagebox.showinfo(sprite, message)

    # questionを表示後、回答を入力するようにして待つ
    # 引数　sprite：画像の名前
    # 引数　message：メッセージ内容
    def Question(self,sprite,message):
        answer = tkinter.StringVar()
        answer.set(tkinter.simpledialog.askstring(sprite, message))
        return answer.get()

    # spriteがmessageを表示
    # 引数　sprite：画像の名前
    # 引数　message：メッセージ内容
    def Answer(self,sprite,message):
        # メッセージボックス
        messagebox.showinfo(sprite, message)

    # spriteがmessageを表示
    # 引数　sprite：画像の名前
    # 引数　message：メッセージ内容
    def SendMessage(self,sprite,message):
        # メッセージボックス
        messagebox.showinfo(sprite, message)
        self.flgMessage = True

    # 呼び出されたらtrueをかえす
    # 戻り値　tmpFlgMessage：True/False
    def ReceiveMessage(self):
        tmpFlgMessage = self.flgMessage
        self.flgMessage = False
        return tmpFlgMessage

    # スプライトのコスチュームを引数で受け取ったコスチュームに変更する(画像の置き換え)
    # 引数　costumeType：コスチュームの画像
    def ChangeCostume(self,costumeType):
        # 変更後の画像を生成
        #キャンバスに生成されているオブジェクトを全て削除する
        self.spriteImg = costumeType
        img = tkinter.PhotoImage(file=self.spriteImg, width=200, height=200)
        points = self.canvas.coords(self.showSpriteImg)
        pointX=points[0]
        pointY=points[1]
        # キャンバスにイメージを表示
        self.showSpriteImg = self.canvas.create_image(pointX, pointY, image=img, anchor=tkinter.NW, tags="sprite")
        self.root.mainloop()

    # 画面端に到達したかを判定
    # 戻り値：True/False
    def TouchEdge(self):
        points = self.canvas.coords(self.showSpriteImg)
        pointX=points[0]
        pointY=points[1]
        if 0 < pointX < self.windowWidth - self.spriteWidth or 0 < pointY < self.windowHeight - self.spriteHeight:
            return False
        else:
            return True

