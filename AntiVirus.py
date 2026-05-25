import pyttsx3
import os
import time
import sys
import pyautogui
import ctypes
import subprocess
import winsound
import winreg
pyautogui.press('f11')
os.system('color 1f')  # 1 — синий фон, f — белый текст
time.sleep(1)
os.system('color 8')  # 1 — синий фон, f — белый текст
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


print("Booting Windows...")
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
    time.sleep(0.0)
    print(error)
    
time.sleep(0.9)
print("Memory section at address 0x0424* is locked!")
time.sleep(0.8)
print("Service UXCryptor started.")
time.sleep(0.7)
print("* Windows blocked!")

print('\a')
os.system('cls')

# Задаём частоту звука в герцах (Hz) и длительность в миллисекундах
frequency = 1000  # 1000 Гц
duration = 500    # 500 мс (0,5 секунды)
winsound.Beep(frequency, duration)
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
    print("        ,:::::::::::::::::::::::  ,    /  /        Dooo")
    print("        ;  ::::::   ::::::;;;:::   ,  /  /          Dooo")
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
os.system('color 4f')  # 4 — красный фон, f — белый текст
time.sleep(2)  # Пауза на 2 секунд
os.system('cls')
os.system('color 1f')  # 1 — синий фон, f — белый текст
print('UCrytor Locked you pc and SvRh')

# Инициализация движка
engine = pyttsx3.init()

# Текст для озвучивания
text = "UCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRhUCrytor Locked you pc and SvRh"

# Произносим текст
engine.say(text)
























# Бесконечно запрашиваем пароль, пока не введён верный.
# После правильного пароля — выход из программы.

PASSWORD = "UXCrytor1223"  # в реальных приложениях хранить только хэш!
os.system('color 1f')  # 1 — синий фон, f — белый текст
while True:
    user_input = input("ну давай побробуй: ")
    os.system('color 1f')  # 1 — синий фон, f — белый текст
    if user_input == PASSWORD:
        os.system('color 1f')  # 1 — синий фон, f — белый текст
        print('notSvVirusUCrytor')
        print("да йоу ну зачем лан.")
        break  # завершение программы
    else:
         # Задаём частоту звука в герцах (Hz) и длительность в миллисекундах
         frequency = 1000  # 1000 Гц
         duration = 500    # 500 мс (0,5 секунды)
         winsound.Beep(frequency, duration)
         print("ебать лох, давай ещё раз)")
os.system('color 1f')  # 1 — синий фон, f — белый текст