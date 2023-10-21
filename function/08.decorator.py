# 데코레이터
# - 함수의 앞,뒤로 부가적인 기능을 넣어주고 싶을 때 사용(aop)

# 데코레이터 생성
def logger(func):
    def wrapper(arg):
        print("함수 시작")
        func(arg)
        print("함수 종료")
    return wrapper


@logger
def print_hello(name):
    print(f"hello {name}")


@logger
def print_goodbye(name):
    print(f"goodbye {name}")


print_hello("janek")
print_goodbye("janek")
