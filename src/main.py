import os
import re

# Hassas veri desenleri
SENSITIVE_PATTERNS = {
    "Sifre/Gizli Veri": r"(?i)(password|passwd|secret|pwd|key)[\s:=]+(\S+)",
    "API Anahtari": r"(?i)(api[_-]key|token)[\s:=]+(\S+)",
    "Email Adresi": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "IP Adresi": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
}

def analyze_logs(target_path):
    print(f"\n--- Tarama Baslatildi: {target_path} ---")
    found_count = 0

    if not os.path.exists(target_path):
        print("Hata: Klasor bulunamadi!")
        return

    for root, dirs, files in os.walk(target_path):
        for file in files:
            if file.endswith((".log", ".txt", ".conf")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_num, line in enumerate(f, 1):
                            for label, pattern in SENSITIVE_PATTERNS.items():
                                if re.search(pattern, line):
                                    print(f"[!] {label} BULUNDU!")
                                    print(f"    Dosya: {file} | Satir: {line_num}")
                                    print(f"    Icerik: {line.strip()[:100]}")
                                    found_count += 1
                except Exception as e:
                    print(f"Hata olustu {file}: {e}")

    print(f"\n--- Tarama Tamamlandi. {found_count} adet hassas veri tespit edildi. ---")

if __name__ == "__main__":
    path = input("Taranacak klasor yolunu girin (Mevcut klasor icin . yazin): ")
    analyze_logs(path)
