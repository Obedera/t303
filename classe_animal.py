class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono

    def comer(self):
        print('umm que bom')

class Gato(Animal):
    def __init__(self,nome,dono,raca):
        super().__init__(nome, dono)
        self.raca = raca
    
    def miar(self):
        print('miauuuuu')



class Cachorro(Animal):
    def latir(self):
        print('Au uuuuuu')

animal = Animal('Layla','Marcia')
cachorro = Cachorro('Costela','Isaque')
gato = Gato('ajato','Sua mãe','viragato')

print(gato.dono)
cachorro.latir()

