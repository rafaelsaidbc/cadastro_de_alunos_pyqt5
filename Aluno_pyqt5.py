from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import*
import sys
import sqlite3
import time
import os


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('g2.png'))
        # criação de menu
        file_menu = self.menuBar().addMenu('&File')
        file_menu = self.menuBar().addMenu('&Ajuda')
        # título da janela
        self.setWindowTitle('Cadastro de alunos em PYQT5')
        # medidas
        self.setMinimumSize(800, 600)

        # tabela
        self.tableWidget = QTableWidget()
        #centraliza a tabela
        self.setCentralWidget(self.tableWidget)
        # sublinha de azul a linha selecionada
        self.tableWidget.setAlternatingRowColors(True)
        #define o numero de colunas e linhas
        self.tableWidget.setColumnCount(6)
        #ajusta automaticamente as colunas
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        # ajusta automaticamente as células
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        # cabeçalho da tabela
        self.tableWidget.setHorizontalHeaderLabels(('Inscrição Nº', 'Nome', 'Filial', 'Semestre', 'Telefone', 'Endereço'))

#cria a aplicação
app = QApplication(sys.argv)
#cria a janela principal
if (QDialog.Accepted == True):
    window = MainWindow()
    window.show()
#sai do programa
sys.exit(app.exec_())

