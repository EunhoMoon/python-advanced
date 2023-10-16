# 일급객체
# 1. 데이터 처럼 사용 가능
# 1-1. 변수에 할당 가능
def func(x, y):
    return x + y


add = func
print(add(3, 4))


# 1-2. 리스트(튜플, 딕셔너리)의 요소로 사용 가능
def mul(x, y):
    return x * y


def div(x, y):
    return x / y


calculator = [mul, div]
print(calculator[0](3, 4))


# 2. 매개변수로 전달 가능
def input_data():
    data = input("데이터를 입력하세요: ")
    return data


def start(func):
    print("입력한 데이터는", func())


start(input_data)


# 3. 반환값으로 사용 가능
def plus_ten(a):
    return a + 10


def func(x):
    return plus_ten(x)


print(func(3))
