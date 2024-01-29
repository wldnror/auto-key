=:: ; '=' 키를 눌렀을 때 실행
Run, "C:\file\ghost.mp4" ; ghost.mp4 파일 실행
Sleep, 1000 ; 파일이 실행되기를 기다림 (필요한 경우 시간 조정)
Send, {F11} ; 전체 화면 단축키 (미디어 플레이어에 따라 다를 수 있음)
Sleep, 500 ; 전체 화면 전환을 기다림
Loop, 100 ; 볼륨 증가 키를 여러 번 누름 (필요한 횟수에 따라 조정)
{
    Send, {Volume_Up} 
    Sleep, 100
}
return
