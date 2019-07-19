def imprimir_lista(v1, v2, v3):
    return print(f'{v1} {v2} {v3}')

vv0 = 0
vv1 = 1
vv2 = 2

imprimir_lista(vv0,vv1,vv2)

def lista_de_compras(pessoa,*args):
    print(f'Lista de compras de {pessoa}:')
    for item in args:
        print(item)
    print('')

lista_de_compras('João', 'miojo', 'pão')
lista_de_compras('Obede', 'Pão de queijo', 'Bife', 'Batata')
lista_de_compras('Maria','pizza')

def lista_de_compras_dic(**kwargs):
    fruta = kwargs.get('fruta') #procura se tem uma chave fruta
    if fruta is not None:
        print(f'Na lista de compras há uma fruta: {fruta}')
    print(f'{kwargs}')

lista_de_compras_dic(fruta='banana', massas='nhoque', verdura='alface')
lista_de_compras_dic(bebida='vinho', sorvete='flocos')





