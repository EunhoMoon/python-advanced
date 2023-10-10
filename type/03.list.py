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
for index, title in enumerate(titles, 1): # 두번째 인자 = 인덱스 시작 번호
    print(index, title)
