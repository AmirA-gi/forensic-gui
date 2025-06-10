
import re

def detect_attacks(log_lines):
    alerts = []

    keywords = {
        "unauthorized": "🔴 Несанкционированный доступ",
        "failed login": "🔴 Неудачная попытка входа",
        "wget": "⚠️ Возможная загрузка вредоносного ПО",
        "powershell": "⚠️ Подозрительное использование PowerShell",
        "rm -rf": "⚠️ Попытка удаления следов",
        "suspicious": "🔴 Обнаружено подозрительное действие",
        "reverse shell": "🔴 Обнаружена попытка создания обратного соединения"
    }

    for line in log_lines:
        lower_line = line.lower()
        for key, alert in keywords.items():
            if key in lower_line:
                alerts.append(f"{alert}: {line.strip()}")

    # Анализ по частоте (пример: много попыток входа)
    failed_attempts = [line for line in log_lines if 'failed login' in line.lower()]
    if len(failed_attempts) >= 5:
        alerts.append(f"🔴 Обнаружено {len(failed_attempts)} неудачных попыток входа — возможная атака брутфорсом")

    return alerts
