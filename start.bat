@echo off
:: Установка кодировки UTF-8
chcp 65001 > nul

:: Определение пути к виртуальному окружению
set VENV_PATH=%~dp0\.venv

:: Активация виртуального окружения
call %VENV_PATH%\Scripts\activate.bat

:: Запуск Python-скрипта
python main.py

:: Деактивация виртуального окружения
deactivate

:: Пауза для просмотра вывода (опционально)
pause
