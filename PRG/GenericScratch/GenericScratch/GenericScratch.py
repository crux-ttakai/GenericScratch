#reference https://qiita.com/nnahito/items/ad1428a30738b3d93762
#reference https://nnahito.gitbooks.io/tkinter/content/helloworld/30dc-30bf-30f3-3092-shi-3063-3066-307f-308b/button3092-she-zhi-3057-3066-307f-308b.html
#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter

root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

Static1 = tkinter.Label(text=u'test')
Static1.pack()

EditBox = tkinter.Entry()
EditBox.pack()

Button = tkinter.Button(text=u'test')
Button.pack()

root.mainloop()
