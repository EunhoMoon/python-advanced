# f-string
name = 'Janek'
duration = 7
message_format = f'{name}님 수강기간이 {duration}일 남았습니다.'

print(message_format)

# format 메서드
a = 'Hello {0} {1} {2}'.format('apple', 'pineapple', 'pen')
print(a)

# index 생략 가능
b = 'Hello {} {} {}'.format('apple', 'pineapple', 'pen')
print(b)
