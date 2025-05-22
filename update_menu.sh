#!/bin/bash

# Python script'ini çalıştır
python3 veri_cek.py

# Değişiklikleri git'e ekle ve commit'le
git add menu_data.json
git commit -m "Menü verisi güncellendi: $(date '+%Y-%m-%d %H:%M:%S')"
git push 