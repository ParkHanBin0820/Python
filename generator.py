def test():
    print("함수가 호출되었습니다")
    yield "test"

# 함수가 호출합니다
print("A 지점 통과")
print("B 지점 통과")
print(test())