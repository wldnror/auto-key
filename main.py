from gpiozero import Button
import os
import time

# 버튼 설정 (GPIO 26)
button = Button(26, bounce_time=0.3)  # 0.2초의 디바운싱 시간 적용

# 키보드 입력 에뮬레이트 함수
def emulate_keyboard():
    print("버튼이 눌렸습니다.")
    # Shift + '=' 키 입력
    # "Ctrl" + "Shift" + "Alt" + "+" 를 누르는 코드
    os.system('sudo bash -c "echo -ne \\"\\x1E\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')
    time.sleep(0.1)
    os.system('sudo bash -c "echo -ne \\"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # 모든 키 뗌

# 버튼 눌림 이벤트
button.when_pressed = emulate_keyboard
# 버튼 해제 이벤트 (필요 없는 경우 비워두거나 None 할당)
button.when_released = None

print("코드가 시작됨")

# 무한 루프로 코드 실행 유지
while True:
    time.sleep(0.3)  # CPU 사용률을 줄이기 위한 잠시 대기
