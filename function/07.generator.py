# generator
# - iterator를 생성해주는 함수
# - 함수 안에 yield(생산) 키워드를 사용하면 generator가 된다.
# - 특징
#   1. 함수 안에 yield 키워드를 사용한다.
#   2. 제너레이터 표현식을 사용할 수 있다.
#   3. 메모리 사용이 효율적이다.
import sys


def season_generator(*args):
    for arg in args:
        yield arg


g = season_generator("spring", "summer", "fall", "winter")
print(g.__next__())


def func():
    print("첫번째 작업 중...")
    yield 1
    # return은 함수를 종료시키지만, yield는 함수를 종료시키지 않는다.

    print("두번째 작업 중...")
    yield 2

    print("세번째 작업 중...")
    yield 3


ge = func()
data = ge.__next__()
print(data)
print("======================")

# 제너레이터 표현식
double_generator = (i * 2 for i in range(1, 10))

for i in double_generator:
    print(i)

# 효율적인 메모리 사용
# 리스트 vs 제너레이터

list_data = [i * 3 for i in range(1, 10000 + 1)]
generator_data = (i * 3 for i in range(1, 10000 + 1))
print("list: ", sys.getsizeof(list_data))   # 87624
print("generator: ", sys.getsizeof(generator_data))  # 112
