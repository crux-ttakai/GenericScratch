# **********�ҏW�s�̎n��**********
import MakedMethod

def StartWork(root,Button,canvas,showSpriteImg,spriteImg):
    # ���\�b�h�Q�̃C���X�^���X����
    pc= MakedMethod.PropertyClass(root,Button,canvas,showSpriteImg,spriteImg)
    # �J�n�{�^���͂P�x�����������Ƃ��ł���
    Button["state"] = "disable"
# **********�ҏW�s�̏I���**********

    # **********�C���^�[�����͈ȉ���ҏW**********
    root.after(100,pc.SetBackground,"IMAGE\image.png")
    root.after(100,pc.Walk,100)
    root.after(100,pc.AddSprite,"IMAGE\elephant.png")