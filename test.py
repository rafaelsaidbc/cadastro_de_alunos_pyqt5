from PyQt5.QtCore import*
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import*
import sys
import sqlite3
import time
import os


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowsIcon(QIcon('icon/g2.png'))

        file_menu = self.menuBar().addMenu("&File")
        self.setWindowTitle('CADASTRO DE ALUNOS EM PYQT5')
        self.setMinimumSize(800, 600)


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = MainWindow()
    window.show()
sys.exit(app.exec_())
