from inimigo import Inimigo
from personagem import Personagem

class Batalha():
    def __init__(self, personagem: 'Personagem',inimigo):
        self.personagem = personagem
        self.inimigo = inimigo
    
    def definir_inicio(self):
        if self.personagem.rolar_iniciativa(20) > self.inimigo.rolar_iniciativa(20):
            self.atacante = self.personagem
            self.defensor = self.inimigo
            print(f"Primeiro turno: {self.atacante}|Segundo turno: {self.defensor}")
            return self.atacante, self.defensor
        else:
            self.atacante = self.inimigo
            self.defensor = self.personagem
            print(f"Primeiro turno: {self.atacante}|Segundo turno: {self.defensor}")
            return self.atacante, self.defensor
        
    def turno_jogada(self):
        print("Turno do Jogador")
        print("\n1-Atacar \n2- Curar \n3-Usar Habilidade \n4-sair")
        e = input("Escolha uma ação: ")

        if e == "1":
            self.personagem.atacar(self.inimigo, self.personagem.dano)
            self.turno_inimigo()

        elif e == "2":
            self.personagem.curar(5)
            self.turno_inimigo()
        
        elif e == "4":
            print("passou")
            self.turno_inimigo()

        else:
            print("opção invalida")
            self.turno_inimigo()

    def turno_inimigo(self):
        print("Turno do Inimigo")
        self.inimigo.atacar(self.personagem, self.inimigo.dano)
        self.turno_jogador()

    def turno(self):
        while self.personagem.vida > 0 or self.inimigo.vida > 0:
            if self.atacante is Personagem:
                self.turno_jogador()

            else:
                self.turno_inimigo()

class habilidade:
    def curar():
        
        