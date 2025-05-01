import subprocess
import os
import re


def get_file_path():
    r1 = r"(Get-ItemProperty 'HKCU:\Control Panel\Desktop' TranscodedImageCache -ErrorAction Stop).TranscodedImageCache"
    r2 = r"[System.Text.Encoding]::Unicode.GetString({r1}) -replace '(.+)([A-Z]:[0-9a-zA-Z\\])+','$2'"
    # Выполнение PowerShell команды
    result = subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            r2.replace("{r1}", r1)
        ],
        capture_output=True,
        text=True,
        check=True
    )
    
    # Вывод сырого результата для отладки
    print(f"{result.stdout=}")
    
    # Применение регулярного выражения для извлечения пути к файлу
    # Ищем паттерн, соответствующий пути в Windows с любым расширением
    file_path_match = re.search(r'([A-Z]:[\\\/][^?]*\.[a-zA-Z0-9]+)', result.stdout)
    
    if file_path_match:
        file_path = file_path_match.group(1)
        file_path = os.path.normpath(file_path)
        print(f"{file_path=}")
        return file_path if os.path.exists(file_path) else None
    
    return None


def open_file_in_explorer(file_path):
    # Открытие файла в проводнике
    print(f"Открытие файла в проводнике: {file_path}")
    subprocess.Popen(f'explorer /select,"{file_path}"', shell=True)

def main():
    file_path = get_file_path()
    if file_path:
        open_file_in_explorer(file_path)
    else:
        print("Не удалось получить действительный путь к файлу.")


if __name__ == "__main__":
    main()
