#!/bin/bash

# Çalışma dizinini ayarla
cd /var/www/html

# Python script'ini çalıştır
python3 veri_cek.py

# Dosya izinlerini ayarla
chmod 644 menu_data.json

# Git işlemleri (eğer git kullanıyorsanız)
# git add menu_data.json
# git commit -m "Menü verisi güncellendi: $(date '+%Y-%m-%d %H:%M:%S')"
# git push 