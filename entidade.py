from abc import ABC, abstractmethod

class Entidade(ABC):
    
    @abstractmethod
    def tomar_dano():
        pass

    @abstractmethod
    def atacar():
        pass

    @abstractmethod
    def curar():
        pass

    @abstractmethod
    def morrer():
        pass

    @abstractmethod
    def usar_habilidade():
        pass