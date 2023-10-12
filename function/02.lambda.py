# 기존 함수
def minus_one(a):
    return a - 1


# 람다 함수
lambda a: a - 1

# 람다 함수 사용
print((lambda a: a - 1)(10))
minus_one_2 = lambda a: a - 1
print(minus_one_2(10))


# 람다 함수에서 if문 사용
# 기존 함수
def is_positive_number(a):
    if a > 0:
        return True
    else:
        return False


# 람다 함수
lambda a: True if a > 0 else False
