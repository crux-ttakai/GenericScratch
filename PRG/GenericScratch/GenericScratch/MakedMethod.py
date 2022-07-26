from pickle import FALSE
import winsound
import time
from tkinter import messagebox
import tkinter
import tkinter.simpledialog

class PropertyClass:
    # インスタンス生成時にプロパティに🏁ボタン、キャンバス、スプライトを設定
    def __init__(self,root,button,canvas,showSpriteImg,spriteImg):
        self.root = root
        self.button = button
        self.canvas = canvas
        self.showSpriteImg = showSpriteImg
        self.spriteImg = spriteImg
        self.flgMessage = False
    
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
    def flgMessage(self):
        return self.__flgMessage
    @flgMessage.setter
    def flgMessage(self, value):
        if value != '':
            self.__flgMessage = value

    # **********以下、作成メソッド**********
    # 各パーツは以下の書き方で参照
    # 🏁ボタン：self.button
    # キャンバス：self.canvas
    # スプライト：self.showSpriteImg

    # 引数で受け取った歩数分動く
    # 引数　step：歩数
    def Walk(self,step):
        # スプライトをX軸方向に100動かす
        self.canvas.move(self.showSpriteImg, step, 0)

    # 引数で受け取った音声ファイルを再生する
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
    # 戻り値：
    def ReceiveMessage(self):
        tmpFlgMessage = self.flgMessage
        self.flgMessage = False
        return tmpFlgMessage