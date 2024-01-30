import os
import time

# 'a' 키를 누르는 HID 리포트 전송
time.sleep(3)
os.system('echo -ne "\\x00\\x00\\x04\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0')  # 'a' 키 누름
time.sleep(11.1)
os.system('echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0')  # 모든 키 뗌
