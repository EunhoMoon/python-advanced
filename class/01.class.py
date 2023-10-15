class Unit:
    # 클래스 속성: 모든 객체가 공유하는 속성
    count = 0

    def __init__(self, name, hp, shield, damage):
        # 인스턴스 속성: 객체마다 다른 값을 가지는 속성
        self.name = name
        # self: 객체 자신을 가리키는 예약어
        self.__hp = hp
        # __(property): 비공개 속성, 네임 맹글림을 통해 접근 가능
        self.shield = shield
        self.damage = damage
        Unit.count += 1
        print(f"[{self.name}](이)가 생성되었습니다.")

    # 매직 메서드(magic method): 특정 상황에서 자동으로 호출되는 메서드(__로 시작, __로 끝남, __init__, __str__)
    def __str__(self):
        return f"[{self.name}] 체력 : {self.__hp} / 방어막 : {self.shield} / 공격력 : {self.damage}"

    # 인스턴스 메서드(instance method): 인스턴스 속성에 접근할 수 있는 메서드
    def hit(self, damage):
        if self.shield > 0:
            self.shield -= damage
            if self.shield < 0:
                self.__hp += self.shield
                self.shield = 0
        else:
            self.__hp -= damage
            if self.__hp < 0:
                self.__hp = 0

    # 클래스 메서드(class method): 클래스 속성에 접근할 수 있는 메서드
    @classmethod
    def print_count(cls):
        print(f"현재까지 {cls.count}개의 유닛이 생성되었습니다.")

    # 정적 메서드(static method): 클래스 속성, 인스턴스 유무와 관계없이 독립적으로 사용
    @staticmethod
    def add(x, y):
        return x + y


probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)

print(probe)
print(zealot)
print(dragoon)

probe.hit(16)
print(probe)

Unit.print_count()
