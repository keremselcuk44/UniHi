# UniHi - Üniversite Bilgi Sistemi 🎓

<div align="center">

![UniHi Logo](photos/unihilogo.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-2.0-blue.svg)](https://github.com/keremselcuk44/unihi)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/keremselcuk44/unihi)
[![Contributors](https://img.shields.io/github/contributors/keremselcuk44/unihi)](https://github.com/keremselcuk44/unihi/graphs/contributors)
[![Stars](https://img.shields.io/github/stars/keremselcuk44/unihi)](https://github.com/keremselcuk44/unihi/stargazers)

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

UniHi, Fırat Üniversitesi öğrencileri için geliştirilmiş yenilikçi bir bilgi ve etkileşim platformudur. Yapay zeka destekli akıllı asistanımız, öğrencilerin akademik ve sosyal yaşamlarını kolaylaştırmak için tasarlanmış modern ve kullanıcı dostu bir arayüz sunmaktadır.

### 🌟 Neden UniHi?

- 🤖 Yapay zeka destekli kişiselleştirilmiş deneyim
- 📱 Responsive tasarım ile her cihazda mükemmel kullanım
- 🔒 Güvenlik odaklı geliştirme
- 🚀 Sürekli güncellenen içerik ve özellikler
- 💡 Kullanıcı geri bildirimleri ile sürekli iyileştirme

## ✨ Özellikler

### 🎓 Akademik Özellikler
- 📚 Detaylı fakülte ve bölüm bilgileri
- 📅 Akademik takvim entegrasyonu
- 📝 Ders programı görüntüleme
- 📊 Not takip sistemi

### 🏠 Kampüs Yaşamı
- 🏛️ KYK yurt bilgileri ve başvuru sistemi
- 🍽️ Yemekhane menü takibi
- 📚 Kütüphane durumu ve rezervasyon sistemi
- 🎯 Etkinlik takibi ve kişisel takvim

### 🤖 Yapay Zeka Özellikleri
- 💬 Akıllı asistan desteği
- 📰 Güncel yapay zeka haberleri
- 🎯 Kişiselleştirilmiş öneriler
- 🔍 Gelişmiş arama özellikleri

## 🚀 Başlangıç

### Gereksinimler

- Modern bir web tarayıcısı (Chrome, Firefox, Safari, Edge)
- İnternet bağlantısı
- JavaScript etkinleştirilmiş olmalı

### Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/keremselcuk44/unihi.git
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

### GNews API
- Haberler bölümü için kullanılmaktadır
- Ücretsiz API planı mevcuttur
- Günlük istek limiti: 100 istek

### Gemini API
- Yapay zeka asistanı için kullanılmaktadır
- Gelişmiş doğal dil işleme özellikleri
- Gerçek zamanlı yanıt sistemi

### Kendi API Anahtarınızı Almak İçin

1. [GNews Kayıt Sayfası](https://gnews.io/register)'na gidin
2. Ücretsiz hesap oluşturun
3. API anahtarınızı alın
4. `modules.html` dosyasındaki `apiKey` değişkenini güncelleyin

## 🔒 Güvenlik

### Güvenlik Önlemleri
- API anahtarları environment variables olarak saklanır
- Backend proxy kullanımı
- Rate limiting uygulaması
- Güvenli API anahtarı yönetimi
- XSS ve CSRF koruması
- Input validasyonu
- Güvenli şifreleme

### Veri Güvenliği
- SSL/TLS şifreleme
- Güvenli oturum yönetimi
- Düzenli güvenlik güncellemeleri
- Veri yedekleme sistemi

## 🛠️ Teknolojiler

### Frontend
- HTML5
- CSS3
- JavaScript (ES6+)
- Tailwind CSS
- Responsive Design

### Backend
- Node.js
- Express.js
- MongoDB
- RESTful API

### API'ler
- GNews API
- Gemini API

### Araçlar
- Git
- VS Code
- Chrome DevTools
- Postman

## 🤝 Katkıda Bulunma

1. Bu projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'feat: Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

### Katkıda Bulunma Kuralları
- Kod standartlarına uygun yazım
- Test coverage sağlama
- Dökümantasyon güncelleme
- Code review sürecine katılım

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📞 İletişim

### UniHi Ekibi
- Kerem Selçuk - Frontend Geliştirici [@keremselcuk44](https://github.com/keremselcuk44)
- Kenan Acımış - Backend Geliştirici [@acimisk](https://github.com/acimisk)
- Recep Yıldırım - UI/UX Tasarımcı [@Recep231](https://github.com/Recep231)
- Emir Ali Eşkili - Yapay Zeka Entegrasyonu [@emiralieskili](https://github.com/emiralieskili)

### Proje Linkleri
- GitHub: [https://github.com/keremselcuk44/unihi](https://github.com/keremselcuk44/unihi)

---

<div align="center">
Made with ❤️ by UniHi Team
</div>
