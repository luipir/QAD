# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qad_dimstyle_diff.ui'
#
# Created: Wed Aug 05 11:13:06 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DimStyle_Diff_Dialog(object):
    def setupUi(self, DimStyle_Diff_Dialog):
        DimStyle_Diff_Dialog.setObjectName(_fromUtf8("DimStyle_Diff_Dialog"))
        DimStyle_Diff_Dialog.resize(443, 526)
        self.label = QtGui.QLabel(DimStyle_Diff_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DimStyle_Diff_Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 101, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dimStyle1 = QtGui.QComboBox(DimStyle_Diff_Dialog)
        self.dimStyle1.setGeometry(QtCore.QRect(80, 10, 211, 22))
        self.dimStyle1.setObjectName(_fromUtf8("dimStyle1"))
        self.dimStyle2 = QtGui.QComboBox(DimStyle_Diff_Dialog)
        self.dimStyle2.setGeometry(QtCore.QRect(80, 40, 211, 22))
        self.dimStyle2.setObjectName(_fromUtf8("dimStyle2"))
        self.line = QtGui.QFrame(DimStyle_Diff_Dialog)
        self.line.setGeometry(QtCore.QRect(10, 70, 421, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.msg = QtGui.QLabel(DimStyle_Diff_Dialog)
        self.msg.setGeometry(QtCore.QRect(10, 80, 321, 21))
        self.msg.setObjectName(_fromUtf8("msg"))
        self.layoutWidget = QtGui.QWidget(DimStyle_Diff_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(277, 490, 158, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.closeButton = QtGui.QPushButton(self.layoutWidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.helpButton = QtGui.QPushButton(self.layoutWidget)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.horizontalLayout.addWidget(self.helpButton)
        self.tableWidget = QtGui.QTableWidget(DimStyle_Diff_Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 421, 371))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.copyButton = QtGui.QPushButton(DimStyle_Diff_Dialog)
        self.copyButton.setGeometry(QtCore.QRect(404, 80, 31, 23))
        self.copyButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/qad/icons/copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copyButton.setIcon(icon)
        self.copyButton.setObjectName(_fromUtf8("copyButton"))

        self.retranslateUi(DimStyle_Diff_Dialog)
        QtCore.QObject.connect(self.helpButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DimStyle_Diff_Dialog.ButtonHELP_Pressed)
        QtCore.QObject.connect(self.dimStyle1, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), DimStyle_Diff_Dialog.DimStyleName1Changed)
        QtCore.QObject.connect(self.dimStyle2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), DimStyle_Diff_Dialog.DimStyleName2Changed)
        QtCore.QObject.connect(self.copyButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DimStyle_Diff_Dialog.copyToClipboard)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DimStyle_Diff_Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(DimStyle_Diff_Dialog)

    def retranslateUi(self, DimStyle_Diff_Dialog):
        DimStyle_Diff_Dialog.setWindowTitle(_translate("DimStyle_Diff_Dialog", "QAD - Confronta stili di quota", None))
        self.label.setText(_translate("DimStyle_Diff_Dialog", "Confronta:", None))
        self.label_2.setText(_translate("DimStyle_Diff_Dialog", "Con:", None))
        self.dimStyle1.setToolTip(_translate("DimStyle_Diff_Dialog", "Specifica il primo stile di quota per il confronto.", None))
        self.dimStyle2.setToolTip(_translate("DimStyle_Diff_Dialog", "Specifica il secondo stile di quota per il confronto.Se si imposta il secondo stile come il primo stile, verranno visualizzate tutte le proprietà dello stile di quota.", None))
        self.msg.setText(_translate("DimStyle_Diff_Dialog", "TextLabel", None))
        self.closeButton.setText(_translate("DimStyle_Diff_Dialog", "Chiudi", None))
        self.helpButton.setText(_translate("DimStyle_Diff_Dialog", "?", None))
        self.tableWidget.setToolTip(_translate("DimStyle_Diff_Dialog", "<html><head/><body><p>Visualizza i risultati dl confronto degli stili di quota. Se si confrontano due stili diversi, verranno mostrate le proprietà con valore differente. Se si imposta il secondo stile come il primo stile, verranno visualizzate tutte le proprietà dello stile di quota.</p></body></html>", None))
        self.copyButton.setToolTip(_translate("DimStyle_Diff_Dialog", "Copia il risultato del confronto negli Appunti.", None))

