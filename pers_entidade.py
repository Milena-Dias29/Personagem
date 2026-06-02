from entidade import Entidade

class Pers_entidade(Entidade):

    def tomar_dano(self, valor):
        self.vida -= valor
        print(f"{self.nome} tomou {valor} de dano!")
        if self.vida <= 0:
            self.morrer()

        self.vida -= valor

    def atacar(self, habilidade):
        print(f"{self.nome} usou a habilidade {habilidade}!")

    def curar(self,valor):
        if valor >= self.max_vida:
            self.vida = self.max_vida
        else:
            self.vida = valor

    def morrer(self):
        print(f"{self.nome} morreu!")

    def usar_habilidade(self,habilidade):
        print(f"{self.nome} possui essas habilidades: {habilidade}")