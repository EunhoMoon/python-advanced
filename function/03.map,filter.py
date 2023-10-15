# map
# map(function, iterable)
print(list(map(int, ['3', '4', '5', '6'])))

# lambda 사용
items = [' 마우스 ', '   키보드 ', ' 모니터    ']
items = list(map(lambda x: x.strip(), items))
print(items)


# filter
# filter(function, iterable)
numbers = [-3, -2, -1, 0, 1, 2, 3]
numbers = list(filter(lambda x: x < 0, numbers))
print(numbers)

animals = ['cat', 'dog', 'lion', 'tiger', 'rabbit']
animals = list(filter(lambda x: len(x) > 3, animals))
print(animals)
