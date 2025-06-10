import os

SUSPICIOUS_KEYWORDS = ['malware', 'backdoor', 'keylogger', 'hack', 'exploit']

def check_filesystem(scan_path=os.path.expanduser("~")):
    hidden_files = []
    executables = []

    for root, dirs, files in os.walk(scan_path):
        for name in files:
            filepath = os.path.join(root, name)

            # Скрытые файлы
            if name.startswith('.'):
                hidden_files.append(filepath)

            # Подозрительные ключевые слова (не обязательно, но можешь добавить в отчёт позже)
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in name.lower() and filepath not in executables:
                    executables.append(filepath)

            # Исполняемые файлы
            if os.access(filepath, os.X_OK) and filepath not in executables:
                executables.append(filepath)

    return {
        "hidden_files": hidden_files,
        "executables": executables
    }
