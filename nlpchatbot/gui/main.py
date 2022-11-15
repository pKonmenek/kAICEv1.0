from curses import window
import os
import sys
import os
from PySide2 import *

#from icons import icon_rc
from PyQt5 import QtCore, QtGui
from ui_interface import *


class MainWindow(QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # # Remove window title bar
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # # Set main background to transparent
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,92,157,550))

        # Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Set window Icon
        # self.setWindowIcon(QtGui.QIcon(""))

        # Set window title
        self.setWindowTitle("KAICE")

        # Window size grip to resize window
        QSizeGrip(self.ui.sixe_grip)

        # Minimize window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        # Close window
        self.ui.close_window_button.clicked.connect(lambda: self.close())

        self.show()

# Execute app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())