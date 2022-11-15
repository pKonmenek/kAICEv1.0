from datetime import datetime
from gui.question_reponse import QuestionReponse
from gui.ui_main import *
from PySide2.QtWidgets import QMainWindow, QListWidgetItem
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPalette
import threading
import os
from loguru import logger
from gui.chip import Chip
from gui.splash_screen import SplashScreen

from kaice.chatbot import ChatBot, BotState
from kaice.settings import CSS_DIR
from kaice.models import Message, Reply
# BEDFE4


class KaiceApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        self.ui = Ui_MainWindow()
        QMainWindow.__init__(self, *args, **kwargs)
        self.chatbot = ChatBot()
        self.bot_state = BotState.NOT_STARTED
        self.ui.setupUi(self)
        self.setup_ui()
        # self.fix_style()

    def setup_ui(self):
        self.setWindowTitle("kAICE")
        self.set_theme('dark')
        self.animation = QPropertyAnimation(self.ui.frame_sm, b"minimumWidth")
        self.animation.setDuration(100)
        self.ui.statusbar.hide()
        self.ui.lbl_login_error.setVisible(False)
        self.ui.fld_password.textChanged.connect(
            lambda x: self.ui.lbl_login_error.setVisible(False))
        self.ui.fld_username.textChanged.connect(
            lambda x: self.ui.lbl_login_error.setVisible(False))
        self.ui.btn_swich_theme.clicked.connect(self.toggle_theme)
        self.ui.btn_hamburger.clicked.connect(self.toggle_side_menu)
        self.ui.btn_connection.clicked.connect(self.login)
        self.ui.cbx_dropdown_user.currentTextChanged.connect(
            self.handle_user_dropdown)
        self.ui.btn_apropos.clicked.connect(lambda: self.swich_page(
            self.ui.page_apropos, self.ui.stck_contents))
        self.ui.btn_messagerie.clicked.connect(
            lambda: self.swich_page(
                self.ui.page_message,
                self.ui.stck_contents)
        )
        self.ui.btn_gerer.clicked.connect(lambda: self.swich_page(
            self.ui.page_bot, self.ui.stck_contents))
        self.ui.btn_stats.clicked.connect(lambda: self.swich_page(
            self.ui.page_stats, self.ui.stck_contents))
        self.ui.btn_parametres.clicked.connect(lambda: self.swich_page(
            self.ui.page_parametres, self.ui.stck_contents))
        self.ui.btn_ajouter_contact.clicked.connect(self.add_contact)
        self.ui.btn_activer.clicked.connect(self.on_off_bot)
        self.ui.fld_ajouter_contact.returnPressed.connect(self.add_contact)
        self.ui.pushButton_9.clicked.connect(self.rec_send_message)
        # self.fix_style()
        self.ui.dt_edit.setDateTime(QDateTime())
        self.load_unreplied_messages()

    def fix_style(self):
        self.ui.cbx_dropdown_user.view().setMinimumWidth(64)
        p = self.ui.table_entrainement.palette()
        p.setColor(QPalette.Base, Qt.blue)
        self.ui.table_entrainement.setPalette(p)

    def set_theme(self, name):
        style = ""
        try:
            with open(f"{CSS_DIR + os.sep + name}.css", 'r') as f:
                for line in f:
                    style += line
            self.setStyleSheet(style)
            self.theme = name
        except FileNotFoundError:
            logger.error(
                "Le fichier de style {}.css est introuvable".format(name))

    def toggle_theme(self):
        if self.theme == 'dark':
            self.set_theme('light')
        else:
            self.set_theme('dark')

    def toggle_side_menu(self):
        width = self.ui.frame_sm.width()

        width_extended = 256 if width == 0 else 0
        if width == 0:
            width_extended = 256
            self.ui.btn_hamburger.setIcon(QIcon(u":/icons/assets/back.png"))
        else:
            self.ui.btn_hamburger.setIcon(QIcon(u":/icons/assets/menu.png"))
            width_extended = 0

        self.animation.setEndValue(width_extended)
        self.animation.start()

    def on_off_bot(self):
        if self.bot_state == BotState.NOT_STARTED:
            self.chatbot.start()
            self.bot_state = BotState.STARTED
            th = threading.Thread(target=self.chatbot.start_chatting)
            th.setDaemon(True)
            th.start()
            # self.chatbot.start()
            self.bot_state = BotState.ON
        else:
            self.chatbot.toggle_state()
            if self.bot_state == BotState.ON:
                self.bot_state = BotState.OFF
            else:
                self.bot_state = BotState.ON

    def login(self):
        username = self.ui.fld_username.text()
        if self.ui.fld_username.text() == 'admin' and\
                self.ui.fld_password.text() == 'admin':
            self.ui.fld_username.clear()
            self.ui.fld_password.clear()
            self.swich_page(self.ui.page_main, self.ui.stck_main)
            self.ui.lbl_username.setText(username)
        else:
            self.ui.lbl_login_error.setVisible(True)

    def handle_user_dropdown(self):
        if self.ui.cbx_dropdown_user.currentIndex() == 1:
            self.logout()
            self.ui.cbx_dropdown_user.setCurrentIndex(0)

    def logout(self):
        self.swich_page(self.ui.page_login, self.ui.stck_main)

    def swich_page(self, page, stacked_widget: QStackedWidget):
        """Permet d'aller a la page  `page` du `statcked_widget`
           passe en parametre.
        """
        index = stacked_widget.indexOf(page)
        stacked_widget.setCurrentIndex(index)

    def add_contact(self):
        """Ajoute un contact dans la liste des contacts d'envoi
            recursif de messages.
        """
        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 32))
        name = self.ui.fld_ajouter_contact.text()
        c = Chip(name)
        c.item_removed.connect(self.remove_contact)
        self.ui.list_chips.addItem(item)
        self.ui.list_chips.setItemWidget(item, c)
        self.ui.fld_ajouter_contact.clear()

    def remove_contact(self, item_chip):
        """Retire un contact dans la liste des contacts a envoyer
           recursivement les messages.
        """
        for i in range(self.ui.list_chips.count()):
            item = self.ui.list_chips.item(i)
            chip = self.ui.list_chips.itemWidget(item)
            if item_chip is chip:
                self.ui.list_chips.model().removeRow(i)

    def load_unreplied_messages(self):
        unreplieds_msgs = Message.select().where(
            Message.id.not_in(Reply.select(Reply.received_id))
            &
            Message.id.not_in(Reply.select(Reply.replied_id))
            )
        for msg in unreplieds_msgs:
            self.add_questionresponse(msg.id, msg.text)

    def add_questionresponse(self, id, question, response=""):
        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 56))
        qr = QuestionReponse(id, question, response)

        qr.item_deleted.connect(self.remove_questionreponse)
        qr.item_saved.connect(self.save_questionreponse)
        self.ui.list_questionreponses.addItem(item)
        self.ui.list_questionreponses.setItemWidget(item, qr)

    def remove_questionreponse(self, item_qr):
        i = self.find_item_in_listwidget(
            self.ui.list_questionreponses,
            item_qr
        )
        if i is not None:
            self.ui.list_questionreponses.model().removeRow(i)
            # query = Message.delete(text=item_qr.question).where(id=item_qr.id)
            Message.delete_by_id(item_qr.id)
            # query.execute()

    def save_questionreponse(self, item_qr):
        i = self.find_item_in_listwidget(
            self.ui.list_questionreponses,
            item_qr
        )
        if i is not None:
            if len(item_qr.response):
                self.ui.list_questionreponses.model().removeRow(i)
                query = Message.update({Message.text:item_qr.question}).where(Message.id==item_qr.id)
                query.execute()

                msg = Message.create(text=item_qr.response)
                msg.save()
                rep = Reply.create(received_id=item_qr.id, replied_id=msg.id)
                rep.save()
                self.chatbot.update_corpus()

    def find_item_in_listwidget(self, listw, obj):
        idx = None
        for i in range(listw.count()):
            item = listw.item(i)
            o = listw.itemWidget(item)
            if obj is o:
                idx = i
        return idx

    def rec_send_message(self):
        """Envoi recursivement les messages aux contacts saisies"""
        contacts = []
        for i in range(self.ui.list_chips.count()):
            item = self.ui.list_chips.item(i)
            chip = self.ui.list_chips.itemWidget(item)
            contacts.append(chip.text.strip())
        msg = self.ui.textEdit.toPlainText()
        dt = self.ui.dt_edit.dateTime().toPython()
        self.chatbot.schedule_rec_msg(contacts, msg, 1, dt)
        self.ui.textEdit.clear()

    def show(self) -> None:
        self.move(self.screen().geometry().center() -
                  self.frameGeometry().center())
        return super().show()


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    kaiceapp = KaiceApp()
    splash = SplashScreen(kaiceapp)
    sys.exit(app.exec_())
