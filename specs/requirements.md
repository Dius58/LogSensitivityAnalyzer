# Teknik Gereksinimler ve Analiz
1. **Dosya Desteği:** Araç; .log, .txt ve .conf uzantılı dosyaları tarayabilmelidir.
2. **Hassas Veri Tipleri:** - E-posta adresleri
   - IPv4 adresleri
   - Şifre ve gizli anahtar kalıpları (Regex tabanlı)
   - API Token yapıları
3. **Hata Yönetimi:** Okunamayan dosyalar veya yanlış dizin yollarında sistem çökmemeli, kullanıcıyı uyarmalıdır.
4. **Çıktı Formatı:** Tespit edilen her bulgu; dosya adı, satır numarası ve veri tipi ile raporlanmalıdır.
