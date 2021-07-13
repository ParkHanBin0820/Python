test = ['요소A', '요소B', '요소C']
test_e = enumerate(test)

print("# 단순 출력")
print(test)
print()

print("# enumerate() 함수 적용 출력")
print(test_e)
print()

print("# list() 함수로 강제 변환 출력")
print(list(test_e))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(test):
    print("{}번째 요소는 {}입니다.".format(i, value))