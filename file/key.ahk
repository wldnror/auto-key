+=:: ; Shift와 '=' 키를 동시에 눌렀을 때 실행
SoundSet, 50 ; 시스템 볼륨을 50%로 설정
SoundSet, 0, , Mute ; 시스템 음소거 해제
Run, "C:\Program Files\VideoLAN\VLC\vlc.exe" --fullscreen --volume=128 "C:\file\ghost.mp4" ; 전체 화면으로 영상 재생 및 VLC 내부 볼륨 50%로 설정
return
