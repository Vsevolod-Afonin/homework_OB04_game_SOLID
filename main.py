from abc import abstractmethod, ABC


class Weapon(ABC):
    @abstractmethod
    def atach(self):
        print('Боец наносит удар')

class Sword(Weapon):
    def atach(self):
        print('Боец наносит удар мечом')

class Bow(Weapon):
    def atach(self):
        print('Боец стреляет из лука')


class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f'Боец сменил оружие')

    def fight(self):
        self.weapon.atach()
        print('Монстр побеждён!')


class Monster():
    pass


sword = Sword()
bow = Bow()

fighter = Fighter(bow)

fighter.fight()

fighter.change_weapon(sword)
fighter.fight()