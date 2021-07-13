# try except 구문으로 예외를 처리합니다
try:
    # 숫자로 변환합니다
    PI = 3.14
    r = float(input("정수 입력> "))
    print("원의 반지름: {}".format(r))
    print("원의 둘레: {}".format(PI * 2 *r))
    print("원의 넓이: {}".format(PI * r * r))
except:
    print("무언가 잘못되엇습니다")