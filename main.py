# from gpiozero import Button
# import os
# import time

# # 버튼 설정 (GPIO 26)
# button = Button(26, bounce_time=0.3)  # 0.2초의 디바운싱 시간 적용

# # 키보드 입력 에뮬레이트 함수
# def emulate_keyboard():
#     print("버튼이 눌렸습니다.")
#     # Shift + '=' 키 입력
#     # "Ctrl" + "Shift" + "Alt" + "=" 를 누르는 코드
#     os.system('sudo bash -c "echo -ne \\"\\x0F\\x00\\x2E\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # Ctrl + Shift + Alt + Windows + '=' 키 누름
#     time.sleep(0.1)
#     os.system('sudo bash -c "echo -ne \\"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # 모든 키 뗌

# # 버튼 눌림 이벤트
# button.when_pressed = emulate_keyboard
# # 버튼 해제 이벤트 (필요 없는 경우 비워두거나 None 할당)
# button.when_released = None

# print("코드가 시작됨")

# # 무한 루프로 코드 실행 유지
# while True:
#     time.sleep(0.3)  # CPU 사용률을 줄이기 위한 잠시 대기

from gpiozero import InputDevice
import os
import time

# 3.3V 입력 감지 설정 (GPIO 26)
input_device = InputDevice(26, pull_up=False)  # pull_up=False로 설정하여 외부에서 3.3V 입력 감지

# 키보드 입력 에뮬레이트 함수
def emulate_keyboard():
    print("3.3V 입력이 감지되었습니다.")
    # 여기에 원하는 키보드 에뮬레이션 코드 삽입
    os.system('sudo bash -c "echo -ne \\"\\x0F\\x00\\x2E\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # Ctrl + Shift + Alt + Windows + '=' 키 누름
    time.sleep(0.1)
    os.system('sudo bash -c "echo -ne \\"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # 모든 키 뗌

print("코드가 시작됨")

# 무한 루프로 코드 실행 유지
while True:
    if input_device.is_active:
        emulate_keyboard()
    time.sleep(0.3)  # CPU 사용률을 줄이기 위한 잠시 대기

# from gpiozero import Button
# import os
# import time

# # 버튼 설정 (GPIO 26)
# button = Button(26, bounce_time=0.3)

# # 키보드 입력 에뮬레이트 함수
# def emulate_keyboard():
#     print("버튼이 눌렸습니다.")
#     # Shift + '=' 키 입력
#     os.system('sudo bash -c "echo -ne \\"\\x0F\\x00\\x2E\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # Ctrl + Shift + Alt + Windows + '=' 키 누름
#     time.sleep(0.1)
#     os.system('sudo bash -c "echo -ne \\"\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\" > /dev/hidg0"')  # 모든 키 뗌

# # 버튼 눌림 상태를 추적하는 변수
# button_pressed = False

# def button_pressed_callback():
#     global button_pressed
#     if not button_pressed:  # 버튼이 이미 눌려있지 않은 경우에만 실행
#         emulate_keyboard()
#         button_pressed = True  # 버튼이 눌렸음을 표시

# def button_released_callback():
#     global button_pressed
#     button_pressed = False  # 버튼이 해제되었음을 표시

# # 이벤트 할당
# button.when_pressed = button_pressed_callback
# button.when_released = button_released_callback

# print("코드가 시작됨")

# # 무한 루프로 코드 실행 유지
# while True:
#     time.sleep(0.3)  # CPU 사용률을 줄이기 위한 잠시 대기
