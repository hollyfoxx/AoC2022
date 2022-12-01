@echo off 

set test_id=%1
if not "%test_id%" == "" (python3 -m pytest .\test.py -s -vv -k %test_id%)
if "%test_id%" == "" (python3 -m pytest .\test.py -s -vv)