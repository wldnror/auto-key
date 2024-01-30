from gpiozero import Button
import os
import time

# 버튼 설정 (GPIO 26)
button = Button(26)

# 키보드 입력 에뮬레이트 함수
def emulate_keyboard():
    # Shift + '=' 키 입력
    os.system('echo -ne "\x02\x38" > /dev/hidg0')  # Shift 키 누름
    os.system('echo -ne "\x00\x2e" > /dev/hidg0')  # '=' 키 누름
    time.sleep(0.1)
    os.system('echo -ne "\x00\x00" > /dev/hidg0')  # 모든 키 뗌

# 무한 루프로 코드 실행 유지
while True:
    button.wait_for_press()  # 버튼 눌림을 기다림
    emulate_keyboard()
