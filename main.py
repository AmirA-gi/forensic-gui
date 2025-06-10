
from parser import logs, filesystem, processes, network, indicators
from utils import report
from utils.html_report import generate_html_report
from utils.attack_detection import detect_attacks

print("[DEBUG] main.py загружен")

def run_analysis(file_path):
    results = {}

    print("[*] Анализ логов...")
    results['logs'] = logs.analyze_logs(file_path)

    print("[*] Проверка файловой системы...")
    results['filesystem'] = filesystem.check_filesystem(file_path)

    print("[*] Анализ процессов...")
    results['processes'] = processes.analyze_processes(file_path)

    print("[*] Анализ сетевых подключений...")
    results['network'] = network.analyze_network(file_path)

    print("[*] Проверка по IOC (Indicators of Compromise)...")
    results['ioc'] = indicators.check_iocs(file_path)

    print("[*] Анализ угроз (на основе логов)...")
    try:
        with open(file_path, "r") as f:
            log_lines = f.readlines()
        results['threats'] = detect_attacks(log_lines)
    except Exception as e:
        results['threats'] = [f"Ошибка при анализе угроз: {e}"]

    print("[*] Генерация текстового отчёта...")
    report.generate_report(results)

    print("[*] Генерация HTML-отчёта...")
    generate_html_report(results, output_path='html/report.html')

    return results
