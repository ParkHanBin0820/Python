list_a = ["요소A", "요소B", "요소C"]
list_a_enumerate = enumerate(list_a)

print("# 단순 출력")
print("['요소A', '요소B', '요소C']")
print()

print("# enumerate() 함수 적용 출력")
print(list_a_enumerate)
print()

print("# list() 함수로 강제 변환 출력")
print(list(list_a_enumerate))
print()

list_a_enumerate = list(enumerate(list_a))
print("# 반복문과 조합하기")
for i, a in list_a_enumerate:
    print("{}번째 요소는 {}입니다.".format(i, list_a))