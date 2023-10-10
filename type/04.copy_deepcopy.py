# 할당
x = [1, 2, 3, 4, 5]
y = x
y[2] = 100
print(x)
print(y)
print(id(x) == id(y))  # True

# 복사
x = [1, 2, 3, 4, 5]
y = x.copy()
y[2] = 100
print(x)
print(y)
print(id(x) == id(y))  # False

# 다차원 리스트 복사
import copy

x = [[1, 2, 3], [4, 5, 6]]
y = copy.deepcopy(x)
y[0][1] = 9
print(x)
print(y)
