# UniHi - Üniversite Bilgi Sistemi 🎓

<div align="center">

![UniHi Logo](photos/unihilogo.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-2.0-blue.svg)](https://github.com/yourusername/unihi)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/yourusername/unihi)

</div>

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Başlangıç](#-başlangıç)
  - [Gereksinimler](#gereksinimler)
  - [Kurulum](#kurulum)
- [Kullanım](#-kullanım)
- [API Entegrasyonu](#-api-entegrasyonu)
- [Güvenlik](#-güvenlik)
- [Teknolojiler](#-teknolojiler)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)
- [İletişim](#-iletişim)

## 🎯 Proje Hakkında

UniHi, Fırat Üniversitesi öğrencileri için geliştirilmiş kapsamlı bir bilgi ve etkileşim platformudur. Platform, öğrencilerin akademik ve sosyal yaşamlarını kolaylaştırmak için tasarlanmış modern ve kullanıcı dostu bir arayüz sunmaktadır.

## ✨ Özellikler

- 🔐 Güvenli kullanıcı girişi ve kayıt sistemi
- 🏛️ Detaylı fakülte ve bölüm bilgileri
- 🏠 KYK yurt bilgileri ve başvuru sistemi
- 📅 Etkinlik takibi ve kişisel takvim
- 🤖 Yapay zeka destekli asistan
- 📰 Güncel yapay zeka haberleri
- 🍽️ Yemekhane menü takibi
- 📚 Kütüphane durumu ve bilgileri
- 🎓 Akademik takvim entegrasyonu
- 📱 Responsive tasarım

## 🚀 Başlangıç

### Gereksinimler

- Modern bir web tarayıcısı (Chrome, Firefox, Safari, Edge)
- İnternet bağlantısı
- JavaScript etkinleştirilmiş olmalı

### Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/yourusername/unihi.git
```

2. Proje dizinine gidin:
```bash
cd unihi
```

3. `modules.html` dosyasını bir web tarayıcısında açın.

## 💻 Kullanım

1. Ana sayfada "Giriş Yap" butonuna tıklayın
2. Üniversite e-posta adresiniz ve şifrenizle giriş yapın
3. Dashboard üzerinden tüm özelliklere erişebilirsiniz

## 🔌 API Entegrasyonu

Projede kullanılan API'ler:

### GNews API
- Haberler bölümü için kullanılmaktadır
- Ücretsiz API planı mevcuttur
- Günlük istek limiti: 100 istek

### Kendi API Anahtarınızı Almak İçin

1. [GNews Kayıt Sayfası](https://gnews.io/register)'na gidin
2. Ücretsiz hesap oluşturun
3. API anahtarınızı alın
4. `modules.html` dosyasındaki `apiKey` değişkenini güncelleyin

## 🔒 Güvenlik

Proje güvenliği için alınan önlemler:

- API anahtarları environment variables olarak saklanmalı
- Backend proxy kullanımı
- Rate limiting uygulaması
- Güvenli API anahtarı yönetimi
- XSS ve CSRF koruması
- Input validasyonu
- Güvenli şifreleme

## 🛠️ Teknolojiler

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript (ES6+)
  - Tailwind CSS
  - Responsive Design

- **API'ler:**
  - GNews API
  - Gemini API

- **Araçlar:**
  - Git
  - VS Code
  - Chrome DevTools

## 🤝 Katkıda Bulunma

1. Bu projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'feat: Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📞 İletişim

UniHi Ekibi:
- Kerem Selçuk - [@keremselcuk](https://github.com/keremselcuk)
- Kenan Acımış - [@kenanacimis](https://github.com/kenanacimis)
- Recep Yıldırım - [@recepyildirim](https://github.com/recepyildirim)
- Emir Ali Eşkili - [@emirali](https://github.com/emirali)

Proje Linki: [https://github.com/keremselcuk44/unihi](https://github.com/yourusername/unihi)
