# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'const.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLayout, QLineEdit, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1031, 671)
        Form.setStyleSheet(u"background-color:\"#343434\"")
        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 30, 1031, 631))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, -1, -1)
        self.densityText = QTextEdit(self.horizontalLayoutWidget_2)
        self.densityText.setObjectName(u"densityText")
        self.densityText.setMaximumSize(QSize(400, 40))
        self.densityText.setStyleSheet(u"background:transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size:12px;\n"
"")
        self.densityText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.densityText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.densityText.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.densityText.setReadOnly(True)

        self.verticalLayout.addWidget(self.densityText)

        self.rho = QLineEdit(self.horizontalLayoutWidget_2)
        self.rho.setObjectName(u"rho")
        self.rho.setMinimumSize(QSize(0, 20))
        self.rho.setMaximumSize(QSize(200, 20))
        self.rho.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")
        self.rho.setMaxLength(10)

        self.verticalLayout.addWidget(self.rho)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.kText_2 = QTextEdit(self.horizontalLayoutWidget_2)
        self.kText_2.setObjectName(u"kText_2")
        self.kText_2.setMaximumSize(QSize(16777215, 40))
        self.kText_2.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;")
        self.kText_2.setFrameShadow(QFrame.Sunken)
        self.kText_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.kText_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.kText_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.kText_2.setReadOnly(True)
        self.kText_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_10.addWidget(self.kText_2)

        self.k_2 = QLineEdit(self.horizontalLayoutWidget_2)
        self.k_2.setObjectName(u"k_2")
        self.k_2.setMinimumSize(QSize(0, 20))
        self.k_2.setMaximumSize(QSize(200, 19))
        self.k_2.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")
        self.k_2.setMaxLength(10)

        self.verticalLayout_10.addWidget(self.k_2)


        self.horizontalLayout.addLayout(self.verticalLayout_10)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.cpText = QTextEdit(self.horizontalLayoutWidget_2)
        self.cpText.setObjectName(u"cpText")
        self.cpText.setMaximumSize(QSize(400, 40))
        self.cpText.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"")
        self.cpText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cpText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cpText.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.cpText)

        self.cp = QLineEdit(self.horizontalLayoutWidget_2)
        self.cp.setObjectName(u"cp")
        self.cp.setEnabled(True)
        self.cp.setMinimumSize(QSize(0, 20))
        self.cp.setMaximumSize(QSize(200, 20))
        self.cp.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")
        self.cp.setMaxLength(10)
        self.cp.setReadOnly(False)

        self.verticalLayout_6.addWidget(self.cp)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(self.horizontalLayoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setWindowModality(Qt.NonModal)
        self.line.setMaximumSize(QSize(16777215, 16777215))
        self.line.setLayoutDirection(Qt.LeftToRight)
        self.line.setStyleSheet(u"margin-left:150px;\n"
"margin-right:150px;\n"
"color:white;\n"
"background-color:\"#EEEEEE\";")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.dvText = QTextEdit(self.horizontalLayoutWidget_2)
        self.dvText.setObjectName(u"dvText")
        self.dvText.setMaximumSize(QSize(16777215, 22))
        self.dvText.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;")
        self.dvText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dvText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dvText.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.dvText)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_11 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_11.setSpacing(-1)
#endif
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_11.setContentsMargins(20, -1, -1, 130)
        self.textEdit_2 = QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 25))
        self.textEdit_2.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;")
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.textEdit_2)

        self.mu = QLineEdit(self.horizontalLayoutWidget_2)
        self.mu.setObjectName(u"mu")
        self.mu.setMaximumSize(QSize(200, 19))
        self.mu.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.verticalLayout_11.addWidget(self.mu)


        self.horizontalLayout_9.addLayout(self.verticalLayout_11)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dp = QLineEdit(self.horizontalLayoutWidget_2)
        self.dp.setObjectName(u"dp")
        self.dp.setEnabled(False)
        self.dp.setMinimumSize(QSize(0, 20))
        self.dp.setMaximumSize(QSize(220, 20))
        self.dp.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"color:white;")
        self.dp.setMaxLength(15)
        self.dp.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.dp)

        self.graph_dp = QWidget(self.horizontalLayoutWidget_2)
        self.graph_dp.setObjectName(u"graph_dp")
        self.graph_dp.setMinimumSize(QSize(270, 230))
        self.graph_dp.setMaximumSize(QSize(300, 250))

        self.verticalLayout_5.addWidget(self.graph_dp)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addLayout(self.verticalLayout_13)

        self.line_2 = QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setWindowModality(Qt.NonModal)
        self.line_2.setMaximumSize(QSize(16777215, 16777215))
        self.line_2.setLayoutDirection(Qt.LeftToRight)
        self.line_2.setStyleSheet(u"margin-left:150px;\n"
"margin-right:150px;\n"
"color:white;\n"
"background-color:\"#EEEEEE\";")
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.dl = QTextEdit(self.horizontalLayoutWidget_2)
        self.dl.setObjectName(u"dl")
        self.dl.setMaximumSize(QSize(16777215, 22))
        self.dl.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"")
        self.dl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dl.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.dl)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lineEdit_8 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_8.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;")
        self.lineEdit_8.setAlignment(Qt.AlignCenter)
        self.lineEdit_8.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.lineEdit_8)

        self.dl_4 = QLineEdit(self.horizontalLayoutWidget_2)
        self.dl_4.setObjectName(u"dl_4")
        self.dl_4.setMinimumSize(QSize(0, 20))
        self.dl_4.setMaximumSize(QSize(50, 20))
        self.dl_4.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;")
        self.dl_4.setMaxLength(10)
        self.dl_4.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.dl_4)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.rh_1 = QLineEdit(self.horizontalLayoutWidget_2)
        self.rh_1.setObjectName(u"rh_1")
        self.rh_1.setMaximumSize(QSize(50, 20))
        self.rh_1.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"\n"
