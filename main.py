from gpiozero import Button
import os
import time

# 버튼 설정 (GPIO 26)
button = Button(26, bounce_time=0.3)

# 키보드 입력 에뮬레이트 함수
def emulate_keyboard():
    print("버튼이 눌렸습니다.")
    # Shift + '=' 키 입력
    os.system('sudo bash -c "echo -ne \\"\\x0F\\x00\\x2E\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # Ctrl + Shift + Alt + Windows + '=' 키 누름
    time.sleep(0.1)
    os.system('sudo bash -c "echo -ne \\"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # 모든 키 뗌

# 버튼 눌림 상태를 추적하는 변수
button_pressed = False

def button_pressed_callback():
    global button_pressed
    if not button_pressed:  # 버튼이 이미 눌려있지 않은 경우에만 실행
        emulate_keyboard()
        button_pressed = True  # 버튼이 눌렸음을 표시

def button_released_callback():
    global button_pressed
    if button_pressed:  # 버튼이 눌려있는 상태에서 해제되는 경우에만 실행
        print("버튼이 해제되었습니다.")  # 버튼 해제 시 출력
    button_pressed = False  # 버튼이 해제되었음을 표시

# 이벤트 할당 (이 부분은 사용하는 라이브러리 또는 프레임워크에 따라 달라질 수 있습니다.)
button.when_pressed = button_pressed_callback
button.when_released = button_released_callback

print("코드가 시작됨")

# 무한 루프로 코드 실행 유지
while True:
    time.sleep(0.3)  # CPU 사용률을 줄이기 위한 잠시 대기
