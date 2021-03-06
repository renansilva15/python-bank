import socket
import threading



from conta import Conta
from cliente import Cliente
from historico import Historico
from banco import Banco



class ConexaoServidor(threading.Thread):

	def __init__(self, banco, clienteEndereco, conexao):
		threading.Thread.__init__(self)


		self.banco = banco
		self.clienteEndereco = clienteEndereco
		self.conexao = conexao
		print("Conexão com {}.".format(self.clienteEndereco))




	def run(self):
		while(self.funcionalidades() != False):
			pass



	def funcionalidades(self):
		dados = self.conexao.recv(1024).decode()
		listaDados = dados.split('/')


		if(listaDados[0] == '1'): # Cadastro.


			aux = self.banco.cadastraCliente(Cliente(listaDados[3], listaDados[4], listaDados[1], listaDados[2]))
			if(aux):
				aux2 = self.banco.criaConta(listaDados[1], Conta(Banco.totalContas(), listaDados[1], 0.0, 0.0))
				print('\nCadastrou.')
				self.conexao.send('True'.encode())


			else:
				print('\nNão cadastrou.')
				self.conexao.send('False'.encode())


		elif(listaDados[0] == '2'): # Acesso.
			aux = self.banco.buscaCliente(listaDados[1])


			if(aux and aux.senha == listaDados[2]):
				print('\nAcessou.')
				self.conexao.send('True'.encode())

			else:
				print('\nNão acessou.')
				self.conexao.send('False'.encode())


		elif(listaDados[0] == '3'): # Número da conta.
			print('\nNúmero da conta.')
			aux = self.banco.buscaConta(listaDados[1])


			if(aux):
				self.conexao.send('{}'.format(aux.numero).encode())


		elif(listaDados[0] == '4'): # Nome e saldo.
			print('\nNome e saldo.')
			aux = self.banco.buscaCliente(listaDados[1])


			if(aux):
				aux2 = self.banco.buscaConta(listaDados[1])
				self.conexao.send('{}/{}'.format(aux.nome, aux2.saldo).encode())


		elif(listaDados[0] == '5'):	# Histórico
			print('\nHistórico.')
			aux = self.banco.buscaCliente(listaDados[1])


			if(aux):
				aux2 = self.banco.buscaConta(listaDados[1]) # Mudar a linha debaixo.
				self.conexao.send('{}/{}/{}/{}/{:.2f}/{:.2f}'.format(aux2.numero, aux.nome, aux.sobrenome, aux.cpf, float(aux2.saldo), float(aux2.limite)).encode())


		elif(listaDados[0] == '6'):	# Depósito.
			aux = self.banco.buscaCliente(listaDados[1])


			if(aux and aux.senha == listaDados[2]):
				aux2 = self.banco.buscaConta(listaDados[1])
				aux2.deposita(float(listaDados[3]))


				print('\nDepositou.')
				self.conexao.send('True'.encode())


			else:
				print('\nNão depositou.')
				self.conexao.send('False'.encode())


		elif(listaDados[0] == '7'):	# Saque.
			aux = self.banco.buscaCliente(listaDados[1])
			aux2 = self.banco.buscaConta(listaDados[1])


			if(aux and aux.senha == listaDados[2] and aux2.saca(float(listaDados[3]))):
				print('\nSacou')
				self.conexao.send('True'.encode())


			else:
				print('\nNão sacou.')
				self.conexao.send('False'.encode())


		elif(listaDados[0] == '8'):	# Transferência.
			aux = self.banco.buscaCliente(listaDados[1])
			aux2 = self.banco.buscaConta(listaDados[1])
			aux3 = self.banco.buscaConta(listaDados[4])


			if(aux and aux.senha == listaDados[2] and aux2.transfere(aux3, float(listaDados[3]))):
				print('\nTransferiu')
				self.conexao.send('True'.encode())


			else:
				print('\nNão transferiu.')
				self.conexao.send('False'.encode())


		elif(listaDados[0] == '9'):
			print('\nExtrato.')
			aux2 = self.banco.buscaConta(listaDados[1])


			if(aux2): # Mudar...
				self.conexao.send('{}'.format(aux2.extrato()).encode())


		else:
			return False


		return True



	# def fechar(self):
	# 	self.socket.close()
	# 	print('\nFechado.')



if __name__ == '__main__':
	banco = Banco()


	host = 'localhost'
	port = 8000


	endereco = (host, port) #
	servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	servidor.bind(endereco)



	print('\nServidor iniciado.')
	print('\nAguardando conexão.')


	while(True):
		servidor.listen(1)
		conexao, clienteEndereco = servidor.accept()


		novaThread = ConexaoServidor(banco, clienteEndereco, conexao)
		novaThread.start()