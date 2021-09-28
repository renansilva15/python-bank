import datetime



class Historico:

	__slots__ = ['_abertura', '_transacoes']



	def __init__(self):
		self._abertura = datetime.datetime.today().strftime('%d/%m/%Y %H:%M')
		self._transacoes = []



	'''@property
	def abertura(self):
		return self._abertura


	@abertura.setter
	def abertura(self, abertura):
		self._abertura = abertura'''



	@property
	def transacoes(self):
		return self._transacoes


	@transacoes.setter
	def transacoes(self, transacoes):
		self._transacoes = transacoes



	def mostra(self):
		print('\nData de abertura: {}'.format(self._abertura))


		print('\nTransações:\n')
		for l in self.transacoes:
			print(l)