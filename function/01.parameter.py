# 위치 매개변수
def my_func(a, b):
    print(a, b)


my_func("a", "b")


# 기본 매개변수: 기본값을 가지는 매개변수
def post_info(title, content="내용 없음"):
    print("제목: ", title)
    print("내용: ", content)


post_info("안녕하세요")


# 키워드 매개변수: 매개변수 이름을 지정하여 전달, 순서를 지키지 않아도 된다.
def post_info(title, content):
    print("제목: ", title)
    print("내용: ", content)


post_info(content="안녕하세요.", title="가입인사")


# 가변 매개변수: 매개변수의 개수가 정해지지 않은 경우, *를 붙여서 선언하며, 튜플 형태로 받는다.
def print_fruits(*fruits):
    print(fruits)


print_fruits('apple', 'banana', 'cherry')


# 가변 키워드 매개변수: 매개변수의 개수가 정해지지 않은 경우, **를 붙여서 선언하며, 딕셔너리 형태로 받는다.
def comment_info(**comments):
    for key, value in comments.items():
        print(key, value)


comment_info(a="첫번째 댓글", b="두번째 댓글", c="세번째 댓글")


# 매개변수 작성 순서: 위치 매개변수 -> 기본 매개변수 -> 가변 매개변수 -> 가변 키워드 매개변수
def post_info(title, content, *tags):
    print("제목: ", title)
    print("내용: ", content)
    print(tags)
