# from conta import Conta
# from cliente import Cliente



class Banco:

	#__slots__ = []

	_totalContas = 1000



	@staticmethod
	def totalContas():
		return Banco._totalContas



	def __init__(self):
		self._clientes = []
		self._contas = {}



	def buscaCliente(self, cpf):
		aux = None


		for l in self._clientes:
			if(l.cpf == cpf):
				aux = l
				break


		return aux



	def buscaConta(self, cpf):
		aux = None


		for l in self._contas:
			if(l == cpf):
				aux = self._contas[l]
				break


		return aux



	def cadastraCliente(self, cliente):
		aux = False


		busca = self.buscaCliente(cliente.cpf)
		if(busca == None):
			self._clientes.append(cliente)
			aux = True


		return aux



	def criaConta(self, cpf, conta):
		aux = False


		busca = self.buscaConta(cpf)
		if(busca == None):
			self._contas[cpf] = conta
			Banco._totalContas += 1
			aux = True


		return aux