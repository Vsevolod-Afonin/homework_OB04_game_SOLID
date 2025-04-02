from abc import abstractmethod, ABC





class Weapon(ABC):
    @abstractmethod
    def atach(self):
        print('Боец наносит удар')

class Sword(Weapon):
    def atach(self):
        print('Боец выбирает меч.')
        print('Боец наносит удар мечом')
        print('Монстр побеждён')

class Bow(Weapon):
    def atach(self):
        print('Боец выбирает лук.')
        print('Боец наносит стреляет из лука')
        print('Монстр побеждён')

class Figther():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self):
        print(f'Боец сменил оружие на {self.weapon}')

class Monster():
    pass