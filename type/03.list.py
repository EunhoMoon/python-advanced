# list methods

# 추가: append
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')

# 삽입: insert
fruits.insert(1, 'mango')

# 병합: extend
fruits2 = ['melon', 'watermelon']
fruits.extend(fruits2)
print(fruits)

# 삭제: pop
fruits.pop(1)
print(fruits)

# 삭제: remove
fruits.remove('banana')

# 삭제: del
del fruits[1]
print(fruits)

# 정렬: sort
numbers = [4, 2, 3, 1]
numbers.sort()
print(numbers)
# 역순 정렬: reverse

# enumerate
titles = ['아이언맨', '스파이더맨', '토르', '헐크']
for index, title in enumerate(titles, 1):  # 두번째 인자 = 인덱스 시작 번호
    print(index, title)

# list 내포
numbers = [i for i in range(5)]
print(numbers)

numbers2 = [100, 200, 300]
double_numbers = [i * 2 for i in numbers2]
print(double_numbers)

# 조건을 활용한 list 내포
numbers3 = [i for i in range(10) if i % 2 == 0]
print(numbers3)

numbers4 = [100, 200, 300, 400, 500]
double_numbers2 = [i * 2 for i in numbers4 if i >= 300]
print(double_numbers2)

# 실습
a = ["apple", "watch", "apollo", "star", "avocado"]
b = [i for i in a if i.startswith('a')]
print(b)

# 실습2: else 사용시 for문은 if문 뒤에 위치
c = ["오메가3", None, "비타민D", None, "비타민C"]
d = [i if i is not None else '' for i in c]
print(d)
