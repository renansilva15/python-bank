from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication


from telaInicial import TelaInicial
from telaCadastro import TelaCadastro
from telaPrincipal import TelaPrincipal
from telaDeposito import TelaDeposito
from telaSaque import TelaSaque
from telaTransferencia import TelaTransferencia
from telaHistorico import TelaHistorico


from conexaoCliente import ConexaoCliente



class Ui_Main(QtWidgets.QWidget):

	def setupUi(self, Main):
		Main.setObjectName('Main')
		Main.resize(640, 480)


		self.QtStack = QtWidgets.QStackedLayout()


		self.stack0 = QtWidgets.QMainWindow()
		self.stack1 = QtWidgets.QMainWindow()
		self.stack2 = QtWidgets.QMainWindow()
		self.stack3 = QtWidgets.QMainWindow()
		self.stack4 = QtWidgets.QMainWindow()
		self.stack5 = QtWidgets.QMainWindow()
		self.stack6 = QtWidgets.QMainWindow()


		self.cpfAtual = None
		self.conexaoCliente = ConexaoCliente()
		self.conexaoCliente.conectar()


		self.telaInicial = TelaInicial()
		self.telaInicial.setupUi(self.stack0)

		self.telaPrincipal = TelaPrincipal()
		self.telaPrincipal.setupUi(self.stack1)

		self.telaCadastro = TelaCadastro()
		self.telaCadastro.setupUi(self.stack2)

		self.telaDeposito = TelaDeposito()
		self.telaDeposito.setupUi(self.stack3)

		self.telaSaque = TelaSaque()
		self.telaSaque.setupUi(self.stack4)

		self.telaTransferencia = TelaTransferencia()
		self.telaTransferencia.setupUi(self.stack5)

		self.telaHistorico = TelaHistorico()
		self.telaHistorico.setupUi(self.stack6)


		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		self.QtStack.addWidget(self.stack3)
		self.QtStack.addWidget(self.stack4)
		self.QtStack.addWidget(self.stack5)
		self.QtStack.addWidget(self.stack6)



