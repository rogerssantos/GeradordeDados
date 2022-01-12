from mimesis import Person
from mimesis.builtins import BrazilSpecProvider
person = Person('pt')

br = BrazilSpecProvider()

print(br.cnpj(with_mask=False))

print(person.full_name())


cdEmpresa
nmEmpresa
dsEmail
nmEmpresaCurto
nuCnpj
nuInscricaoEstadual
dsLogradouro
dsComplemento
dsBairro
dsCep
dsCidade
dsEstado
dsPais
nuFone
nuFoneFax
nuLogradouro