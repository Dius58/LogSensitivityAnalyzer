# ChatGPT ile Regex Stratejisi Araştırması

**Soru:** "Log dosyalarındaki şifre, email ve IP gibi verileri en az hata payı ile yakalamak için hangi Regex (Düzenli İfade) desenlerini kullanmalıyım?"

### ChatGPT'nin Önerileri ve Seçilen Yöntem:
1. **Büyük/Küçük Harf Duyarsızlığı:** Loglarda "Password", "PASSWORD" veya "password" gibi farklı yazımları yakalamak için `(?i)` bayrağının kullanılması önerildi.
2. **Atama Operatörleri:** Hassas verinin sadece bir kelime olarak geçmesi değil, bir değer atanmış olması (`password: 123` veya `password = 123`) durumunu yakalamak için `[\s:=]+` deseni eklendi.
3. **Email ve IP Validasyonu:** Standart e-posta ve IPv4 desenleri kullanılarak yanlış eşleşmelerin (False Positive) önüne geçilmesi sağlandı.

**Sonuç:** Kod içerisindeki `SENSITIVE_PATTERNS` sözlüğü bu öneriler doğrultusunda optimize edildi.
