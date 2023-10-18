# 1. 이터러블 객체(iterable object)
# 문자열, 리스트, 튜플, 딕셔너리, range 객체
for i in "123":
    print(i)

for i in [10, 20, 30]:
    print(i)

print(type([10, 20, 30].__iter__))  # <class 'method-wrapper'>
iter_obj = [10, 20, 30].__iter__()

# print(dir(iter_obj))
print(iter_obj.__next__())  # 10
print(iter_obj.__next__())  # 20


class Seasons:
    # 이터레이터 생성 방법: __iter__()와 __next__()를 모두 구현
    def __init__(self):
        self.seasons_list = ["spring", "summer", "fall", "winter"]
        self.index = 0
        self.max_num = 4

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.max_num:
            current_index = self.index
            self.index += 1
            return self.seasons_list[current_index]
        else:
            raise StopIteration


# for i in Seasons():
#     print(i)

seasons_iter = Seasons().__iter__()
print(seasons_iter.__next__())  # spring
print(seasons_iter.__next__())  # summer
print(seasons_iter.__next__())  # fall
print(seasons_iter.__next__())  # winter
print(seasons_iter.__next__())  # StopIteration
