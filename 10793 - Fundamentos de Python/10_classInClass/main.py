from Pessoa import Pessoa



p1 = Pessoa("Gonçalo", "1234456", "email@sapo.pt")

p1.add_contato(1)

print(p1.__dict__())




"""

{
    'nome': 'Gonçalo', 
    'listaCts': [
        Contacto(telefone='1234456', emial='email@sapo.pt'),
         Contacto(telefone='telefone 1', emial='email 1')
    ]
} 


{
    'nome': 'nome',
     'listaCts': [
        {
        'telefone': '1234456', 
        'emial': 'email@sapo.pt'
        },
         {
        'telefone': 'telefone 1', 
        'emial': 'email 1'
        }
    ]
}
"""