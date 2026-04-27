from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem
from numpy import*
from random import*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
m=array([[int]*10]*10)
def remplir(m,n):
    for i in range (n):
        for j in range (n):
            m[i,j]=randint(0,1)
def puissance(a,b):
    p=1
    for ls3d in range (p):
        p=p*a
    return p
def convertir (m,n):
    ls3d=""
    for i in range (n):
        monira=0
        for j in range (n):
            monira=monira+m[i,j]*puissance(2,n-j-1)
        ls3d=ls3d+str(monira)+"-"
    ls3d=ls3d[0:len(ls3d)-1]
    return ls3d
def reponse():
    n=int(f.nbr.text())
    if not (2<n<11):
        f.txt.setText("thabbet oumourkkkkkkkkkkkkk")
    else:
        remplir(m,n)
        ch=convertir(m,n)
        f.txt.setText(ch)
        


app = QApplication([])
f = loadUi ("interface_conv.ui")
f.show()
f.afficher.clicked.connect (reponse)
f.Nom_Bouton.clicked.connect (Nom_Module)
f.Nom_Bouton.clicked.connect (Nom_Module)
app.exec_()