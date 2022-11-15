# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainswVjAF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from gui import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 717)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/icons/assets/chatbot.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.stck_main = QStackedWidget(self.centralwidget)
        self.stck_main.setObjectName(u"stck_main")
        self.stck_main.setMinimumSize(QSize(0, 0))
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.horizontalLayout_10 = QHBoxLayout(self.page_login)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.frame_login = QFrame(self.page_login)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMaximumSize(QSize(300, 400))
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_login)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.label_6 = QLabel(self.frame_login)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(92, 92))
        self.label_6.setMaximumSize(QSize(64, 64))
        self.label_6.setBaseSize(QSize(64, 64))
        self.label_6.setPixmap(QPixmap(u":/icons/assets/user_dark.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.lbl_login_error = QLabel(self.frame_login)
        self.lbl_login_error.setObjectName(u"lbl_login_error")

        self.verticalLayout_10.addWidget(self.lbl_login_error)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setVerticalSpacing(6)
        self.fld_username = QLineEdit(self.frame_login)
        self.fld_username.setObjectName(u"fld_username")
        self.fld_username.setMinimumSize(QSize(0, 38))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.fld_username)

        self.fld_password = QLineEdit(self.frame_login)
        self.fld_password.setObjectName(u"fld_password")
        self.fld_password.setMinimumSize(QSize(0, 38))
        self.fld_password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.fld_password)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 10, -1, 2)
        self.label_7 = QLabel(self.frame_login)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QSize(18, 18))
        self.label_7.setStyleSheet(u"")
        self.label_7.setPixmap(QPixmap(u":/icons/assets/arroba_dark.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_17.addWidget(self.label_7)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 10, -1, -1)
        self.label_8 = QLabel(self.frame_login)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QSize(18, 18))
        self.label_8.setBaseSize(QSize(16, 16))
        self.label_8.setPixmap(QPixmap(u":/icons/assets/padlock_dark.png"))
        self.label_8.setScaledContents(True)

        self.verticalLayout_18.addWidget(self.label_8)


        self.formLayout.setLayout(3, QFormLayout.LabelRole, self.verticalLayout_18)


        self.verticalLayout_10.addLayout(self.formLayout)

        self.btn_connection = QPushButton(self.frame_login)
        self.btn_connection.setObjectName(u"btn_connection")
        self.btn_connection.setMinimumSize(QSize(0, 38))

        self.verticalLayout_10.addWidget(self.btn_connection)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_7)


        self.verticalLayout_11.addWidget(self.frame_login)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_7 = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.stck_main.addWidget(self.page_login)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.verticalLayout_4 = QVBoxLayout(self.page_main)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(self.page_main)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(32, 0, 0, 0)
        self.btn_hamburger = QPushButton(self.frame_header)
        self.btn_hamburger.setObjectName(u"btn_hamburger")
        self.btn_hamburger.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hamburger.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/menu_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_hamburger.setIcon(icon1)
        self.btn_hamburger.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_hamburger)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_swich_theme = QPushButton(self.frame_header)
        self.btn_swich_theme.setObjectName(u"btn_swich_theme")
        self.btn_swich_theme.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_swich_theme.setStyleSheet(u"icon-btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/moon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_swich_theme.setIcon(icon2)
        self.btn_swich_theme.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_swich_theme)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.label_3 = QLabel(self.frame_header)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777213))
        self.label_3.setPixmap(QPixmap(u":/icons/assets/user.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.lbl_username = QLabel(self.frame_header)
        self.lbl_username.setObjectName(u"lbl_username")

        self.horizontalLayout.addWidget(self.lbl_username)

        self.cbx_dropdown_user = QComboBox(self.frame_header)
        self.cbx_dropdown_user.addItem("")
        self.cbx_dropdown_user.addItem("")
        self.cbx_dropdown_user.setObjectName(u"cbx_dropdown_user")
        self.cbx_dropdown_user.setMaximumSize(QSize(24, 16))

        self.horizontalLayout.addWidget(self.cbx_dropdown_user)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_4.addWidget(self.frame_header)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_sm = QFrame(self.page_main)
        self.frame_sm.setObjectName(u"frame_sm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_sm.sizePolicy().hasHeightForWidth())
        self.frame_sm.setSizePolicy(sizePolicy1)
        self.frame_sm.setMinimumSize(QSize(0, 0))
        self.frame_sm.setMaximumSize(QSize(0, 16777215))
        self.frame_sm.setBaseSize(QSize(0, 0))
        self.frame_sm.setFrameShape(QFrame.NoFrame)
        self.frame_sm.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_sm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_sm)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 100))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.btn_messagerie = QPushButton(self.frame_sm)
        self.btn_messagerie.setObjectName(u"btn_messagerie")
        self.btn_messagerie.setMinimumSize(QSize(0, 48))
        self.btn_messagerie.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/speech-bubble_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_messagerie.setIcon(icon3)
        self.btn_messagerie.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_messagerie)

        self.btn_gerer = QPushButton(self.frame_sm)
        self.btn_gerer.setObjectName(u"btn_gerer")
        self.btn_gerer.setMinimumSize(QSize(0, 48))
        self.btn_gerer.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/chatbot_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerer.setIcon(icon4)
        self.btn_gerer.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_gerer)

        self.btn_stats = QPushButton(self.frame_sm)
        self.btn_stats.setObjectName(u"btn_stats")
        self.btn_stats.setMinimumSize(QSize(0, 48))
        self.btn_stats.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/bar-chart_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stats.setIcon(icon5)
        self.btn_stats.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_stats)

        self.btn_parametres = QPushButton(self.frame_sm)
        self.btn_parametres.setObjectName(u"btn_parametres")
        self.btn_parametres.setMinimumSize(QSize(0, 48))
        self.btn_parametres.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/technical-support_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_parametres.setIcon(icon6)
        self.btn_parametres.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_parametres)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_apropos = QPushButton(self.frame_sm)
        self.btn_apropos.setObjectName(u"btn_apropos")
        self.btn_apropos.setMinimumSize(QSize(0, 48))
        self.btn_apropos.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/about_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_apropos.setIcon(icon7)
        self.btn_apropos.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_apropos)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.lbl_nom_app = QLabel(self.frame_sm)
        self.lbl_nom_app.setObjectName(u"lbl_nom_app")
        self.lbl_nom_app.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_nom_app)

        self.lbl_version = QLabel(self.frame_sm)
        self.lbl_version.setObjectName(u"lbl_version")
        self.lbl_version.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_version)


        self.horizontalLayout_4.addWidget(self.frame_sm)

        self.stck_contents = QStackedWidget(self.page_main)
        self.stck_contents.setObjectName(u"stck_contents")
        self.page_bienvenu = QWidget()
        self.page_bienvenu.setObjectName(u"page_bienvenu")
        self.verticalLayout_5 = QVBoxLayout(self.page_bienvenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.page_bienvenu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.verticalLayout_5.addWidget(self.frame_2)

        self.stck_contents.addWidget(self.page_bienvenu)
        self.page_message = QWidget()
        self.page_message.setObjectName(u"page_message")
        self.verticalLayout_7 = QVBoxLayout(self.page_message)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textEdit = QTextEdit(self.page_message)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_5.addWidget(self.textEdit)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.page_message)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_14 = QVBoxLayout(self.frame_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.fld_ajouter_contact = QLineEdit(self.frame_3)
        self.fld_ajouter_contact.setObjectName(u"fld_ajouter_contact")
        self.fld_ajouter_contact.setMinimumSize(QSize(0, 38))

        self.horizontalLayout_11.addWidget(self.fld_ajouter_contact)

        self.btn_ajouter_contact = QPushButton(self.frame_3)
        self.btn_ajouter_contact.setObjectName(u"btn_ajouter_contact")
        self.btn_ajouter_contact.setMinimumSize(QSize(128, 38))

        self.horizontalLayout_11.addWidget(self.btn_ajouter_contact)


        self.verticalLayout_14.addLayout(self.horizontalLayout_11)

        self.scrollArea_2 = QScrollArea(self.frame_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 422, 456))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.list_chips = QListWidget(self.scrollAreaWidgetContents_2)
        self.list_chips.setObjectName(u"list_chips")

        self.verticalLayout_15.addWidget(self.list_chips)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_14.addWidget(self.scrollArea_2)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.dt_edit = QDateTimeEdit(self.page_message)
        self.dt_edit.setObjectName(u"dt_edit")
        self.dt_edit.setMinimumSize(QSize(0, 38))
        self.dt_edit.setProperty("showGroupSeparator", False)
        self.dt_edit.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.dt_edit.setCalendarPopup(True)

        self.verticalLayout_6.addWidget(self.dt_edit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.pushButton_9 = QPushButton(self.page_message)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(128, 38))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_9)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.stck_contents.addWidget(self.page_message)
        self.page_bot = QWidget()
        self.page_bot.setObjectName(u"page_bot")
        self.verticalLayout_9 = QVBoxLayout(self.page_bot)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(24)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_activer = QPushButton(self.page_bot)
        self.btn_activer.setObjectName(u"btn_activer")
        self.btn_activer.setMinimumSize(QSize(164, 38))
        self.btn_activer.setMaximumSize(QSize(16777214, 16777215))
        self.btn_activer.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/power-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_activer.setIcon(icon9)
        self.btn_activer.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.btn_activer)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label = QLabel(self.page_bot)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.scrollArea_3 = QScrollArea(self.page_bot)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 852, 372))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.list_questionreponses = QListWidget(self.scrollAreaWidgetContents_3)
        self.list_questionreponses.setObjectName(u"list_questionreponses")

        self.verticalLayout_19.addWidget(self.list_questionreponses)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollArea_3)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_fichier = QPushButton(self.page_bot)
        self.btn_fichier.setObjectName(u"btn_fichier")
        self.btn_fichier.setMinimumSize(QSize(192, 38))
        self.btn_fichier.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/upload-dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fichier.setIcon(icon10)

        self.horizontalLayout_8.addWidget(self.btn_fichier)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.stck_contents.addWidget(self.page_bot)
        self.page_stats = QWidget()
        self.page_stats.setObjectName(u"page_stats")
        self.verticalLayout_16 = QVBoxLayout(self.page_stats)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.tableview_stats = QTableView(self.page_stats)
        self.tableview_stats.setObjectName(u"tableview_stats")
        self.tableview_stats.setFrameShape(QFrame.NoFrame)
        self.tableview_stats.setFrameShadow(QFrame.Plain)

        self.verticalLayout_16.addWidget(self.tableview_stats)

        self.stck_contents.addWidget(self.page_stats)
        self.page_parametres = QWidget()
        self.page_parametres.setObjectName(u"page_parametres")
        self.label_2 = QLabel(self.page_parametres)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 190, 141, 17))
        self.stck_contents.addWidget(self.page_parametres)
        self.page_apropos = QWidget()
        self.page_apropos.setObjectName(u"page_apropos")
        self.label_4 = QLabel(self.page_apropos)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 220, 131, 17))
        self.stck_contents.addWidget(self.page_apropos)

        self.horizontalLayout_4.addWidget(self.stck_contents)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.stck_main.addWidget(self.page_main)

        self.verticalLayout_8.addWidget(self.stck_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 882, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stck_main.setCurrentIndex(0)
        self.stck_contents.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        MainWindow.setProperty("class", QCoreApplication.translate("MainWindow", u"main-content", None))
        self.label_6.setText("")
        self.lbl_login_error.setText(QCoreApplication.translate("MainWindow", u"Nom d'utilsateur ou mot de passe incorrect!", None))
        self.lbl_login_error.setProperty("class", QCoreApplication.translate("MainWindow", u"error-text", None))
        self.fld_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.fld_username.setProperty("class", QCoreApplication.translate("MainWindow", u"text-entry", None))
        self.fld_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.fld_password.setProperty("class", QCoreApplication.translate("MainWindow", u"text-entry", None))
        self.label_7.setText("")
        self.label_8.setText("")
        self.btn_connection.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.btn_connection.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton", None))
        self.frame_header.setProperty("class", QCoreApplication.translate("MainWindow", u"header-frame", None))
        self.btn_hamburger.setText("")
        self.btn_hamburger.setProperty("class", QCoreApplication.translate("MainWindow", u"icon-btn", None))
        self.btn_swich_theme.setText("")
        self.btn_swich_theme.setProperty("class", QCoreApplication.translate("MainWindow", u"icon-btn", None))
        self.label_3.setText("")
        self.lbl_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lbl_username.setProperty("class", QCoreApplication.translate("MainWindow", u"label-text", None))
        self.cbx_dropdown_user.setItemText(0, "")
        self.cbx_dropdown_user.setItemText(1, QCoreApplication.translate("MainWindow", u"Deconnexion", None))

        self.frame_sm.setProperty("class", QCoreApplication.translate("MainWindow", u"sm-frame", None))
        self.btn_messagerie.setText(QCoreApplication.translate("MainWindow", u"        Messagerie", None))
        self.btn_messagerie.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton-sm", None))
        self.btn_gerer.setText(QCoreApplication.translate("MainWindow", u"        Gerer le bot", None))
        self.btn_gerer.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton-sm", None))
        self.btn_stats.setText(QCoreApplication.translate("MainWindow", u"        Statistiques", None))
        self.btn_stats.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton-sm", None))
        self.btn_parametres.setText(QCoreApplication.translate("MainWindow", u"        Parametres", None))
        self.btn_parametres.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton-sm", None))
        self.btn_apropos.setText(QCoreApplication.translate("MainWindow", u"        A propos", None))
        self.btn_apropos.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton-sm", None))
        self.lbl_nom_app.setText(QCoreApplication.translate("MainWindow", u"kAICE", None))
        self.lbl_nom_app.setProperty("class", QCoreApplication.translate("MainWindow", u"label-text", None))
        self.lbl_version.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.0", None))
        self.lbl_version.setProperty("class", QCoreApplication.translate("MainWindow", u"label-text", None))
        self.stck_contents.setProperty("class", QCoreApplication.translate("MainWindow", u"main-content", None))
        self.frame_2.setProperty("class", QCoreApplication.translate("MainWindow", u"wellcome-page", None))
        self.textEdit.setProperty("class", QCoreApplication.translate("MainWindow", u"text-entry", None))
        self.fld_ajouter_contact.setProperty("class", QCoreApplication.translate("MainWindow", u"text-entry", None))
        self.btn_ajouter_contact.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.btn_ajouter_contact.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton", None))
        self.scrollArea_2.setProperty("class", QCoreApplication.translate("MainWindow", u"main-content", None))
        self.list_chips.setProperty("class", QCoreApplication.translate("MainWindow", u"text-entry", None))
        self.dt_edit.setProperty("class", QCoreApplication.translate("MainWindow", u"text-entry", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"    Envoyer", None))
        self.pushButton_9.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton", None))
        self.btn_activer.setText(QCoreApplication.translate("MainWindow", u"     Activer le bot", None))
        self.btn_activer.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Liste des messages sans reponses", None))
        self.btn_fichier.setText(QCoreApplication.translate("MainWindow", u"    Fichier d'entrainement...", None))
        self.btn_fichier.setProperty("class", QCoreApplication.translate("MainWindow", u"bouton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Page de parametres", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Page A propos", None))
    # retranslateUi

