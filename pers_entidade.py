from entidade import Entidade

class Pers_entidade(Entidade):

    def tomar_dano(self, valor):
        if self.vida >= valor:
            self.morrer

        return self.vida -= valor

    def atacar(self, habilidade):
        print(f"{Entidade} possui habilidade de ")

    def curar(self,valor):
        if valor >= self.max_vida:
            self.vida = self.max_vida
        else:
            self.vida = valor





            