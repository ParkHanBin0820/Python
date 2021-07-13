# 정수
output_a = "{:}" .format(52)

# 특정 칸에 출력하기
output_b = "{:5}".format(52)          #5칸
output_c = "{:10}".format(52)         #10칸

# 빈칸을 0으로 채우기                    
output_d = "{:05}".format(52)         #양수
output_e = "{:05}".format(52)        #음수

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)