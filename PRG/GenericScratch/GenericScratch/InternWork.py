
# **********�ҏW�s�̎n��**********
import MakedMethod

def StartWork(root,Button,label,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight):
    # ���\�b�h�Q�̃C���X�^���X����
    pc= MakedMethod.PropertyClass(root,Button,label,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight)
    # �J�n�{�^���͂P�x�����������Ƃ��ł���
    Button["state"] = "disable"
# **********�ҏW�s�̏I���**********

    # **********�C���^�[�����͈ȉ���ҏW�̎n��**********
    root.after(100,pc.ChangeXCoord,100)
    # 1�b��Ƀ^�C�}�[��i�ߎn�߂�
    root.after(1000, pc.repeat_func)
    # **********�C���^�[�����͈ȉ���ҏW�̏I���*******




# **********�ҏW�s�̎n��**********
def StartWorkSprite(root,Button,label,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight):
    # ���\�b�h�Q�̃C���X�^���X����
    pc= MakedMethod.PropertyClass(root,Button,label,canvas,showSpriteImg,spriteImg,WindowWidth,WindowHeight,SpriteWidth,SpriteHeight)
# **********�ҏW�s�̏I���**********

    # **********�C���^�[�����͈ȉ���ҏW�̎n��**********
    pc.DownPen()
    pc.ChangePenColor("Blue")
    pc.ChangePenSize(10)
    pc.ChangeXCoord(100)
    pc.ChangePenColor("Red")
    pc.ChangePenSize(2)
    pc.ChangeYCoord(100)
    pc.UpPen()
    if pc.TouchEdge():
        print("kkkkkkkk")
    else:
        print("bbbbbbbb")
    # **********�C���^�[�����͈ȉ���ҏW�̏I���*******

