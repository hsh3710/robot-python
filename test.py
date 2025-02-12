import random
import time

def contains_369(number):
    return any(digit in str(number) for digit in ['3', '6', '9'])

def get_correct_response(number):
    if contains_369(number):
        return "짝"
    return str(number)

def play_369_game():
    print("369 게임을 시작합니다!")
    print("3, 6, 9가 들어간 숫자는 '짝'을 입력하세요.")
    print("게임을 종료하려면 'q'를 입력하세요.")
    
    current_number = 1
    
    while True:
        # 사용자 차례
        print(f"\n현재 숫자: {current_number}")
        correct_answer = get_correct_response(current_number)
        user_input = input("당신의 차례: ")
        
        if user_input.lower() == 'q':
            print("게임을 종료합니다.")
            break
            
        if user_input != correct_answer:
            print(f"틀렸습니다! 정답은 {correct_answer}입니다.")
            break
            
        current_number += 1
        
        # 컴퓨터 차례
        computer_answer = get_correct_response(current_number)
        print(f"컴퓨터: {computer_answer}")
        time.sleep(1)  # 컴퓨터의 응답을 보기 쉽게 약간의 딜레이를 줍니다
        
        current_number += 1

if __name__ == "__main__":
    play_369_game()
