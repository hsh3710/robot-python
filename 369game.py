import time

# 369게임 시작
def play_369_game():
    print("369 게임을 시작합니다!")
    print("3, 6, 9가 들어간 숫자는 '짝'을 입력하세요.")
    print("게임을 종료하려면 'e'를 입력하세요.")

# 369를 포함하는지 판정 함수
def contains_369(number):
    return any(n_list in str(number) for n_list in ['3', '6', '9'])

# 정답지 함수
def get_correct_response(number):
    if contains_369(number):
        return "짝"
    else:
        return str(number)
    
# 게임 실행
play_369_game()

# 사용자 입력받아 1 부터 시작
current_number = 1
    
while True:
    # 사용자 차례
    correct_answer = get_correct_response(current_number)
    user_input = input("당신의 차례: ")
    
    #'e'입력 시 게임 종료
    if user_input.lower() == 'e':
        print("게임을 종료합니다.")
        break

    # 오답 시 게임 종료    
    if user_input != correct_answer:
        print(f"틀렸습니다! 정답은 {correct_answer}입니다.")
        break
        
    current_number += 1

# 다음 컴퓨터 진행
    computer_answer = get_correct_response(current_number)
    print(f"컴퓨터: {computer_answer}")
    time.sleep(1)  # 컴퓨터의 응답을 보기 쉽게 약간의 딜레이를 줍니다
    
    current_number += 1

# 게임 실행
if __name__ == "__main__":
    play_369_game()
