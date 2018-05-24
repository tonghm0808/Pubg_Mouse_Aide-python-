@echo off
pyinstaller -F -w aider.py -i icon.ico --upx-dir upx307w
rmdir /q /s "build"
pause