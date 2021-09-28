from conta import Conta
from cliente import Cliente



cl1 = Cliente('Ayanami', 'Rei', '00')
cl2 = Cliente('Misato', 'Katsuragi', '15')
cl3 = Cliente('Asuka', 'Langley', '02')


co1 = Conta(1, cl1, 0, 500)
co2 = Conta(2, cl2, 200, 500)
co3 = Conta(3, cl3, 500, 1000)


co1.deposita(100)
co1.saca(50)


co1.saca(150)
co1.extrato()


print('\n_____________________________________________________________________________________________________________________________________________________')
co2.transfere(co1, 100)
co2.transfere(co1, 200)


co1.extrato()
co2.extrato()


print('\nTotal de contas:\n{}'.format(Conta.totalContas()))