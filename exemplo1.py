import json

dicionario1 = {'codigo':123, 'nome':'Pedro Crispim', 'idade':18, 'altura':1.90, 'notas':[9,10,11,12]}

dicionario2 = {'codigo':432, 'nome':'leticiã', 'idade':18, 'altura':1.60, 'notas':[10,11,12,92,2,]}

lista = [dicionario1,dicionario2]

with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(lista, arquivo, indent=4, sort_keys=True, ensure_ascii=False)