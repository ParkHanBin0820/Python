# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= now.month <= 5:
    print("현재는 봄입니다")

elif 6 <= now.month <= 8:
    print("현재는 여름입니다")

elif 9 <= now.month <= 9:
    print("현재는 가을입니다")

else:
    print("현재는 겨울입니다")