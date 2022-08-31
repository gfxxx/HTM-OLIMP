# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QStackedWidget, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

from customWidget import (ColorButtonGreen, ColorButtonRed, ZoomButton)
import images_rc
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 794)
        MainWindow.setStyleSheet(u"background-color: \"#343434\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:\"#343434\";")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1031, 801))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.horizontalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QSize(800, 618))
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.stackedWidget.setStyleSheet(u"background-color: \"#343434\"")
        self.filePage = QWidget()
        self.filePage.setObjectName(u"filePage")
        self.nextButton = ZoomButton(self.filePage)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(940, 700, 51, 51))
        self.nextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextButton.setMouseTracking(False)
        self.nextButton.setAutoFillBackground(False)
        self.nextButton.setStyleSheet(u"\n"
"background: transparent;\n"
"font-size: 16px;\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/images/Images/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setIconSize(QSize(30, 30))
        self.nextButton.setCheckable(False)
        self.line = QFrame(self.filePage)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(170, 190, 691, 20))
        self.line.setStyleSheet(u"color: \"white\";")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lineEdit_22 = QLineEdit(self.filePage)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setEnabled(False)
        self.lineEdit_22.setGeometry(QRect(450, 20, 113, 41))
        self.lineEdit_22.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: white;\n"
"font-size: 20px;")
        self.lineEdit_22.setFrame(True)
        self.lineEdit_22.setAlignment(Qt.AlignCenter)
        self.downloadDefault = QPushButton(self.filePage)
        self.downloadDefault.setObjectName(u"downloadDefault")
        self.downloadDefault.setGeometry(QRect(790, 80, 71, 31))
        self.downloadDefault.setCursor(QCursor(Qt.PointingHandCursor))
        self.downloadDefault.setStyleSheet(u"border: 1px solid \"#CECECE\";\n"
"color: \"#888\"")
        self.verticalLayoutWidget_6 = QWidget(self.filePage)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(30, 80, 221, 61))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.useDefault = QRadioButton(self.verticalLayoutWidget_6)
        self.useDefault.setObjectName(u"useDefault")
        self.useDefault.setStyleSheet(u"QRadioButton{\n"
"	color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 9px;\n"
"    height: 9px;\n"
"    border-radius: 6px;\n"
"	margin-right:4px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  \"#3372d6\";\n"
"    border:  2px solid \"#EEE\";\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:  \"#666\";\n"
"    border:  2px solid \"#666\";\n"
"}")

        self.horizontalLayout_9.addWidget(self.useDefault)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_7.setSpacing(-1)
#endif
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.useCustom = QRadioButton(self.verticalLayoutWidget_6)
        self.useCustom.setObjectName(u"useCustom")
        self.useCustom.setStyleSheet(u"QRadioButton{\n"
"	color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 9px;\n"
"    height: 9px;\n"
"    border-radius: 6px;\n"
"	margin-right:4px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  \"#3372d6\";\n"
"    border:  2px solid \"#EEE\";\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:  \"#666\";\n"
"    border:  2px solid \"#666\";\n"
"}")

        self.horizontalLayout_7.addWidget(self.useCustom)

        self.importButton = QPushButton(self.verticalLayoutWidget_6)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.importButton.setStyleSheet(u"border: 1px solid \"#898989\";\n"
"background: \"#787878\";\n"
"color:white;")

        self.horizontalLayout_7.addWidget(self.importButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.lineEdit_2 = QLineEdit(self.filePage)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(460, 430, 111, 31))
        self.lineEdit_2.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: white;\n"
"font-size: 20px;")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.horizontalLayoutWidget_3 = QWidget(self.filePage)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(30, 460, 231, 80))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(115, 50))
        self.lineEdit_3.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color:white;\n"