class Main(QMainWindow, Ui_Main):

	def __init__(self, parent = None):
		super(Main, self).__init__(parent)
		self.setupUi(self)


		self.telaInicial.pushButton.clicked.connect(self.abrirTelaPrincipal)
		self.telaInicial.pushButton_2.clicked.connect(self.abrirTelaCadastro)


		self.telaCadastro.pushButton.clicked.connect(self.botaoCadastro)
		self.telaCadastro.pushButton_2.clicked.connect(self.botaoVoltarTelaInicial)


		self.telaPrincipal.pushButton_2.clicked.connect(self.abrirTelaDeposito)
		self.telaDeposito.pushButton.clicked.connect(self.botaoDeposito)
		self.telaDeposito.pushButton_2.clicked.connect(self.botaoVoltarTelaPrincipal)


		self.telaPrincipal.pushButton.clicked.connect(self.abrirTelaSaque)
		self.telaSaque.pushButton.clicked.connect(self.botaoSaque)
		self.telaSaque.pushButton_2.clicked.connect(self.botaoVoltarTelaPrincipal)


		self.telaPrincipal.pushButton_4.clicked.connect(self.abrirTelaTransferencia)
		self.telaTransferencia.pushButton.clicked.connect(self.botaoTransferencia)
		self.telaTransferencia.pushButton_2.clicked.connect(self.botaoVoltarTelaPrincipal)


		self.telaPrincipal.pushButton_3.clicked.connect(self.abrirTelaHistorico)
		self.telaHistorico.pushButton_2.clicked.connect(self.botaoVoltarTelaPrincipal)


		self.telaPrincipal.pushButton_5.clicked.connect(self.botaoVoltarTelaInicial)



	def abrirTelaPrincipal(self):
		cpf = self.telaInicial.lineEdit.text()
		senha = self.telaInicial.lineEdit_2.text()


		if(not(cpf == '' or senha == '')):
			self.cpfAtual = cpf
			aux = self.conexaoCliente.comunicar("{}/{}/{}".format(2, self.cpfAtual, senha))


			if(aux == 'True'):
				self.telaInicial.lineEdit.setText('')
				self.telaInicial.lineEdit_2.setText('')


				aux = self.conexaoCliente.comunicar("{}/{}".format(4, self.cpfAtual))
				aux = aux.split('/')


				self.telaPrincipal.label_2.setText(str('Olá %s' %(aux[0])))
				self.telaPrincipal.label_3.setText(str('Saldo R$ %.2f' %(float(aux[1]))))


				self.telaDeposito.lineEdit_3.setText('')
				self.telaDeposito.lineEdit_4.setText('')


				self.telaSaque.lineEdit_3.setText('')
				self.telaSaque.lineEdit_4.setText('')


				self.telaTransferencia.lineEdit_3.setText('')
				self.telaTransferencia.lineEdit_5.setText('')
				self.telaTransferencia.lineEdit_4.setText('')
				self.QtStack.setCurrentIndex(1)


			else:
				self.telaInicial.lineEdit.setText('')
				self.telaInicial.lineEdit_2.setText('')
				QMessageBox.information(None, '', 'Não foi possível acessar, verifique seu CPF e senha.')


		else:
			QMessageBox.information(None, '', 'Prencha todos os campos.')



	def abrirTelaCadastro(self):
		self.telaInicial.lineEdit.setText('')
		self.telaInicial.lineEdit_2.setText('')
		self.QtStack.setCurrentIndex(2)



	def botaoCadastro(self):
		nome = self.telaCadastro.lineEdit_3.text()
		sobrenome = self.telaCadastro.lineEdit_4.text()
		cpf = self.telaCadastro.lineEdit.text()
		senha = self.telaCadastro.lineEdit_2.text()


		if(not(nome == '' or sobrenome == '' or cpf == '' or senha == '')):
			self.cpfAtual = cpf
			aux = self.conexaoCliente.comunicar("{}/{}/{}/{}/{}".format(1, self.cpfAtual, senha, nome, sobrenome))


			if(aux == 'True'):
				self.telaCadastro.lineEdit_3.setText('')
				self.telaCadastro.lineEdit_4.setText('')
				self.telaCadastro.lineEdit.setText('')
				self.telaCadastro.lineEdit_2.setText('')


				aux = int(self.conexaoCliente.comunicar("{}/{}".format(3, self.cpfAtual)))


				QMessageBox.information(None, '', 'Cadastro realizado.\n\nO número da sua conta é: %d' %(aux))
				self.QtStack.setCurrentIndex(0)

			else:
				QMessageBox.information(None, '', 'Não foi possível realizar o cadastro.')


		else:
			QMessageBox.information(None, '', 'Prencha todos os campos.')



	def botaoVoltarTelaInicial(self):
		self.telaCadastro.lineEdit_3.setText('')
		self.telaCadastro.lineEdit_4.setText('')
		self.telaCadastro.lineEdit.setText('')
		self.telaCadastro.lineEdit_2.setText('')


		self.QtStack.setCurrentIndex(0)



	def abrirTelaDeposito(self):
		self.QtStack.setCurrentIndex(3)



	def botaoDeposito(self):
		valor = float(self.telaDeposito.lineEdit_3.text())
		senha = self.telaDeposito.lineEdit_4.text()


		if(not(valor == '' or senha == '')):
			if(valor > 0):


				aux = self.conexaoCliente.comunicar("{}/{}/{}/{}".format(6, self.cpfAtual, senha, valor))
				if(aux == 'True'):
					self.telaDeposito.lineEdit_3.setText('')
					self.telaDeposito.lineEdit_4.setText('')
					QMessageBox.information(None, '', 'Depósito realizado.')


					aux = self.conexaoCliente.comunicar("{}/{}".format(4, self.cpfAtual))
					aux = aux.split('/')


					self.telaPrincipal.label_3.setText(str('Saldo R$ %.2f' %(float(aux[1]))))


					self.QtStack.setCurrentIndex(1)


				else:
					self.telaDeposito.lineEdit_4.setText('')
					QMessageBox.information(None, '', 'Não foi possível realizar o depósito, senha incorreta.')

			else:
				QMessageBox.information(None, '', 'Valor inválido.')

		else:
			QMessageBox.information(None, '', 'Prencha todos os campos.')



	def botaoVoltarTelaPrincipal(self):
		self.QtStack.setCurrentIndex(1)



	def abrirTelaSaque(self):
		self.QtStack.setCurrentIndex(4)



	def botaoSaque(self):
		valor = float(self.telaSaque.lineEdit_3.text())
		senha = self.telaSaque.lineEdit_4.text()


		if(not(valor == '' or senha == '')):
			if(valor > 0):


				aux = self.conexaoCliente.comunicar("{}/{}/{}/{}".format(7, self.cpfAtual, senha, valor))
				if(aux == 'True'):
					self.telaSaque.lineEdit_3.setText('')
					self.telaSaque.lineEdit_4.setText('')
					QMessageBox.information(None, '', 'Saque realizado.')


					aux = self.conexaoCliente.comunicar("{}/{}".format(4, self.cpfAtual))
					aux = aux.split('/')


					self.telaPrincipal.label_3.setText(str('Saldo R$ %.2f' %(float(aux[1]))))


					self.QtStack.setCurrentIndex(1)


				else:
					self.telaDeposito.lineEdit_4.setText('')
					QMessageBox.information(None, '', 'Não foi possível realizar o saque, verifique seu saldo e sua senha.')

			else:
				QMessageBox.information(None, '', 'Valor inválido.')

		else:
			QMessageBox.information(None, '', 'Prencha todos os campos.')



	def abrirTelaTransferencia(self):
		self.QtStack.setCurrentIndex(5)



	def botaoTransferencia(self):
		valor = float(self.telaTransferencia.lineEdit_3.text())
		cpfDestino = self.telaTransferencia.lineEdit_5.text()
		senha = self.telaTransferencia.lineEdit_4.text()


		if(not(valor == '' or cpfDestino == '' or senha == '')):
			if(valor > 0):


				aux = self.conexaoCliente.comunicar("{}/{}/{}/{}/{}".format(8, self.cpfAtual, senha, valor, cpfDestino))
				if(aux == 'True'):
					self.telaTransferencia.lineEdit_3.setText('')
					self.telaTransferencia.lineEdit_5.setText('')
					self.telaTransferencia.lineEdit_4.setText('')
					QMessageBox.information(None, '', 'Transferência realizada.')


					aux = self.conexaoCliente.comunicar("{}/{}".format(4, self.cpfAtual))
					aux = aux.split('/')


					self.telaPrincipal.label_3.setText(str('Saldo R$ %.2f' %(float(aux[1]))))


					self.QtStack.setCurrentIndex(1)


				else:
					self.telaDeposito.lineEdit_4.setText('')
					QMessageBox.information(None, '', 'Não foi possível realizar o saque, verifique seu saldo, sua senha e o CPF da conta destino.')

			else:
				QMessageBox.information(None, '', 'Valor inválido.')

		else:
			QMessageBox.information(None, '', 'Prencha todos os campos.')



	def abrirTelaHistorico(self):
		aux = self.conexaoCliente.comunicar("{}/{}".format(5, self.cpfAtual))
		aux = aux.split('/')


		aux2 = self.conexaoCliente.comunicar("{}/{}".format(9, self.cpfAtual))


		self.telaHistorico.textEdit.setText('\nNúmero: {}\nTitular: {} {} | CPF: {}\nSaldo: R$ {}\nLimite: R$ {}\n{}'.format(aux[0], aux[1], aux[2], aux[3], aux[4], aux[5], aux2))
		self.QtStack.setCurrentIndex(6)



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	show_main = Main()
	sys.exit(app.exec_())
	self.conexaoCliente.fechar()