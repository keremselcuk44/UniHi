# UniHi - Üniversite Bilgi Sistemi

Bu proje, üniversite öğrencileri için geliştirilmiş bir bilgi ve etkileşim platformudur.

## Özellikler

- Kullanıcı girişi ve kayıt sistemi
- Fakülte bilgileri
- Yurt bilgileri
- Etkinlik takibi
- Güncel yapay zeka haberleri

## API Kullanımı

Projede haberler bölümü için GNews API kullanılmaktadır. API anahtarı doğrudan kodda bulunmaktadır çünkü:

1. GNews'in ücretsiz API planı kullanılmaktadır
2. API anahtarı günlük sınırlı sayıda istek yapılabilir
3. Bu tür ücretsiz API'ler genellikle demo/test amaçlı kullanılır

### Kendi API Anahtarınızı Almak İçin

1. https://gnews.io/register adresine gidin
2. Ücretsiz hesap oluşturun
3. API anahtarınızı alın
4. `modules.html` dosyasındaki `apiKey` değişkenini kendi API anahtarınızla değiştirin

## Güvenlik Notu

Bu projede kullanılan API anahtarı ücretsiz ve sınırlı kullanıma sahiptir. Gerçek bir üretim ortamında:

- API anahtarları environment variables olarak saklanmalı
- Backend proxy kullanılmalı
- Rate limiting uygulanmalı
- API anahtarları güvenli bir şekilde yönetilmeli

## Teknolojiler

- HTML5
- CSS3
- JavaScript
- Tailwind CSS
- GNews API
