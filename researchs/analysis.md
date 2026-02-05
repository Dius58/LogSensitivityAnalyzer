# Hassas Veri Tarama Teknikleri Araştırması
Bu çalışmada, log dosyalarındaki veri sızıntılarını tespit etmek için en güvenilir yöntemler araştırılmıştır.

### Regex Stratejisi
Araştırmalar sonucunda, sadece anahtar kelime aramanın çok fazla "false positive" (hatalı pozisyon) verdiği görülmüştür. Bu nedenle:
- `(?i)` bayrağı kullanılarak büyük/küçük harf duyarsızlığı sağlanmıştır.
- `[\s:=]+` yapısı ile kelime ve değer arasındaki boşluk, eşittir veya iki nokta üst üste gibi farklı atama operatörleri kapsama alınmıştır.

### Güvenlik Standartları
Log yönetiminde kişisel verilerin korunması (KVKK/GDPR) kapsamında, logların periyodik olarak bu tarz araçlarla taranması gerektiği saptanmıştır.
