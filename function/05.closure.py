# 내부 함수
def outer(name):
    def inner():
        print(name, "님 안녕하세요!")
    return inner


func = outer("Janek")  # 외부 함수 호출, 내부 함수 반환(func = inner())
# func()  # 내부 함수 호출
# 외부 함수가 종료되었음에도 불구하고 변수로 선언된 내부 함수는 종료된 외부 함수의 지역변수 사용

# 클로저: 함수가 종료되었어도 자원을 사용할 수 있는 함수
# 클로저가 될 수 있는 조건
# 1. 내부 함수여야 한다.
# 2. 외부 함수의 변수를 참조해야 한다.
# 3. 외부 함수가 내부 함수를 반환해야 한다.
# - 따라서 inner()는 클로저


def greeting(name, age, gender):
    def inner():
        print(name, "님 안녕하세요!")
        print("나이: ", age)
    return inner


closure = greeting("Janek", 30, "남자")
closure()  # Janek 님 안녕하세요!

print(type(closure.__closure__))    # <class 'tuple'>

for i in closure.__closure__:
    print(i.cell_contents)  # Janek 30, 내부 함수의 지역변수가 출력됨

# 전역변수를 사용해서 대체가 가능하지만, 전역변수 사용은 최소화 하는 것이 좋다.
#  - 네이밍, 스코프 문제 발생 가능성
# class를 이용하면 클로저를 대체할 수 있다.
