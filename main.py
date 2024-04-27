import subprocess

r1 = r"(Get-ItemProperty 'HKCU:\Control Panel\Desktop' TranscodedImageCache -ErrorAction Stop).TranscodedImageCache"
r2 = r"[System.Text.Encoding]::Unicode.GetString({r1}) -replace '(.+)([A-Z]:[0-9a-zA-Z\\])+','$2'"
file_name = subprocess.run(
    [
        'powershell.exe',
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        r2.replace("{r1}", r1)
    ],
    capture_output=True,
    text=True).stdout

res = ''.join(i for i in file_name if i.isprintable())

subprocess.Popen(r'explorer /select,{res}'.replace("{res}", res))
