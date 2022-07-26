#def StartWork(Button,canvas,showSpriteImg):
    # �X�v���C�g��X��������100������
    #canvas.move(showSpriteImg, 100, 0)
    # �J�n�{�^���͂P�x�����������Ƃ��ł���
    #Button["state"] = "disable"


import tkinter
import time
from PIL import Image,ImageTk

def ChangeXCoord(Button,canvas,showSpriteImg,ChangeCoord):
    #�X�v���C�g��X���W�����Ɏ󂯎����������(ChangeCoord)�ړ�����
    canvas.move(showSpriteImg,ChangeCoord,0)
    # �J�n�{�^���͂P�x�����������Ƃ��ł���
    Button["state"] = "disable"

def ChangeYCoord(Button,canvas,showSpriteImg,ChangeCoord):
    #�X�v���C�g��Y���W�����Ɏ󂯎����������(ChangeCoord)�ړ�����
    canvas.move(showSpriteImg,0,ChangeCoord)
    # �J�n�{�^���͂P�x�����������Ƃ��ł���
    Button["state"] = "disable"



def ChangeSize(Button,canvas,showSpriteImg,spriteImg,size,root):
    #�摜�t�@�C�����J���iGenericScratch�t�@�C�����玝���Ă���j
    img = Image.open(spriteImg)
    #�T�C�Y�̊g��k������
    img_process = img.resize((size,size))
    #PhotoImage�ɕϊ�
    img_PhotoImage = ImageTk.PhotoImage(img_process)
    #���������摜�t�@�C�����폜
    canvas.delete(showSpriteImg)
    #�g��k�����������摜�t�@�C����\��
    canvas.create_image(0,0,image=img_PhotoImage,anchor=tkinter.NW)
    #�{�^����񊈐�
    Button["state"] = "disable"
    #�y�[�W�̍X�V
    root.mainloop()


    


def Rebound(Button,canvas,showSpriteImg,spriteImg,root):
    #�摜�t�@�C�����J���i�チ�\�b�h�Ɠ��l�A�����Ƃ��Ď󂯎��j
    img = Image.open(spriteImg)
    #���E���]����
    img_process = img.transpose(Image.FLIP_LEFT_RIGHT)
    #PhotoImage�ɕϊ�
    img_PhotoImage = ImageTk.PhotoImage(img_process)
    #���������摜�t�@�C�����폜
    canvas.delete(showSpriteImg)
    #���E���]���������摜�t�@�C����\��
    canvas.create_image(0,0,image=img_PhotoImage, anchor=tkinter.NW)
    #�{�^����񊈐�
    Button["state"] = "disable"
    #�y�[�W�̍X�V
    root.mainloop()
    

def Turn(Button,canvas,showSpriteImg,spriteImg,angle,root):
    #�摜�t�@�C�����J���i�チ�\�b�h�Ɠ��l�A�����Ƃ��Ď󂯎��j
    img = Image.open(spriteImg)
    #���v����90�x��]
    img_process = img.rotate(angle*-1)
    #PhotoImage�ɕϊ�
    img_PhotoImage = ImageTk.PhotoImage(img_process)
    #���������摜�t�@�C�����폜
    canvas.delete(showSpriteImg)
    #��]�������摜�t�@�C����\��
    canvas.create_image(0,0,image=img_PhotoImage, anchor=tkinter.NW)
    #�{�^����񊈐�
    Button["state"] = "disable"
    #�y�[�W�̍X�V
    root.mainloop()
    