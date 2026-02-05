import os
import re
import sys

# =================================================================
# PROJE: Log Sensitivity Analyzer
# GELİŞTİRİCİ: Yiğit Arslan
# AÇIKLAMA: Log dosyalarındaki hassas verileri otomatik tespit eder.
# =================================================================

# Gelişmiş Regex Desenleri (ChatGPT ve Gemini önerileriyle optimize edildi)
SENSITIVE_PATTERNS = {
    "Sifre/Parola": r"(?i)(password|passwd|secret|pwd|key|pass)[\s:=]+(\S+)",
    "API Anahtari": r"(?i)(api[_-]key|token|bearer)[\s:=]+(\S+)",
    "E-posta Adresi": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "IPv4 Adresi": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
}

def self_test():
    """
    Sistemin doğru çalışıp çalışmadığını kontrol eden 
    otomatik test mekanizması (Self-Check).
    """
    test_string = "admin_password: password123"
    # Sifre/Parola desenini test et
    match = re.search(SENSITIVE_PATTERNS["Sifre/Parola"], test_string)
    
    if match:
        print("[BAŞARILI] Sistem iç testleri onaylandı.")
        return True
    else:
        print("[HATA] Regex desenleri doğrulanamadı!")
        return False

def run_scan(target_folder):
    """
    Belirtilen klasördeki logları satır satır tarar.
    """
    found_count = 0
    
    if not os.path.exists(target_folder):
        print(f"\n[!] HATA: '{target_folder}' isimli bir klasör bulunamadı!")
        return

    print(f"\n--- Tarama Başlatıldı: {target_folder} ---")
    
    for root, _, files in os.walk(target_folder):
        for file in files:
            # Sadece log ve txt dosyalarını hedef al
            if file.endswith((".log", ".txt")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_num, line in enumerate(f, 1):
                            for label, pattern in SENSITIVE_PATTERNS.items():
                                if re.search(pattern, line):
                                    print(f"[!] {label} TESPİT EDİLDİ")
                                    print(f"    Dosya : {file}")
                                    print(f"    Satır : {line_num}")
                                    print(f"    İçerik: {line.strip()[:60]}...")
                                    print("-" * 40)
                                    found_count += 1
                except Exception as e:
                    print(f"[x] Dosya okuma hatası ({file}): {e}")

    print(f"\nTarama tamamlandı. Toplam {found_count} riskli veri bulundu.")

if __name__ == "__main__":
    # 1. Ekranı temizle (Görsel profesyonellik için)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("===============================================================")
    print("      LOG SENSITIVITY ANALYZER | GELİŞTİRİCİ: YİĞİT ARSLAN     ")
    print("===============================================================")
    
    # 2. Önce self-test çalıştır
    if self_test():
        # 3. Klasör ismini sor
        folder_input = input("\nTaranacak klasör ismini girin (Örn: tests veya .): ")
        if not folder_input: 
            folder_input = "."
        
        run_scan(folder_input)
    else:
        print("Sistem testi başarısız olduğu için program durduruldu.")
        sys.exit(1)
