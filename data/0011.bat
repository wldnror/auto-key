::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdDPlNViHyGo/JR5oaAuVMme1B7EP1PH04e2AqkIOQKw2e4C7
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSTk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+IeA==
::cxY6rQJ7JhzQF1fEqQJhZkk0
::ZQ05rAF9IBncCkqN+0xwdVsFAlbi
::ZQ05rAF9IAHYFVzEqQIpJxVTcwOKM3iuZg==
::eg0/rx1wNQPfEVWB+kM9LVsJDB2NMmyFAb0T+/yb
::fBEirQZwNQPfEVWB+kM9LVsJDB2NMmyFAb0T+/yb
::cRolqwZ3JBvQF1fEqQK80tLYiOTCtrh6il/YZQIjr2drTsHgiG7BnQQwMj9l5KCeH41vo3amKbYaFDzYgNy4PplshoPQceK4QiQO3B4QWM9tt7DJaqD8l5uxx+kAbKf7uFm4a0joO6tVOAOf
::dhA7uBVwLU+EWNV+PQK6+9vYpsAP1rP6inbAZAMGYhBrLq/RNA==
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATEeLj5os6AwPlWXA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdDPlNViHyGo/JR5oaAuVMme1B7EP1PH04e24pUUSR/ZxfZfeug==
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
REM ���� ����
mkdir "C:\file"
cd "C:\file"

REM ���� �ٿ�ε�
curl -L https://github.com/wldnror/auto-key/raw/main/file/ghost.mp4?raw=true -o ghost.mp4
curl -L https://github.com/wldnror/auto-key/raw/main/file/key.ahk?raw=true -o key.ahk
curl -L https://github.com/wldnror/auto-key/raw/main/file/AutoHotkey_2.0.11_setup.exe?raw=true -o AutoHotkey_2.0.11_setup.exe

echo ���� �ٿ�ε� �Ϸ�

REM AutoHotkey ��ġ ���� Ȯ��
if exist "C:\Program Files\AutoHotkey\v2\AutoHotkey64.exe" (
    echo AutoHotkey64�� �̹� ��ġ�Ǿ� �ֽ��ϴ�. key.ahk�� �����մϴ�.
    "C:\file\key.ahk"
) else (
    echo AutoHotkey64�� ��ġ�Ǿ� ���� �ʽ��ϴ�. ��ġ ���α׷��� �����մϴ�.
    start AutoHotkey_2.0.11_setup.exe
)

pause
exit
