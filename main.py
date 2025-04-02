from abc import abstractmethod


class Figther():
    pass

class Monster():
    pass


class Weapon(ABC):
    @abstractmethod
    def atach(self):
        print('Боец наносит удар')

class Sword(Weapon):
    def atach(self):
        print('Боец наносит удар мечом')

class Bow(Weapon):
    def atach(self):
        print('Боец наносит стреляет из лука')