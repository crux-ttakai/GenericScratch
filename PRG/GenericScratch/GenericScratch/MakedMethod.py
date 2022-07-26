import tkinter
import tkinter.font
from tkinter import filedialog
import shutil
import time

class PropertyClass:
    # インスタンス生成時にプロパティに🏁ボタン、キャンバス、スプライトを設定
    def __init__(self,root,button,canvas,showSpriteImg,spriteImg):
        self.root = root
        self.button = button
        self.canvas = canvas
        self.showSpriteImg = showSpriteImg
        self.spriteImg = spriteImg
    
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




