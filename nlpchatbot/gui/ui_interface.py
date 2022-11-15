# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceFSrZwd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(953, 565)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	background-color:rgb(52,65,70);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_container = QFrame(self.centralwidget)
        self.left_menu_container.setObjectName(u"left_menu_container")
        self.left_menu_container.setEnabled(True)
        self.left_menu_container.setMaximumSize(QSize(0, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(52, 65, 70, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(252, 252, 252, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2)
        self.left_menu_container.setPalette(palette)
        font = QFont()
        font.setFamily(u"Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.left_menu_container.setFont(font)
        self.left_menu_container.setFrameShape(QFrame.StyledPanel)
        self.left_menu_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.left_menu_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.left_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(180, 0))
        self.slide_menu.setStyleSheet(u"*{\n"
"	background-color:rgb(93,131,145);\n"
"	color: rgb(251,222,252);\n"
"}")
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.slide_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Montserrat ExtraBold")
        font1.setPointSize(17)
        self.label.setFont(font1)
        self.label.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.slide_menu)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.toolBox = QToolBox(self.frame_5)
        self.toolBox.setObjectName(u"toolBox")
        font2 = QFont()
        font2.setFamily(u"Montserrat Medium")
        font2.setPointSize(10)
        self.toolBox.setFont(font2)
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"	background-color:rgb(122,139,145);\n"
"	text-align:left;\n"
"}\n"
"QToolBox::tab{\n"
"	border-radius:5px;\n"
"	background-color:rgb(69,60,51);\n"
"	text-align:left;\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 162, 383))
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        font3 = QFont()
        font3.setFamily(u"Montserrat Alternates SemiBold")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_9.setFont(font3)

        self.verticalLayout_4.addWidget(self.pushButton_9, 0, Qt.AlignLeft)

        self.pushButton_10 = QPushButton(self.frame_9)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font)

        self.verticalLayout_4.addWidget(self.pushButton_10, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_9, 0, Qt.AlignTop)

        icon = QIcon()
        icon.addFile(u":/icon/send-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon, u"Envoi de message")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 162, 383))
        self.frame_10 = QFrame(self.page_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(9, 9, 169, 84))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_10)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font)

        self.verticalLayout_5.addWidget(self.pushButton_11, 0, Qt.AlignLeft)

        self.pushButton_12 = QPushButton(self.frame_10)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font)

        self.verticalLayout_5.addWidget(self.pushButton_12, 0, Qt.AlignLeft)

        self.pushButton_13 = QPushButton(self.frame_10)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font)

        self.verticalLayout_5.addWidget(self.pushButton_13, 0, Qt.AlignLeft)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 210, 74, 13))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons8-robotique-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon1, u"Bot")

        self.horizontalLayout_8.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.slide_menu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_8 = QPushButton(self.frame_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"*{\n"
"	color:rgb(3,3,3);\n"
"	\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons8-voir-en-tant-qu\u2019utilisateur-diff\u00e9rent-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.pushButton_8, 0, Qt.AlignLeft)

        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons8-mesure-de-l&#39;ordinateur-portable-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.pushButton_7)


        self.verticalLayout_2.addWidget(self.frame_8, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.left_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.main_body)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setStyleSheet(u"*{\n"
"	background-color:rgb(93,131,145);\n"
"}")
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.main_header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(194, 44))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(0, 10, 28, 40))
        self.pushButton_6.setMaximumSize(QSize(28, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/icon/menu-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(22, 22))

        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.main_header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(16, 16))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 10, 75, 24))
        self.pushButton_5.setMinimumSize(QSize(75, 23))
        icon5 = QIcon()
        icon5.addFile(u":/icon/account-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_2 = QFrame(self.main_header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.minimize_window_button = QPushButton(self.frame_2)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon.qrc", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.minimize_window_button)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon7 = QIcon()
        icon7.addFile(u":/icon/minimize-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.close_window_button = QPushButton(self.frame_2)
        self.close_window_button.setObjectName(u"close_window_button")
        icon8 = QIcon()
        icon8.addFile(u":/icon/close-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.close_window_button)


        self.horizontalLayout_3.addWidget(self.frame_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body_2 = QFrame(self.main_body)
        self.main_body_2.setObjectName(u"main_body_2")
        sizePolicy.setHeightForWidth(self.main_body_2.sizePolicy().hasHeightForWidth())
        self.main_body_2.setSizePolicy(sizePolicy)
        self.main_body_2.setFrameShape(QFrame.StyledPanel)
        self.main_body_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_body_2)

        self.main_footer = QFrame(self.main_body)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setStyleSheet(u"*{\n"
"	color: rgb(251,222,252);\n"
"}")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.main_footer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.main_footer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1, 20, 111, 23))

        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.main_footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_6)

        self.sixe_grip = QFrame(self.main_footer)
        self.sixe_grip.setObjectName(u"sixe_grip")
        self.sixe_grip.setMinimumSize(QSize(10, 10))
        self.sixe_grip.setMaximumSize(QSize(10, 10))
        self.sixe_grip.setFrameShape(QFrame.StyledPanel)
        self.sixe_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sixe_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.main_footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KAICE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"INSTANTANNE", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"DIFFERE", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Envoi de message", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"ENTRAINER", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"ACTIVER/DESACTIVER", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"GESTION DE DONNEES", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Texte explicatif", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Bot", None))
        self.pushButton_8.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.minimize_window_button.setText("")
        self.pushButton_3.setText("")
        self.close_window_button.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"KAICE v1.0 (C) 2022 ", None))
    # retranslateUi

