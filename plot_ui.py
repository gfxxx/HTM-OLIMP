# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)
import images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1034, 750)
        self.plot = QWidget(Form)
        self.plot.setObjectName(u"plot")
        self.plot.setGeometry(QRect(120, 150, 801, 441))
        self.plot.setStyleSheet(u"background-color: \"#343434\"\n"
"")
        self.savePlot = QPushButton(Form)
        self.savePlot.setObjectName(u"savePlot")
        self.savePlot.setGeometry(QRect(950, 50, 41, 41))
        self.savePlot.setCursor(QCursor(Qt.PointingHandCursor))
        self.savePlot.setStyleSheet(u"border: 1px solid \"#33d64b\";\n"
"color: \"#33d64b\";\n"
"border-radius:20px;\n"
"")
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(140, 40, 251, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: white;")
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.date_min = QSpinBox(self.horizontalLayoutWidget)
        self.date_min.setObjectName(u"date_min")
        self.date_min.setMinimumSize(QSize(70, 0))
        self.date_min.setStyleSheet(u"QSpinBox{\n"
"border: 1px solid #CECECE;\n"
"color:white;\n"
"}\n"
"\n"
"QSpinBox::up-button{\n"
"	image: url(:/images/Images/plus.png);\n"
"	height: 9px;\n"
"	width:9px;\n"
"	background-color: #888;\n"
"	subcontrol-position: top right;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"\n"
"QSpinBox::down-button{\n"
"	image: url(:/images/Images/minus.png);\n"
"	height: 9px;\n"
"	width:9px;\n"
"	background-color: #888;\n"
"	subcontrol-position: bottom right;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"")
        self.date_min.setMaximum(1000)
        self.date_min.setDisplayIntegerBase(10)

        self.horizontalLayout.addWidget(self.date_min)

        self.date_max = QSpinBox(self.horizontalLayoutWidget)
        self.date_max.setObjectName(u"date_max")
        self.date_max.setMinimumSize(QSize(70, 0))
        self.date_max.setStyleSheet(u"QSpinBox{\n"
"border: 1px solid #CECECE;\n"
"color:white;\n"
"}\n"
"\n"
"QSpinBox::up-button{\n"
"	image: url(:/images/Images/plus.png);\n"
"	height: 9px;\n"
"	width:9px;\n"
"	background-color: #888;\n"
"	subcontrol-position: top right;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"\n"
"QSpinBox::down-button{\n"
"	image: url(:/images/Images/minus.png);\n"
"	height: 9px;\n"
"	width:9px;\n"
"	background-color: #888;\n"
"	subcontrol-position: bottom right;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"")
        self.date_max.setMaximum(1000)

        self.horizontalLayout.addWidget(self.date_max)

        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(440, 40, 131, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;")
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.space = QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.space.setObjectName(u"space")
        self.space.setMinimumSize(QSize(70, 0))
        self.space.setStyleSheet(u"QDoubleSpinBox{\n"
"border: 1px solid #CECECE;\n"
"color:white;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"	image: url(:/images/Images/plus.png);\n"
"	height: 9px;\n"
"	width:9px;\n"
"	background-color: #888;\n"
"	subcontrol-position: top right;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"	image: url(:/images/Images/minus.png);\n"
"	height: 9px;\n"
"	width:9px;\n"
"	background-color: #888;\n"
"	subcontrol-position: bottom right;\n"
"	padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"")
        self.space.setDecimals(2)
        self.space.setSingleStep(0.050000000000000)

        self.horizontalLayout_2.addWidget(self.space)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.savePlot.setText(QCoreApplication.translate("Form", u"Save", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"Date range:", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"Space:", None))
    # retranslateUi

