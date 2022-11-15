# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question_responseqZUXup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(789, 89)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plaintext_question = QPlainTextEdit(Form)
        self.plaintext_question.setObjectName(u"plaintext_question")

        self.horizontalLayout_2.addWidget(self.plaintext_question)

        self.plaintext_reponse = QPlainTextEdit(Form)
        self.plaintext_reponse.setObjectName(u"plaintext_reponse")

        self.horizontalLayout_2.addWidget(self.plaintext_reponse)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_enregistrer = QPushButton(Form)
        self.btn_enregistrer.setObjectName(u"btn_enregistrer")

        self.horizontalLayout.addWidget(self.btn_enregistrer)

        self.btn_supprimer = QPushButton(Form)
        self.btn_supprimer.setObjectName(u"btn_supprimer")

        self.horizontalLayout.addWidget(self.btn_supprimer)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.plaintext_question.setPlainText("")
        self.btn_enregistrer.setText(QCoreApplication.translate("Form", u"valider", None))
        self.btn_supprimer.setText(QCoreApplication.translate("Form", u"supprimer", None))
    # retranslateUi

