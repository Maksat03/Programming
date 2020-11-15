# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(251, 275)
        Calculator.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        Calculator.setFont(font)
        Calculator.setStyleSheet(u"QPushButton {\n"
"	background-color: silver;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: gray;\n"
"}")
        self.OUTPUT = QLineEdit(Calculator)
        self.OUTPUT.setObjectName(u"OUTPUT")
        self.OUTPUT.setGeometry(QRect(10, 10, 231, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.OUTPUT.setFont(font1)
        self.OUTPUT.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayoutWidget = QWidget(Calculator)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 59, 171, 211))
        self.nums_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.nums_gridLayout.setObjectName(u"nums_gridLayout")
        self.nums_gridLayout.setHorizontalSpacing(3)
        self.nums_gridLayout.setVerticalSpacing(0)
        self.nums_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_comma = QPushButton(self.gridLayoutWidget)
        self.btn_comma.setObjectName(u"btn_comma")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_comma.sizePolicy().hasHeightForWidth())
        self.btn_comma.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_comma.setFont(font2)
        self.btn_comma.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_comma.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 35px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn_comma, 3, 2, 1, 1)

        self.btn9 = QPushButton(self.gridLayoutWidget)
        self.btn9.setObjectName(u"btn9")
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        self.btn9.setFont(font2)
        self.btn9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn9.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn9, 0, 2, 1, 1)

        self.btn8 = QPushButton(self.gridLayoutWidget)
        self.btn8.setObjectName(u"btn8")
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        self.btn8.setFont(font2)
        self.btn8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn8.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn8, 0, 1, 1, 1)

        self.btn6 = QPushButton(self.gridLayoutWidget)
        self.btn6.setObjectName(u"btn6")
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        self.btn6.setFont(font2)
        self.btn6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn6.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn6, 1, 2, 1, 1)

        self.btn7 = QPushButton(self.gridLayoutWidget)
        self.btn7.setObjectName(u"btn7")
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        self.btn7.setFont(font2)
        self.btn7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn7.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn7, 0, 0, 1, 1)

        self.btn2 = QPushButton(self.gridLayoutWidget)
        self.btn2.setObjectName(u"btn2")
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setFont(font2)
        self.btn2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn2.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn2, 2, 1, 1, 1)

        self.btn4 = QPushButton(self.gridLayoutWidget)
        self.btn4.setObjectName(u"btn4")
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setFont(font2)
        self.btn4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn4.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn4, 1, 0, 1, 1)

        self.btn3 = QPushButton(self.gridLayoutWidget)
        self.btn3.setObjectName(u"btn3")
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setFont(font2)
        self.btn3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn3.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn3, 2, 2, 1, 1)

        self.btn5 = QPushButton(self.gridLayoutWidget)
        self.btn5.setObjectName(u"btn5")
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn5.setFont(font2)
        self.btn5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn5.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn5, 1, 1, 1, 1)

        self.btn1 = QPushButton(self.gridLayoutWidget)
        self.btn1.setObjectName(u"btn1")
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setFont(font2)
        self.btn1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn1.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn1, 2, 0, 1, 1)

        self.btn0 = QPushButton(self.gridLayoutWidget)
        self.btn0.setObjectName(u"btn0")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy1)
        self.btn0.setFont(font2)
        self.btn0.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn0.setStyleSheet(u"QPushButton {\n"
"	width: 75px;\n"
"	height: 35px;\n"
"}")

        self.nums_gridLayout.addWidget(self.btn0, 3, 0, 1, 2)

        self.gridLayoutWidget_2 = QWidget(Calculator)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(180, 59, 61, 113))
        self.operators_gridlayout = QGridLayout(self.gridLayoutWidget_2)
        self.operators_gridlayout.setObjectName(u"operators_gridlayout")
        self.operators_gridlayout.setHorizontalSpacing(3)
        self.operators_gridlayout.setVerticalSpacing(7)
        self.operators_gridlayout.setContentsMargins(0, 4, 0, 0)
        self.btn_multiplication = QPushButton(self.gridLayoutWidget_2)
        self.btn_multiplication.setObjectName(u"btn_multiplication")
        sizePolicy.setHeightForWidth(self.btn_multiplication.sizePolicy().hasHeightForWidth())
        self.btn_multiplication.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_multiplication.setFont(font3)
        self.btn_multiplication.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_multiplication.setStyleSheet(u"QPushButton {\n"
"	width: 25px;\n"
"	height: 50px;\n"
"}")

        self.operators_gridlayout.addWidget(self.btn_multiplication, 1, 0, 1, 1)

        self.btn_plus = QPushButton(self.gridLayoutWidget_2)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setFont(font3)
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plus.setStyleSheet(u"QPushButton {\n"
"	width: 25px;\n"
"	height: 46.5px;\n"
"}")

        self.operators_gridlayout.addWidget(self.btn_plus, 0, 0, 1, 1)

        self.btn_minus = QPushButton(self.gridLayoutWidget_2)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setFont(font3)
        self.btn_minus.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minus.setStyleSheet(u"QPushButton {\n"
"	width: 25px;\n"
"	height: 46.5px;\n"
"}")

        self.operators_gridlayout.addWidget(self.btn_minus, 0, 1, 1, 1)

        self.btn_division = QPushButton(self.gridLayoutWidget_2)
        self.btn_division.setObjectName(u"btn_division")
        sizePolicy.setHeightForWidth(self.btn_division.sizePolicy().hasHeightForWidth())
        self.btn_division.setSizePolicy(sizePolicy)
        self.btn_division.setFont(font3)
        self.btn_division.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_division.setStyleSheet(u"QPushButton {\n"
"	width: 25px;\n"
"	height: 50px;\n"
"}")

        self.operators_gridlayout.addWidget(self.btn_division, 1, 1, 1, 1)

        self.verticalLayoutWidget = QWidget(Calculator)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(180, 170, 61, 101))
        self.cmd_gridlayout = QVBoxLayout(self.verticalLayoutWidget)
        self.cmd_gridlayout.setSpacing(2)
        self.cmd_gridlayout.setObjectName(u"cmd_gridlayout")
        self.cmd_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.btn_equals = QPushButton(self.verticalLayoutWidget)
        self.btn_equals.setObjectName(u"btn_equals")
        sizePolicy.setHeightForWidth(self.btn_equals.sizePolicy().hasHeightForWidth())
        self.btn_equals.setSizePolicy(sizePolicy)
        self.btn_equals.setFont(font3)
        self.btn_equals.setStyleSheet(u"QPushButton {\n"
"	width: 57px;\n"
"	height: 40px;\n"
"}")

        self.cmd_gridlayout.addWidget(self.btn_equals)

        self.btn_clear = QPushButton(self.verticalLayoutWidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(10)
        self.btn_clear.setFont(font4)
        self.btn_clear.setStyleSheet(u"QPushButton {\n"
"	width: 57px;\n"
"	height: 40px;\n"
"}")

        self.cmd_gridlayout.addWidget(self.btn_clear)


        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.btn_comma.setText(QCoreApplication.translate("Calculator", u",", None))
        self.btn9.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.btn8.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.btn6.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.btn7.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.btn2.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.btn4.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.btn3.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.btn5.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.btn1.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.btn0.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.btn_multiplication.setText(QCoreApplication.translate("Calculator", u"*", None))
        self.btn_plus.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.btn_minus.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.btn_division.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.btn_equals.setText(QCoreApplication.translate("Calculator", u"=", None))
        self.btn_clear.setText(QCoreApplication.translate("Calculator", u"CLEAR", None))
    # retranslateUi