"")
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.lineEdit_3)

        self.nb_layers = QSpinBox(self.horizontalLayoutWidget_3)
        self.nb_layers.setObjectName(u"nb_layers")
        self.nb_layers.setStyleSheet(u"QSpinBox{\n"
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
        self.nb_layers.setWrapping(False)
        self.nb_layers.setFrame(True)
        self.nb_layers.setAlignment(Qt.AlignCenter)
        self.nb_layers.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.nb_layers.setMinimum(1)
        self.nb_layers.setMaximum(5)

        self.horizontalLayout_10.addWidget(self.nb_layers)

        self.validLayer = QPushButton(self.horizontalLayoutWidget_3)
        self.validLayer.setObjectName(u"validLayer")
        self.validLayer.setMaximumSize(QSize(30, 30))
        self.validLayer.setCursor(QCursor(Qt.PointingHandCursor))
        self.validLayer.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/images/Images/checked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.validLayer.setIcon(icon1)
        self.validLayer.setIconSize(QSize(25, 25))

        self.horizontalLayout_10.addWidget(self.validLayer)

        self.verticalLayoutWidget = QWidget(self.filePage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 540, 621, 201))
        self.layersSettings = QVBoxLayout(self.verticalLayoutWidget)
        self.layersSettings.setObjectName(u"layersSettings")
        self.layersSettings.setContentsMargins(0, 0, 0, 0)
        self.selectedFile = QLineEdit(self.filePage)
        self.selectedFile.setObjectName(u"selectedFile")
        self.selectedFile.setGeometry(QRect(30, 140, 221, 21))
        self.selectedFile.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"color:white;")
        self.selectedFile.setReadOnly(True)
        self.verticalLayoutWidget_7 = QWidget(self.filePage)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(30, 290, 221, 61))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.useDefault_ray = QRadioButton(self.verticalLayoutWidget_7)
        self.useDefault_ray.setObjectName(u"useDefault_ray")
        self.useDefault_ray.setStyleSheet(u"QRadioButton{\n"
"	color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 9px;\n"
"    height: 9px;\n"
"    border-radius: 6px;\n"
"	margin-right:4px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  \"#3372d6\";\n"
"    border:  2px solid \"#EEE\";\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:  \"#666\";\n"
"    border:  2px solid \"#666\";\n"
"}")

        self.horizontalLayout_11.addWidget(self.useDefault_ray)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_8 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_8.setSpacing(-1)
#endif
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.useCustom_ray = QRadioButton(self.verticalLayoutWidget_7)
        self.useCustom_ray.setObjectName(u"useCustom_ray")
        self.useCustom_ray.setStyleSheet(u"QRadioButton{\n"
"	color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 9px;\n"
"    height: 9px;\n"
"    border-radius: 6px;\n"
"	margin-right:4px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  \"#3372d6\";\n"
"    border:  2px solid \"#EEE\";\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:  \"#666\";\n"
"    border:  2px solid \"#666\";\n"
"}")

        self.horizontalLayout_8.addWidget(self.useCustom_ray)

        self.importButton_ray = QPushButton(self.verticalLayoutWidget_7)
        self.importButton_ray.setObjectName(u"importButton_ray")
        self.importButton_ray.setCursor(QCursor(Qt.PointingHandCursor))
        self.importButton_ray.setStyleSheet(u"border: 1px solid \"#898989\";\n"
"background: \"#787878\";\n"
"color:white;")

        self.horizontalLayout_8.addWidget(self.importButton_ray)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.downloadDefault_ray = QPushButton(self.filePage)
        self.downloadDefault_ray.setObjectName(u"downloadDefault_ray")
        self.downloadDefault_ray.setGeometry(QRect(790, 290, 71, 31))
        self.downloadDefault_ray.setCursor(QCursor(Qt.PointingHandCursor))
        self.downloadDefault_ray.setStyleSheet(u"border: 1px solid \"#CECECE\";\n"
"color: \"#888\"")
        self.lineEdit_23 = QLineEdit(self.filePage)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setEnabled(False)
        self.lineEdit_23.setGeometry(QRect(430, 210, 171, 41))
        self.lineEdit_23.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: white;\n"
