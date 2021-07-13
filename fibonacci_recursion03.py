# 변수를 선언합니다.
counter = 0

# 함수를 선언합니다
def fibonacci(n):
    global counter
    counter += 1
    # 피보나치 수를 구합니다
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 함수를 호출합니다.
print(fibonacci(10))