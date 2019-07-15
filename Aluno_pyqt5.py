import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# função para inserir dados dos alunos
class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText('Registrar')

        # título do layout
        self.setWindowTitle('Adicionar aluno')
        # dimensões da janela
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle('Dados do aluno')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.addstudent)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText('Nome')
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem('Engenharia Química')
        self.branchinput.addItem('Engenharia Elétrica')
        self.branchinput.addItem('Engenharia Eletrônica')
        self.branchinput.addItem('Engenharia de Computação')
        self.branchinput.addItem('Tencologia da Informação')

        layout.addWidget(self.branchinput)

        self.seminput = QComboBox()
        self.seminput.addItem('1')
        self.seminput.addItem('2')
        self.seminput.addItem('3')
        self.seminput.addItem('4')
        self.seminput.addItem('5')
        self.seminput.addItem('6')
        self.seminput.addItem('7')
        self.seminput.addItem('8')

        layout.addWidget(self.seminput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText('Telefone nº')
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText('Endereço')
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addstudent(self):
        name = ''
        branch = ''
        sem = -1
        mobile = ''
        address = ''

        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        # dimensões da janela
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        # abre ao clicar no botão
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        # cria o objeto layout
        layout = QVBoxLayout()

        # título do layout
        self.setWindowTitle('Sobre')
        title = QLabel('Cadastro de alunos em PYQT5')
        # cria a fonte
        font = title.font()
        # configura a fonte
        font.setPointSize(20)
        title.setFont(font)

        # imagem do layout
        labelpic = QLabel()
        # campo
        pixmap = QPixmap('help.jpg')
        # largura do objeto
        pixmap = pixmap.scaledToWidth(275)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)

        # adiciona mensagens ao layout
        layout.addWidget(QLabel('V 5.0'))
        layout.addWidget(QLabel('Copyright Rafa Said 2019'))
        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('g2.png'))
        # criação de menu
        file_menu = self.menuBar().addMenu('&File')
        help_menu = self.menuBar().addMenu('&Ajuda')
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

        # toolbar
        toolbar = QToolBar()
        # fixa a toolbar, não permite movimento
        toolbar.setMovable(False)
        # self é o formulário (janela), adiciona o toolbar a janela
        self.addToolBar(toolbar)
        # adiciona um botão na toolbar
        btn_ac_adduser = QAction(QIcon('add.png'), "Adicionar", self)
        btn_ac_adduser.triggered.connect(self.insert)
        # da visibilidade ao título
        btn_ac_adduser.setStatusTip('Adicionar aluno')
        toolbar.addAction(btn_ac_adduser)

        # adiciona um botão na toolbar
        btn_ac_refresh = QAction(QIcon('update.png'), "Atualizar", self)
        # da visibilidade ao título
        btn_ac_refresh.setStatusTip('Atualizar dados do Aluno')
        toolbar.addAction(btn_ac_refresh)

        # adiciona um botão na toolbar
        btn_ac_search = QAction(QIcon('search.png'), "Pesquisar", self)
        # da visibilidade ao título
        btn_ac_search.setStatusTip('Pesquisar por Aluno')
        toolbar.addAction(btn_ac_search)

        # adiciona um botão na toolbar
        btn_ac_delete = QAction(QIcon('delete.png'), "Deletar", self)
        # da visibilidade ao título
        btn_ac_delete.setStatusTip('Deletar cadastro do aluno')
        toolbar.addAction(btn_ac_delete)

        # adiciona um botão na toolbar
        about_action = QAction(QIcon('about.png'), "Desenvolvedor", self)
        # da visibilidade ao título
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()



#cria a aplicação
app = QApplication(sys.argv)
#cria a janela principal
if (QDialog.Accepted == True):
    window = MainWindow()
    window.show()
#sai do programa
sys.exit(app.exec_())

