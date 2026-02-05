import os
import re

# Yiğit Arslan - Log Sensitivity Analyzer
# Bu araç güvenlik amaçlı log taraması yapar.

SENSITIVE_PATTERNS = {
    "Sifre/Parola": r"(?i)(password|passwd|secret|pwd|key)[\s:=]+(\S+)",
    "API Anahtari": r"(?i)(api[_-]key|token)[\s:=]+(\S+)",
    "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "IP Adresi": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
}

def self_test():
    """Hocanın istediği otomatik test mekanizması"""
    test_data = "admin_pass: 123456"
    return bool(re.search(SENSITIVE_PATTERNS["Sifre/Parola"], test_data))

def run_scan(folder):
    found = 0
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith((".log", ".txt")):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        for label, pattern in SENSITIVE_PATTERNS.items():
                            if re.search(pattern, line):
                                print(f"[!] {label} Bulundu -> Dosya: {file}, Satir: {i}")
                                found += 1
    print(f"\nTarama bitti. Toplam {found} bulgu.")

if __name__ == "__main__":
    print("--- Log Sensitivity Analyzer | Geliştirici: Yiğit Arslan ---")
    if self_test():
        target = input("Taranacak klasör (Mevcut dizin için '.'): ")
        run_scan(target)
