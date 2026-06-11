import time
import json
import random

class inimigo:
    def __init__(self, nome, nivel, habilidade=None):
        self.nome = nome
        self.nivel = nivel
        self.habilidade = habilidade

    def habilidade(self):
        print(f"{self.nome} possui essas habilidades: {self.habilidade}")
        print(f"{self.nome} esta escolhendo uma habilidade...")
        time.sleep(1)
        habilidades_disponiveis = self.habilidade
        print(f"{self.nome} atacou usando: {random.choice(habilidades_disponiveis)}")

    def salvar_dados(self):
        personagem = {
        "nome": self.nome,
        "habilidade": self.habilidade,
        "nivel": self.nivel
        }

        with open ('personagem.json', 'w') as arquivo:
            json.dump(personagem,arquivo)
        
    def carregar_dados(self):
        with open ('personagem.json', 'r') as arquivo:
            personagem=json.load(arquivo)
            print(personagem)

    def __str__(self):
        return(f"{self.nome}, é um inimigo nivel {self.nivel}, que possui as habilidades {self.habilidade}")

Mox = inimigo("Mox", 1, ["criar objetos","desaparecer","vento"])
Mox.salvar_dados()
Mox.carregar_dados()
print(Mox)
Mox.usar_habilidade()
Mox.subir_nivel(1)
