from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from gui.ui_question_response import *

class QuestionReponse(QWidget):
    item_saved = Signal(object)
    item_deleted = Signal(object)

    def __init__(self, id, question="", response=""):
        self.id = id
        self.ui = Ui_Form()
        QWidget.__init__(self)
        self.ui.setupUi(self)
        self.question = question
        self.response = response
        self.setup_ui()

    def setup_ui(self):
        self.ui.btn_enregistrer.clicked.connect(
            lambda x: self.item_saved.emit(self)
        )
        self.ui.btn_supprimer.clicked.connect(
            lambda x: self.item_deleted.emit(self)
        )
        

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def question(self):
        return self.ui.plaintext_question.toPlainText()

    @question.setter
    def question(self, question):
        self.ui.plaintext_question.setPlainText(question)

    @property
    def response(self):
        return self.ui.plaintext_reponse.toPlainText()

    @response.setter
    def response(self, response):
        self.ui.plaintext_reponse.setPlainText(response)

if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    main = QuestionReponse(1, "Salut", "Comment tu vas ?")
    main.show()
    sys.exit(app.exec_())