import socket



host = 'localhost'
port = 8000

class ConexaoCliente:

	def __init__(self):
		self.endereco = None
		self.clienteSocket = None



	def conectar(self):
		self.endereco = ((host, port))
		self.clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clienteSocket.connect(self.endereco)



	def comunicar(self, dados): # dados: str
		self.clienteSocket.send(dados.encode())
		dadosRecebidos = self.clienteSocket.recv(1024).decode()


		return dadosRecebidos



	def fechar(self):
		self.clienteSocket.send('Close'.encode())
		self.clienteSocket.close()