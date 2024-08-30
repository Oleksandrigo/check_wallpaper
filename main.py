import subprocess
import os

def get_file_path():
    # PowerShell команды для получения пути к файлу
    ps_commands = [
        r"(Get-ItemProperty 'HKCU:\Control Panel\Desktop' TranscodedImageCache -ErrorAction Stop).TranscodedImageCache",
        r"[System.Text.Encoding]::Unicode.GetString({0}) -replace '(.+)([A-Z]:[0-9a-zA-Z\\])+','$2'"
    ]
    
    # Выполнение PowerShell команд
    result = subprocess.run(
        ['powershell.exe', "-NoProfile", "-ExecutionPolicy", "Bypass", 
         ps_commands[1].format(ps_commands[0])],
        capture_output=True, text=True, check=True
    )
    
    # Очистка и проверка результата
    file_path = ''.join(char for char in result.stdout if char.isprintable()).strip()
    return file_path if os.path.exists(file_path) else None

def open_file_in_explorer(file_path):
    # Открытие файла в проводнике
    subprocess.Popen(f'explorer /select,"{file_path}"')

def main():
    file_path = get_file_path()
    if file_path:
        open_file_in_explorer(file_path)
    else:
        print("Не удалось получить действительный путь к файлу.")

if __name__ == "__main__":
    main()