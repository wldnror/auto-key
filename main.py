from gpiozero import InputDevice
import os
import time

# 3.3V 입력 감지 설정 (GPIO 26)
input_device = InputDevice(26, pull_up=False)  # 외부에서 3.3V 입력 감지

# 키보드 입력 에뮬레이트 함수
def emulate_keyboard():
    print("3.3V 입력이 감지되었습니다.")
    # 여기에 원하는 키보드 에뮬레이션 코드 삽입
    os.system('sudo bash -c "echo -ne \\"\\x0F\\x00\\x2E\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # Ctrl + Shift + Alt + Windows + '=' 키 누름
    time.sleep(0.1)
    os.system('sudo bash -c "echo -ne \\"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # 모든 키 뗌

print("코드가 시작됨")

# 이전 입력 상태 추적
previous_input = False

# 무한 루프로 코드 실행 유지
while True:
    # 현재 입력 상태
    current_input = input_device.is_active
    
    # 입력 상태 변화 감지: 이전에는 비활성 상태였으나 현재는 활성 상태인 경우
    if current_input and not previous_input:
        emulate_keyboard()
    
    # 현재 입력 상태를 이전 상태로 업데이트
    previous_input = current_input
    
    time.sleep(0.3)  # CPU 사용률을 줄이기 위한 잠시 대기
