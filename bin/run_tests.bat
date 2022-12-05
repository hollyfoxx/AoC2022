@echo off 

set test_id=%1
if not "%test_id%" == "" (pytest .\test.py -s -vv -k %test_id%)
if "%test_id%" == "" (pytest .\test.py -s -vv)