"font-size: 20px;")
        self.lineEdit_23.setFrame(True)
        self.lineEdit_23.setAlignment(Qt.AlignCenter)
        self.line_2 = QFrame(self.filePage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(170, 390, 691, 20))
        self.line_2.setStyleSheet(u"color: \"white\";")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.selectedFile_ray = QLineEdit(self.filePage)
        self.selectedFile_ray.setObjectName(u"selectedFile_ray")
        self.selectedFile_ray.setGeometry(QRect(30, 350, 221, 21))
        self.selectedFile_ray.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"color:white;")
        self.selectedFile_ray.setReadOnly(True)
        self.stackedWidget.addWidget(self.filePage)
        self.constPage = QWidget()
        self.constPage.setObjectName(u"constPage")
        self.run = ColorButtonGreen(self.constPage)
        self.run.setObjectName(u"run")
        self.run.setGeometry(QRect(460, 700, 111, 41))
        self.run.setCursor(QCursor(Qt.PointingHandCursor))
        self.run.setStyleSheet(u"border: 1px solid \"#33d64b\";\n"
"color: \"#33d64b\";\n"
"\n"
"\n"
"")
        self.returnButton = ZoomButton(self.constPage)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setGeometry(QRect(40, 700, 51, 51))
        self.returnButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.returnButton.setStyleSheet(u"background: transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/images/Images/arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.returnButton.setIcon(icon2)
        self.returnButton.setIconSize(QSize(30, 30))
        self.tabConst = QTabWidget(self.constPage)
        self.tabConst.setObjectName(u"tabConst")
        self.tabConst.setGeometry(QRect(0, -1, 1031, 701))
        self.tabConst.setStyleSheet(u"QTabWidget{\n"
"	border: none;\n"
"}\n"
"QTabWidget::pane { \n"
"border: 0px;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"	width:200px;\n"
"	border-radius: 0;\n"
"	border: 1px solid gray;\n"
"	height: 30px;\n"
"	color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"	background: gray;\n"
"}")
        self.stackedWidget.addWidget(self.constPage)
        self.runningPage = QWidget()
        self.runningPage.setObjectName(u"runningPage")
        self.timeText = QTextBrowser(self.runningPage)
        self.timeText.setObjectName(u"timeText")
        self.timeText.setGeometry(QRect(320, 480, 151, 31))
        self.timeText.setStyleSheet(u"background: transparent;\n"
"border:none;\n"
"color:white;")
        self.stopButton = ColorButtonRed(self.runningPage)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(460, 700, 110, 41))
        self.stopButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopButton.setStyleSheet(u"border: 1px solid \"#d63338\";\n"
"color: \"#d63338\";\n"
"")
        self.stopButton.setAutoDefault(False)
        self.progressBar = QProgressBar(self.runningPage)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QRect(320, 450, 390, 21))
        self.progressBar.setCursor(QCursor(Qt.ArrowCursor))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	border: 1px solid \"#787878\";\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
"	color:white;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: \"#33d64b\";\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.goResult = ZoomButton(self.runningPage)
        self.goResult.setObjectName(u"goResult")
        self.goResult.setGeometry(QRect(940, 700, 51, 51))
        self.goResult.setCursor(QCursor(Qt.PointingHandCursor))
        self.goResult.setAutoFillBackground(False)
        self.goResult.setStyleSheet(u"\n"
"background: transparent;\n"
"font-size: 16px;\n"
"\n"
"")
        self.goResult.setIcon(icon)
        self.goResult.setIconSize(QSize(30, 30))
        self.goResult.setCheckable(False)
        self.returnButton_stop = ZoomButton(self.runningPage)
        self.returnButton_stop.setObjectName(u"returnButton_stop")
        self.returnButton_stop.setGeometry(QRect(40, 700, 51, 51))
        self.returnButton_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.returnButton_stop.setStyleSheet(u"background: transparent;")
        self.returnButton_stop.setIcon(icon2)
        self.returnButton_stop.setIconSize(QSize(30, 30))
        self.stackedWidget.addWidget(self.runningPage)
        self.resultPage = QWidget()
        self.resultPage.setObjectName(u"resultPage")
        self.resulTabWidget = QTabWidget(self.resultPage)
        self.resulTabWidget.setObjectName(u"resulTabWidget")
        self.resulTabWidget.setGeometry(QRect(0, 0, 1031, 801))
        self.resulTabWidget.setMinimumSize(QSize(0, 100))
        self.resulTabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.resulTabWidget.setStyleSheet(u"QTabWidget{\n"
"	border: none;\n"
"}\n"
"QTabWidget::pane {\n"
" border: 0px;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"	width:100px;\n"
"	border-radius: 0;\n"
"	border: 1px solid gray;\n"
"	height: 30px;\n"
"	color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"	background: gray;\n"
"}")
        self.resulTabWidget.setTabPosition(QTabWidget.North)
        self.resulTabWidget.setTabShape(QTabWidget.Rounded)
        self.resulTabWidget.setElideMode(Qt.ElideRight)
        self.resulTabWidget.setUsesScrollButtons(True)
        self.resulTabWidget.setDocumentMode(False)
        self.resulTabWidget.setTabsClosable(False)
        self.resulTabWidget.setMovable(False)
        self.resulTabWidget.setTabBarAutoHide(False)
        self.all = QWidget()
        self.all.setObjectName(u"all")
        self.newButton = QPushButton(self.all)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setGeometry(QRect(40, 30, 105, 31))
        self.newButton.setStyleSheet(u"border: 1px solid \"#CECECE\";\n"
"color: \"#888\"")
        self.verticalLayoutWidget_2 = QWidget(self.all)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(400, 170, 206, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-size:14px;\n"
"color:white;")
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.download_T = QPushButton(self.verticalLayoutWidget_2)
        self.download_T.setObjectName(u"download_T")
        self.download_T.setMinimumSize(QSize(70, 30))
        self.download_T.setCursor(QCursor(Qt.PointingHandCursor))
        self.download_T.setStyleSheet(u"border: 1px solid  \"#33d64b\";\n"
"color:  \"#8dc996\"")

        self.horizontalLayout_2.addWidget(self.download_T)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-size:14px;\n"
