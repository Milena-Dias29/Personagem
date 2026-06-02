import time
import random
import json

class personagem:
    def __init__(self, nome, nivel, habilidde=None, guilda=False):
        self.nome = nome
        self.guilda = guilda
        self.nivel = nivel
        self.habilidade = habilidde


    def entrar_guilda(self, nome_guilda):
        self.guilda = True
        print(f"{self.nome} entrou na guilda {nome_guilda}")

    def sair_guilda(self,):
        self.guilda = False
        print(f"{self.nome} saiu da guilda")

    def usar_habilidade(self):
        opçao=input("Deseja escolher uma habilidade ou usar uma aleatória?")
        if opçao == "escolher":
            print(f"{self.nome} tem essas habilidades disponiveis: {self.habilidade}")
            escolha = input("Qual habilidade vai usar?")
            if escolha in self.habilidade:
                time.sleep(1)
                print(f"{self.nome} usou {escolha}")
            else:
                time.sleep(1)
                print(f"{self.nome} não possui essa habilidade")

        elif opçao == "aleatória":
            print(f"{self.nome} está escolhendo uma habilidade...")
            time.sleep(2)
            habilidades_disponiveis = self.habilidade
            print(f"{self.nome} usou: {random.choice(habilidades_disponiveis)}")

    def subir_nivel(self, valor:int):
        self.nivel += valor
        print(f"{self.nome} subiu de nível. Nível atual:{self.nivel}")

    def salvar_dados(self):
        personagem = {
            "nome": self.nome,
            "nivel": self.nivel,
            "habilidade": self.habilidade,
            "guilda": self.guilda
        }
        with open('personagem.json', 'w') as arquivo:
            json.dump(personagem, arquivo)

    def carregar_dados(self):
        with open('personagem.json', 'r') as arquivo:
            personagem=json.load(arquivo)
            print(personagem)
        

    def __str__(self):  
        return f"{self.nome}, a/o personagem é nivel {self.nivel}, possui habilidade/s {self.habilidade},{"ta em uma guilda" if self.guilda==True else "não esta em uma guilda"}"
    
v