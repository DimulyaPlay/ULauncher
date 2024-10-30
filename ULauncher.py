import subprocess
import os
import sys

#  pyinstaller.exe --onefile --windowed .\ULauncher.py


def get_launcher_directory():
    """Получает директорию, в которой находится лаунчер, избегая временной папки."""
    if hasattr(sys, '_MEIPASS'):
        # Когда запущено в режиме onefile, берем директорию exe, а не временную
        return os.path.dirname(sys.executable)
    else:
        # При обычном запуске или режиме onedir
        return os.path.dirname(os.path.abspath(sys.argv[0]))


def load_config():
    """Загружает конфигурацию из текстового файла, имя которого совпадает с именем исполняемого файла."""
    launcher_dir = get_launcher_directory()
    exe_name = os.path.splitext(os.path.basename(sys.executable))[0]
    config_file = os.path.join(launcher_dir, f"{exe_name}.txt")

    programs = []
    try:
        with open(config_file, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if parts:
                    # Добавляем абсолютный путь для программы
                    program_name = os.path.join(launcher_dir, parts[0])
                    arguments = parts[1:]
                    programs.append((program_name, arguments))
    except FileNotFoundError:
        print(f"Конфигурационный файл {config_file} не найден.")
    return programs


def run_programs(programs):
    """Запускает программы с аргументами из конфигурации."""
    for program_name, arguments in programs:
        try:
            command = [program_name] + arguments
            subprocess.run(command, check=True)
            print(f"Запущена программа: {program_name}")
        except Exception as e:
            print(f"Ошибка при запуске {program_name}: {e}")


def main():
    programs = load_config()
    if programs:
        run_programs(programs)
    else:
        print("Список программ для запуска пуст.")


if __name__ == '__main__':
    main()
