class Cliente:

	__slots__ = ['_nome', '_sobrenome', '_cpf', '_senha']



	def __init__(self, nome, sobrenome, cpf, senha):
		self._nome = nome
		self._sobrenome = sobrenome
		self._cpf = cpf
		self._senha = senha



	@property
	def nome(self):
		return self._nome


	@nome.setter
	def nome(self, nome):
		self._nome = nome



	@property
	def sobrenome(self):
		return self._sobrenome


	@sobrenome.setter
	def sobrenome(self, sobrenome):
		self._sobrenome = sobrenome



	@property
	def cpf(self):
		return self._cpf


	@cpf.setter
	def cpf(self, cpf):
		self._cpf = cpf



	@property
	def senha(self):
		return self._senha


	@senha.setter
	def senha(self, senha):
		self._senha = senha