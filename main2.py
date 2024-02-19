from gpiozero import Button
import os
import time

# 버튼 설정 (GPIO 26)
button = Button(26, bounce_time=0.3)

# 전원 버튼 에뮬레이트 함수
def emulate_power_button():
    print("전원 버튼 에뮬레이트")
    # 전원 버튼 스캔 코드 전송 (가상의 스캔 코드, 실제 코드로 교체 필요)
    os.system('sudo bash -c "echo -ne \\"\\xE2\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # 전원 버튼 누름
    time.sleep(0.1)
    os.system('sudo bash -c "echo -ne \\"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # 모든 키 뗌

# 버튼 눌림 상태를 추적하는 변수
button_pressed = False

def button_pressed_callback():
    global button_pressed
    if not button_pressed:
        emulate_power_button()
        button_pressed = True

def button_released_callback():
    global button_pressed
    if button_pressed:
        print("버튼이 해제되었습니다.")
    button_pressed = False

# 이벤트 할당
button.when_pressed = button_pressed_callback
button.when_released = button_released_callback

print("코드가 시작됨")

while True:
    time.sleep(0.3)
