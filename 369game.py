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

# 사용자 입력받아 1 부터 시작

# 다음 컴퓨터 진행

# 3 6 9에 숫자에 짝 인식하는 함수 생성

# 게임 진행 중 'e' 입력시 프로그램 종료
