from abc import *

class Item(metaclass=ABCMeta):  # 추상 클래스
    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다.")

    def discard(self):
        print(f"[{self.name}]을(를) 버렸습니다.")

    @abstractmethod
    def use(self):
        pass    # 추상 메서드


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def use(self):
        print(f"[{self.name}]을(를) 사용합니다. {self.damage}의 피해를 입혔습니다.")


class HealingItem(Item):
    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount

    def use(self):
        print(f"[{self.name}]을(를) 사용합니다. {self.recovery_amount}만큼 회복합니다.")


m16 = Weapon("M16", 110)
bandage = HealingItem("붕대", 20)

m16.use()
bandage.use()