import datetime
from historico import Historico



class Conta:

	__slots__ = ['_numero', '_cpf', '_saldo', '_limite', '_historico']



	_totalContas = 0



	@staticmethod
	def totalContas():
		return Conta._totalContas



	def __init__(self, numero, cpf, saldo, limite):
		self._numero = numero
		self._cpf = cpf
		self._saldo = float(saldo)
		self._limite = float(limite)
		self._historico = Historico()
		Conta._totalContas += 1



	@property
	def numero(self):
		return self._numero


	@numero.setter
	def numero(self, numero):
		self._numero = numero



	@property
	def cpf(self):
		return self.cpf


	@cpf.setter
	def cpf(self, cpf):
		self.cpf = cpf



	@property
	def limite(self):
		return self._limite


	@limite.setter
	def limite(self, limite):
		self._limite = limite



	@property
	def historico(self):
		return self._historico


	@historico.setter
	def historico(self, historico):
		self._historico = historico



	@property
	def saldo(self):
		return self._saldo


	@saldo.setter
	def saldo(self, saldo):
		self._saldo = saldo



	def deposita(self, valor):
		aux = False


		if(valor > 0):
			self._saldo += valor
			self._historico.transacoes.append('+ Depósito de R$ {:.2f} ({})\n'.format(valor, datetime.datetime.today().strftime('%d/%m/%Y %H:%M')))
			aux = True


		return aux



	def saca(self, valor):
		aux = False


		if(valor > 0 and self._saldo >= valor):
			self._saldo -= valor
			self._historico.transacoes.append('- Saque de R$ {:.2f} ({})\n'.format(valor, datetime.datetime.today().strftime('%d/%m/%Y %H:%M')))
			aux = True


		return aux



	def extrato(self):
		#print('\nNúmero: {}\nTitular: {} {} | CPF: {}\nSaldo: R$ {:.2f}\nLimite: R$ {:.2f}'.format(self._numero, self._cliente.nome, self._cliente.sobrenome, self._cliente.cpf, self._saldo, self._limite))
	 	return self._historico.mostra()



	def transfere(self, destino, valor):
		aux = False


		if(type(destino) == type(self) and valor > 0 and self._saldo >= valor):
			self._saldo -= valor
			destino._saldo += valor


			self._historico.transacoes.append('- Transferência de R$ {:.2f} para a conta "{}" ({})\n'.format(valor, destino._numero, datetime.datetime.today().strftime('%d/%m/%Y %H:%M')))
			destino._historico.transacoes.append('+ Recebe transferência de R$ {:.2f} da conta "{}" ({})\n'.format(valor, self._numero, datetime.datetime.today().strftime('%d/%m/%Y %H:%M')))
			aux = True


		return aux