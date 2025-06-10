# report.py

def generate_report(results):
    print("\n===== FORENSIC ANALYSIS REPORT =====\n")
    for section, data in results.items():
        print(f"\n--- {section.upper()} ---")
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"{key}:")
                if isinstance(value, list):
                    for item in value:
                        print(f"  - {item}")
                else:
                    print(f"  {value}")
        else:
            print(data)
    print("\n===== END OF REPORT =====")