"color:white;")

        self.horizontalLayout_15.addWidget(self.rh_1)

        self.dl_1 = QLineEdit(self.horizontalLayoutWidget_2)
        self.dl_1.setObjectName(u"dl_1")
        self.dl_1.setMinimumSize(QSize(0, 20))
        self.dl_1.setMaximumSize(QSize(50, 20))
        self.dl_1.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"\n"
"color:white;")
        self.dl_1.setMaxLength(10)

        self.horizontalLayout_15.addWidget(self.dl_1)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.rh_2 = QLineEdit(self.horizontalLayoutWidget_2)
        self.rh_2.setObjectName(u"rh_2")
        self.rh_2.setMaximumSize(QSize(50, 20))
        self.rh_2.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"\n"
"color:white;")

        self.horizontalLayout_13.addWidget(self.rh_2)

        self.dl_2 = QLineEdit(self.horizontalLayoutWidget_2)
        self.dl_2.setObjectName(u"dl_2")
        self.dl_2.setMinimumSize(QSize(0, 20))
        self.dl_2.setMaximumSize(QSize(50, 20))
        self.dl_2.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"\n"
"color:white;")
        self.dl_2.setMaxLength(10)

        self.horizontalLayout_13.addWidget(self.dl_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.rh_3 = QLineEdit(self.horizontalLayoutWidget_2)
        self.rh_3.setObjectName(u"rh_3")
        self.rh_3.setMaximumSize(QSize(50, 20))
        self.rh_3.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"\n"
"color:white;")

        self.horizontalLayout_12.addWidget(self.rh_3)

        self.dl_3 = QLineEdit(self.horizontalLayoutWidget_2)
        self.dl_3.setObjectName(u"dl_3")
        self.dl_3.setMinimumSize(QSize(0, 20))
        self.dl_3.setMaximumSize(QSize(50, 20))
        self.dl_3.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"\n"
