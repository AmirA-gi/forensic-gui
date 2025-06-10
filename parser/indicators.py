# indicators.py
import json
import os

IOC_FILE_PATH = '/Users/ayan/Downloads/forensic_tool/utils/ios.json'


def check_iocs(file_path):
    if not os.path.exists(IOC_FILE_PATH):
        return {
            "status": "Ошибка при загрузке IOC",
            "error": f"Файл {IOC_FILE_PATH} не найден",
            "matches": []
        }

    try:
        with open(IOC_FILE_PATH, 'r', encoding='utf-8') as f:
            iocs = json.load(f)
    except Exception as e:
        return {
            "status": "Ошибка при загрузке IOC",
            "error": str(e),
            "matches": []
        }

    return {
        "status": "IOC загружены",
        "matches": []  # Здесь позже можно добавить реальные совпадения
    }
