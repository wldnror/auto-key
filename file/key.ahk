; Shift, Alt, Left Windows Key, Ctrl, "=" 키가 동시에 눌렸을 때 실행
^+#!=:: ; Ctrl(^), Shift(+), Alt(!), Left Windows Key(#), "="(=) 키 조합
SoundSet, 100 ; 시스템 볼륨을 100%로 설정
SoundSet, 0, , Mute ; 시스템 음소거 해제
Run, "C:\Program Files\VideoLAN\VLC\vlc.exe" --no-video-title-show --no-qt-fs-controller --fullscreen --volume=128 "C:\file\ghost.mp4" ; 전체 화면으로 영상 재생 및 VLC 내부 볼륨 50%로 설정
return