"color:white;")
        self.dl_3.setMaxLength(10)

        self.horizontalLayout_12.addWidget(self.dl_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_11.addLayout(self.verticalLayout_12)

        self.graph_dl = QWidget(self.horizontalLayoutWidget_2)
        self.graph_dl.setObjectName(u"graph_dl")
        self.graph_dl.setMinimumSize(QSize(270, 230))
        self.graph_dl.setMaximumSize(QSize(300, 250))
        self.graph_dl.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.graph_dl)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_10.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textEdit = QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 40))
        self.textEdit.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(False)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_4.addWidget(self.textEdit)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 30, -1)
        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_4)

        self.w10 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w10.setObjectName(u"w10")
        self.w10.setMinimumSize(QSize(0, 20))
        self.w10.setMaximumSize(QSize(100, 16777215))
        self.w10.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_6.addWidget(self.w10)

        self.lineEdit_12 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_12.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_12)

        self.w20 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w20.setObjectName(u"w20")
        self.w20.setMinimumSize(QSize(0, 20))
        self.w20.setMaximumSize(QSize(100, 16777215))
        self.w20.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_6.addWidget(self.w20)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 4)
        self.horizontalLayout_6.setStretch(2, 2)
        self.horizontalLayout_6.setStretch(3, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 30, -1)
        self.lineEdit_15 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_15.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_15)

        self.w30 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w30.setObjectName(u"w30")
        self.w30.setMinimumSize(QSize(0, 20))
        self.w30.setMaximumSize(QSize(100, 16777215))
        self.w30.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_5.addWidget(self.w30)

        self.lineEdit_7 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_7.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_7)

        self.w40 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w40.setObjectName(u"w40")
        self.w40.setMinimumSize(QSize(0, 20))
        self.w40.setMaximumSize(QSize(100, 16777215))
        self.w40.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_5.addWidget(self.w40)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 4)
        self.horizontalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.setStretch(3, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 30, -1)
        self.lineEdit_17 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_17.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_17)

        self.w50 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w50.setObjectName(u"w50")
        self.w50.setMinimumSize(QSize(0, 20))
        self.w50.setMaximumSize(QSize(100, 16777215))
        self.w50.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_4.addWidget(self.w50)

        self.lineEdit_9 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_9.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_9)

        self.w60 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w60.setObjectName(u"w60")
        self.w60.setMinimumSize(QSize(0, 20))
        self.w60.setMaximumSize(QSize(100, 16777215))
        self.w60.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_4.addWidget(self.w60)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 4)
        self.horizontalLayout_4.setStretch(2, 2)
        self.horizontalLayout_4.setStretch(3, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 30, -1)
        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.w70 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w70.setObjectName(u"w70")
        self.w70.setMinimumSize(QSize(0, 20))
        self.w70.setMaximumSize(QSize(100, 16777215))
        self.w70.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_3.addWidget(self.w70)

        self.lineEdit_19 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_19.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_19)

        self.w80 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w80.setObjectName(u"w80")
        self.w80.setMinimumSize(QSize(0, 20))
        self.w80.setMaximumSize(QSize(100, 16777215))
        self.w80.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_3.addWidget(self.w80)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 30, -1)
        self.lineEdit_21 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_21.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_21)

        self.w90 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w90.setObjectName(u"w90")
        self.w90.setMinimumSize(QSize(0, 20))
        self.w90.setMaximumSize(QSize(100, 16777215))
        self.w90.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_8.addWidget(self.w90)

        self.lineEdit_11 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"font-size: 12px;")
        self.lineEdit_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_11.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_11)

        self.w100 = QLineEdit(self.horizontalLayoutWidget_2)
        self.w100.setObjectName(u"w100")
        self.w100.setMinimumSize(QSize(0, 20))
        self.w100.setMaximumSize(QSize(100, 16777215))
        self.w100.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.2);\n"
"color:white;")

        self.horizontalLayout_8.addWidget(self.w100)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 4)
        self.horizontalLayout_8.setStretch(2, 2)
        self.horizontalLayout_8.setStretch(3, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.graph_w = QWidget(self.horizontalLayoutWidget_2)
        self.graph_w.setObjectName(u"graph_w")

        self.verticalLayout_4.addWidget(self.graph_w)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.densityText.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px;\">Density [kg.m</span><span style=\" font-size:12px; vertical-align:super;\">-3</span><span style=\" font-size:12px;\">]</span></p></body></html>", None))
        self.rho.setText("")
        self.kText_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px;\">Thermal Conductivity [W.m</span><span style=\" font-size:12px; vertical-align:super;\">-1</span><span style=\" font-size:12px;\">.K</span><span style=\" font-size:12px; vertical-align:super;\">-1</span><span style=\" font-size:12px;\">]</span></p></body></html>", None))
        self.cpText.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px;\">Heat Capacity [J.kg</span><span style=\" font-size:12px; vertical-align:super;\">-1</span><span style=\" font-size:12px;\">.K</span><span style=\" font-size:12px; vertical-align:super;\">-1</span><span style=\" font-size:12px;\">]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12px;\"><br /></p></body></html>", None))
        self.cp.setText("")
        self.dvText.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">Water vapour permeability [kg/(m.s.Pa)]</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px;\">Water vapour resistance factor [-]</span></p></body></html>", None))
        self.dl.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">Liquid water permeability [kg/(m.s.Pa)]</span></p></body></html>", None))
        self.lineEdit_8.setText(QCoreApplication.translate("Form", u"RH", None))
        self.dl_4.setText(QCoreApplication.translate("Form", u"Delta l", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px; text-decoration: underline;\">Isotherme de sorption [kg.m</span><span style=\" font-size:14px; text-decoration: underline; vertical-align:super;\">-3</span><span style=\" font-size:14px; text-decoration: underline;\">]</span><span style=\" font-size:11px; text-decoration: underline;\"> (10 values)</span></p></body></html>", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"10%", None))
        self.lineEdit_12.setText(QCoreApplication.translate("Form", u"20%", None))
        self.lineEdit_15.setText(QCoreApplication.translate("Form", u"30%", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"40%", None))
        self.lineEdit_17.setText(QCoreApplication.translate("Form", u"50%", None))
        self.lineEdit_9.setText(QCoreApplication.translate("Form", u"60%", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"70%", None))
        self.lineEdit_19.setText(QCoreApplication.translate("Form", u"80%", None))
        self.lineEdit_21.setText(QCoreApplication.translate("Form", u"90%", None))
        self.lineEdit_11.setText(QCoreApplication.translate("Form", u"100%", None))
    # retranslateUi

