
# **********�ҏW�s�̎n��**********
import MakedMethod

def StartWork(Button,canvas,showSpriteImg):
    # ���\�b�h�Q�̃C���X�^���X����
    pc= MakedMethod.PropertyClass(Button,canvas,showSpriteImg)
    # �J�n�{�^���͂P�x�����������Ƃ��ł���
    Button["state"] = "disable"
# **********�ҏW�s�̏I���**********

    # **********�C���^�[�����͈ȉ���ҏW**********
    pc.Walk(100)

