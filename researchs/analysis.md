# Hassas Veri Tespiti Araştırması
Bu projede kullanılan tespit yöntemleri siber güvenlik standartları (OWASP vb.) baz alınarak araştırılmıştır.

- **Regex (Düzenli İfadeler):** Statik analiz yöntemleri arasında en hızlı ve etkili yöntem olduğu için tercih edilmiştir.
- **Duyarlılık Seviyeleri:** "Password", "Secret", "Key" gibi anahtar kelimelerin yanındaki verilerin yakalanması için "Case-Insensitive" (büyük-küçük harf duyarsız) tarama mantığı kurgulanmıştır.
- **Performans:** Büyük log dosyalarında bellek kullanımını minimize etmek için dosyalar satır satır okunacak şekilde planlanmıştır.