"color:white;")
        self.lineEdit_6.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_6)

        self.download_RH = QPushButton(self.verticalLayoutWidget_2)
        self.download_RH.setObjectName(u"download_RH")
        self.download_RH.setMinimumSize(QSize(70, 30))
        self.download_RH.setCursor(QCursor(Qt.PointingHandCursor))
        self.download_RH.setStyleSheet(u"border: 1px solid  \"#33d64b\";\n"
"color:  \"#8dc996\"")

        self.horizontalLayout_4.addWidget(self.download_RH)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-size:14px;\n"
"color:white;")
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_5)

        self.download_pv = QPushButton(self.verticalLayoutWidget_2)
        self.download_pv.setObjectName(u"download_pv")
        self.download_pv.setMinimumSize(QSize(70, 30))
        self.download_pv.setCursor(QCursor(Qt.PointingHandCursor))
        self.download_pv.setStyleSheet(u"border: 1px solid  \"#33d64b\";\n"
"color:  \"#8dc996\"")

        self.horizontalLayout_3.addWidget(self.download_pv)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.lineEdit = QLineEdit(self.all)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(440, 120, 141, 21))
        font = QFont()
        font.setUnderline(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-size: 18px;\n"
"color:white;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.resulTabWidget.addTab(self.all, "")
        self.stackedWidget.addWidget(self.resultPage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabConst.setCurrentIndex(-1)
        self.stopButton.setDefault(False)
        self.resulTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.nextButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.nextButton.setText("")
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"Meteo data", None))
        self.downloadDefault.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.useDefault.setText(QCoreApplication.translate("MainWindow", u"Use default", None))
        self.useCustom.setText(QCoreApplication.translate("MainWindow", u"Use custom file", None))
        self.importButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Number of layers:", None))
        self.validLayer.setText("")
        self.useDefault_ray.setText(QCoreApplication.translate("MainWindow", u"Use default", None))
        self.useCustom_ray.setText(QCoreApplication.translate("MainWindow", u"Use custom file", None))
        self.importButton_ray.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.downloadDefault_ray.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lineEdit_23.setText(QCoreApplication.translate("MainWindow", u"Radiation data", None))
        self.run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.returnButton.setText("")
        self.timeText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Time [min]: </p></body></html>", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(whatsthis)
        self.goResult.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.goResult.setText("")
        self.returnButton_stop.setText("")
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"New simulation", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.download_T.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"RH", None))
        self.download_RH.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"pv", None))
        self.download_pv.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Export matrices", None))
        self.resulTabWidget.setTabText(self.resulTabWidget.indexOf(self.all), QCoreApplication.translate("MainWindow", u"Table", None))
    # retranslateUi

