from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem
def inverser(ch):
    ch2=""
    for i in range(len(ch)):
        ch2=ch2+ch[i]
    return ch2

def propre(ch):
    las3d=int(ch)
    if (las3d%10)*las3d==int(inverser(ch)):
        test=True
    else:
        test=False
    return test

def monira():
    ch=f.nbre.text()
    if not(ch.isdecimal() and len(ch)==4):
        msg="verifi ya za7i "
    elif propre(ch):
        msg="nbr est prpr"
    else:
        msg="nbr n'est ps prpr"
    f.msg.setText(msg)
    
app = QApplication([])
f = loadUi ("interface_propre.ui")
f.show()
f.verifier.clicked.connect (monira)
app.exec_()