from gpiozero import Button
import os
import time

# GPIO 26에 스위치 연결 설정
button = Button(26)

# 버튼이 눌린 상태를 추적하는 플래그
button_pressed = False

def button_released():
    global button_pressed
    button_pressed = False  # 버튼이 릴리즈 되면 플래그를 False로 설정

# 키보드 입력 에뮬레이트 함수
def check_button():
    global button_pressed
    if button.is_pressed and not button_pressed:
        button_pressed = True  # 버튼이 눌렸음을 표시
        emulate_keyboard()
        button.when_released = button_released  # 버튼 릴리즈 이벤트 핸들러 설정

def emulate_keyboard():
    print("버튼 입력이 감지되었습니다.")
    # 여기에 원하는 키보드 에뮬레이션 코드 삽입
    os.system('sudo bash -c "echo -ne \\"\\x0F\\x00\\x2E\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # Ctrl + Shift + Alt + Windows + '=' 키 누름
    time.sleep(0.1)
    os.system('sudo bash -c "echo -ne \\"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # 모든 키 뗌

print("코드가 시작됨")

# 메인 루프
while True:
    check_button()  # 버튼 상태 확인 및 처리
    time.sleep(0.1)  # CPU 사용률을 줄이기 위한 잠시 대기
