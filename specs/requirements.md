# Proje Gereksinim Analizi
**Geliştirici:** Yiğit Arslan

### İşlevsel Gereksinimler
- Sistem, kullanıcıdan alınan dizin yolundaki tüm `.log` ve `.txt` dosyalarını taramalıdır.
- Aşağıdaki hassas veri türleri Regex (Düzenli İfadeler) ile tespit edilmelidir:
  - Şifreler ve Parolalar (password, pwd, secret vb.)
  - API Anahtarları ve Tokenlar
  - IPv4 Adresleri
  - E-posta Adresleri
- Hatalı dizin yollarında kullanıcıya açıklayıcı hata mesajı verilmelidir.

### Teknik Gereksinimler
- Yazılım Python 3.x ortamında çalışmalıdır.
- Herhangi bir dış kütüphane bağımlılığı olmamalıdır (Standart kütüphaneler yeterlidir).
