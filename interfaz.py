# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnodo = QtWidgets.QPushButton(self.centralwidget)
        self.btnodo.setGeometry(QtCore.QRect(100, 120, 91, 23))
        self.btnodo.setObjectName("btnodo")
        self.lbnodo = QtWidgets.QLabel(self.centralwidget)
        self.lbnodo.setGeometry(QtCore.QRect(10, 80, 141, 20))
        self.lbnodo.setObjectName("lbnodo")
        self.btgrafo = QtWidgets.QPushButton(self.centralwidget)
        self.btgrafo.setGeometry(QtCore.QRect(40, 10, 75, 23))
        self.btgrafo.setObjectName("btgrafo")
        self.txtnombrenodo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtnombrenodo.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.txtnombrenodo.setObjectName("txtnombrenodo")
        self.btdigrafo = QtWidgets.QPushButton(self.centralwidget)
        self.btdigrafo.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.btdigrafo.setObjectName("btdigrafo")
        self.btcamino = QtWidgets.QPushButton(self.centralwidget)
        self.btcamino.setGeometry(QtCore.QRect(180, 450, 75, 23))
        self.btcamino.setObjectName("btcamino")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 350, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 420, 91, 16))
        self.label_8.setObjectName("label_8")
        self.txtsalidacamino = QtWidgets.QLineEdit(self.centralwidget)
        self.txtsalidacamino.setGeometry(QtCore.QRect(20, 380, 113, 20))
        self.txtsalidacamino.setObjectName("txtsalidacamino")
        self.txtcaminollegada = QtWidgets.QLineEdit(self.centralwidget)
        self.txtcaminollegada.setGeometry(QtCore.QRect(20, 420, 113, 20))
        self.txtcaminollegada.setObjectName("txtcaminollegada")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 380, 71, 16))
        self.label_7.setObjectName("label_7")
        self.txtpeso = QtWidgets.QLineEdit(self.centralwidget)
        self.txtpeso.setGeometry(QtCore.QRect(130, 270, 113, 20))
        self.txtpeso.setObjectName("txtpeso")
        self.txtsalida = QtWidgets.QLineEdit(self.centralwidget)
        self.txtsalida.setGeometry(QtCore.QRect(160, 170, 113, 20))
        self.txtsalida.setObjectName("txtsalida")
        self.btarista = QtWidgets.QPushButton(self.centralwidget)
        self.btarista.setGeometry(QtCore.QRect(90, 310, 91, 23))
        self.btarista.setObjectName("btarista")
        self.lbllegada = QtWidgets.QLabel(self.centralwidget)
        self.lbllegada.setGeometry(QtCore.QRect(10, 220, 141, 20))
        self.lbllegada.setObjectName("lbllegada")
        self.lbsalida = QtWidgets.QLabel(self.centralwidget)
        self.lbsalida.setGeometry(QtCore.QRect(20, 170, 131, 20))
        self.lbsalida.setObjectName("lbsalida")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 270, 91, 20))
        self.label_3.setObjectName("label_3")
        self.txtllegada = QtWidgets.QLineEdit(self.centralwidget)
        self.txtllegada.setGeometry(QtCore.QRect(160, 220, 113, 20))
        self.txtllegada.setObjectName("txtllegada")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(280, 0, 20, 471))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 150, 291, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-10, 330, 301, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lbadyacencia = QtWidgets.QLabel(self.centralwidget)
        self.lbadyacencia.setGeometry(QtCore.QRect(300, 40, 371, 91))
        self.lbadyacencia.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbadyacencia.setText("")
        self.lbadyacencia.setObjectName("lbadyacencia")
        self.lbincidencia = QtWidgets.QLabel(self.centralwidget)
        self.lbincidencia.setGeometry(QtCore.QRect(300, 170, 371, 91))
        self.lbincidencia.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbincidencia.setText("")
        self.lbincidencia.setObjectName("lbincidencia")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 10, 111, 16))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 140, 111, 16))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 40, 291, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lbcircuito = QtWidgets.QLabel(self.centralwidget)
        self.lbcircuito.setGeometry(QtCore.QRect(300, 290, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbcircuito.setFont(font)
        self.lbcircuito.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbcircuito.setText("")
        self.lbcircuito.setObjectName("lbcircuito")
        self.lbcamino = QtWidgets.QLabel(self.centralwidget)
        self.lbcamino.setGeometry(QtCore.QRect(300, 330, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbcamino.setFont(font)
        self.lbcamino.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbcamino.setText("")
        self.lbcamino.setObjectName("lbcamino")
        self.lbhamiltoniano = QtWidgets.QLabel(self.centralwidget)
        self.lbhamiltoniano.setGeometry(QtCore.QRect(300, 370, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbhamiltoniano.setFont(font)
        self.lbhamiltoniano.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbhamiltoniano.setText("")
        self.lbhamiltoniano.setObjectName("lbhamiltoniano")
        self.lbplanar = QtWidgets.QLabel(self.centralwidget)
        self.lbplanar.setGeometry(QtCore.QRect(300, 410, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbplanar.setFont(font)
        self.lbplanar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbplanar.setText("")
        self.lbplanar.setObjectName("lbplanar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grafos"))
        self.btnodo.setText(_translate("MainWindow", "Ingresar Nodo"))
        self.lbnodo.setText(_translate("MainWindow", "Nombre del nodo a agregar:"))
        self.btgrafo.setText(_translate("MainWindow", "Grafo"))
        self.btdigrafo.setText(_translate("MainWindow", "DiGrafo"))
        self.btcamino.setText(_translate("MainWindow", "Aceptar"))
        self.label_9.setText(_translate("MainWindow", "Camino Mas Corto"))
        self.label_8.setText(_translate("MainWindow", "Nodo de LLegada"))
        self.label_7.setText(_translate("MainWindow", "Nodo de Salida"))
        self.btarista.setText(_translate("MainWindow", "Ingresar Arista"))
        self.lbllegada.setText(_translate("MainWindow", "Nodo de Llegada de la arista"))
        self.lbsalida.setText(_translate("MainWindow", "Nodo de Salida de la arista "))
        self.label_3.setText(_translate("MainWindow", "Peso de la Arista"))
        self.label_4.setText(_translate("MainWindow", "Matriz de Adyacencia:"))
        self.label_5.setText(_translate("MainWindow", "Matriz de Incidencia:"))
