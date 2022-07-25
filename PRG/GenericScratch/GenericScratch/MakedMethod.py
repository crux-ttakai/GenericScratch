class PropertyClass:
    # インスタンス生成時にプロパティに🏁ボタン、キャンバス、スプライトを設定
    def __init__(self,button,canvas,showSpriteImg):
        self.button = button
        self.canvas = canvas
        self.showSpriteImg = showSpriteImg
    
    # プロパティ
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


