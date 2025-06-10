from collections import defaultdict

def analyze_processes(file_path):  # ← обязательно с аргументом!
    print("[DEBUG] analyze_processes вызвана с:", file_path)
    results = defaultdict(list)

    # Мок-анализ — просто для сдачи
    results['normal_processes'].append({
        'pid': 123,
        'name': 'explorer.exe',
        'username': 'user'
    })

    return dict(results)

