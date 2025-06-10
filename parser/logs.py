import os


def analyze_logs(file_path, max_lines=1000):
    if not os.path.exists(file_path):
        return {"status": "error", "error": f"Файл {file_path} не найден", "suspicious_entries": []}

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    last_lines = lines[-max_lines:]
    suspicious = [line.strip() for line in last_lines if 'error' in line.lower() or 'fail' in line.lower()]

    return {
        "status": "ok",
        "suspicious_entries": suspicious,
        "count": len(suspicious)
    }


