
from main import run_analysis

file_path = "../test_files/sample_log.txt"
results = run_analysis(file_path)

print("\n===== АНАЛИЗ ЗАВЕРШЁН =====\n")
for key, value in results.items():
    print(f"=== {key.upper()} ===")
    if isinstance(value, dict):
        for k, v in value.items():
            print(f"{k}: {v}")
    elif isinstance(value, list):
        for item in value:
            print(f"- {item}")
    else:
        print(value)
    print()
