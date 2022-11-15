from PySide2.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt, QTimer
from gui.ui_splash_screen import Ui_SplashScreen

class SplashScreen(QMainWindow):
    def __init__(self, mainapp = None):
        QMainWindow.__init__(self)
        self.mainapp = mainapp
        self.counter = 0
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # UI ==> INTERFACE CODES
        ########################################################################

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText(
            "<strong>BIENVENUE</strong> SUR kAICE")

        # Change Texts
        QTimer.singleShot(1500, lambda: self.ui.label_description.setText(
            "<strong>CHARGEMENT</strong> DE LA BASE DE DONNEES"))
        QTimer.singleShot(3000, lambda: self.ui.label_description.setText(
            "<strong>CHARGEMENT</strong> DE L'INTERFACE UTILISATEUR"))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.move(self.screen().geometry().center() -
                  self.frameGeometry().center())
        self.show()
        ## ==> END ##

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(self.counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.mainapp.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.counter += 1

    # TODO: Surcharger la methode quit
