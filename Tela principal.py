from PyQt5 import uic, QtWidgets

def chama_segunda_tela():
    primeira_tela.hide()
    segunda_tela.show()

app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi('tela de login.ui')
segunda_tela = uic.loadUi('tela de cadastro.ui')
terceira_tela = uic.loadUi('sair cadastro.ui')

primeira_tela.criar_conta.clicked.connect(chama_segunda_tela)

def login_conta():
    user = str(primeira_tela.email_login.text())
    password = str(primeira_tela.senha_login.text())

    print(f'usuario:{user} senha:{password}')

primeira_tela.logar.clicked.connect(login_conta)

def fazer_cadastro():

    name = str(segunda_tela.nome_cadastro.text())
    email = str(segunda_tela.email_cadastro.text())

    password = str(segunda_tela.senha_cadastro.text())
    conf_password = str(segunda_tela.confirmar_senha.text())

    print(f'nome: {name} email: {email} senha: {password} confirma senha: {conf_password}')



segunda_tela.cadastrar.clicked.connect(fazer_cadastro)

def chama_terceira_tela():
    terceira_tela.show()
    segunda_tela.hide()

segunda_tela.cadastrar.clicked.connect(chama_terceira_tela)

def chama_primeira_tela():
    terceira_tela.hide()
    primeira_tela.show()

terceira_tela.login_cadastro.clicked.connect(chama_primeira_tela)







primeira_tela.show()
app.exec()


