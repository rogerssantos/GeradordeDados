from mimesis import Person, Address
from mimesis.builtins import BrazilSpecProvider

person = Person('pt-br')
endereco = Address('pt-br')
br = BrazilSpecProvider()

data = {}

class Empresa:
    def __init__(self, gerarNovo, qtEmpresa):

        #self.gerarNovo = gerarNovo

        #if True(gerarNovo):
        self.nmEmpresa = person.full_name()
        self.nmEmpresaCurto = person.full_name()
        self.nuFone = person.telephone(mask=False)
        self.nuFoneFax = person.telephone(mask=False)
        self.dsEmail = person.email()
        self.nuCnpj = br.cnpj(with_mask=False)
        self.dsCep = endereco.zip_code()
        self.dsCidade = endereco.city()
        self.dsEstado = endereco.state()
        self.nuLogradouro = endereco.street_number()
        self.dsLogradouro = endereco.street_name()
        self.dsPais = 'Brasil'

emp = Empresa(1, 2)

a = 1

row = {
       f'{emp.nmEmpresa=}'.split('=')[0].split('.')[1]: emp.nmEmpresa,
       f'{emp.nmEmpresaCurto=}'.split('=')[0].split('.')[1]: emp.nmEmpresaCurto,
       f'{emp.nuFone=}'.split('=')[0].split('.')[1]: emp.nuFone
}
data[a] = row

print(data)

#print(emp.dsCidade)

#cdEmpresa
#nuInscricaoEstadual
#dsComplemento
#dsBairro

#
#for a in range(1, 100):
#    row = {
#       'CDEMPRESA': 'empresa ' + str(a),
#       'CDREP': 'rep ' + str(a)
#      }
#    data[a] = row


f'{emp.nmEmpresa=}'.split('=')[0]

print((f'{emp.nmEmpresa=}'.split('=')[0]).split('.')[1])

