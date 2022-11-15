from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
from gui.ui_chip import *
from kaice.settings import CSS_DIR

class Chip(QWidget):

    item_removed = Signal(object)

    def __init__(self, text, *args, **kwargs):
        self._text = text
        self.ui = Ui_Form()
        QWidget.__init__(self)
        self.ui.setupUi(self)
        self.setup_ui()


    def setup_ui(self):
        self.ui.lbl_text.setText(self.text)
        style = ""
        with open(CSS_DIR+"/dark.css", 'r') as f:
            for line in f:
                style+=line
        self.setStyleSheet(style)
        self.ui.btn_close.clicked.connect(lambda x: \
            self.item_removed.emit(self))

    @property
    def text(self)->str:
        return self._text

    @text.setter
    def text(self, text:str)->None:
        self._text = text
        self.ui.lbl_text.setText(text)

    

    


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    main = Chip("Kouam franck Joel Gaetan")
    main.show()
    sys.exit(app.exec_())