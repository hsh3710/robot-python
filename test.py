import random

# 3 6 9 게임
# 사용자가 숫자를 입력하면 3 6 9 게임을 하는 프로그램
# 3 6 9 게임은 3의 배수를 외치면 박수를 치는 게임

input_number = int(input("숫자를 입력하세요: "))    

for i in range(1, input_number + 1):
    if i % 3 == 0:
        print("박수")
    else:
        print(i)

