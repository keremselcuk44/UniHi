from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
from datetime import datetime
import requests
import os
import subprocess
import paramiko

# Chrome seçeneklerini ayarla
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")  # SSL hatalarını yoksay
chrome_options.add_argument("--headless")  # Tarayıcıyı başsız modda çalıştır
chrome_options.add_argument("--disable-gpu")  # GPU kullanımını devre dışı bırak
chrome_options.add_argument("--window-size=1920x1080")  # Ekran boyutunu ayarla

# Varsayılan değerler
menu_items = []
menu_date = "Menü bilgisi alınamadı"

try:
    # Tarayıcıyı başlat
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://unievi.firat.edu.tr/")

    # Sayfanın tamamen yüklenmesini bekle
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "box__content"))
    )

    # Sayfa içeriğini al
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Menü içeriğini çek
    menu_items = soup.find_all("div", class_="box__content")

    # Tarih bilgisini çek
    date_element = soup.find("h4", class_="container mb-3 mb-md-4 food-date")
    menu_date = date_element.text.strip() if date_element else "Tarih bulunamadı"

except Exception as e:
    print(f"Üniversite menüsü alınırken hata oluştu: {str(e)}")
    menu_items = []
    menu_date = "Menü bilgisi alınamadı"

finally:
    # Tarayıcıyı kapat
    try:
        driver.quit()
    except:
        pass

# KYK menülerini JSON dosyalarından oku
with open("kykmenuaksam.json", "r", encoding="utf-8") as f:
    kyk_menu = json.load(f)

with open("kykmenusabah.json", "r", encoding="utf-8") as f:
    kyk_sabah_menu = json.load(f)

# Mevcut HTML dosyasını aç
with open("modules.html", "r", encoding="utf-8") as f:
    existing_html = f.read()

# BeautifulSoup ile mevcut HTML'yi düzenle
soup = BeautifulSoup(existing_html, "html.parser")

# Tüm eski menü bölümlerini temizle
for old_menu in soup.find_all(["div"], id=["gunun-menusu", "kyk-menu", "kyk-sabah-menu", "menu-container", "kyk-container"]):
    old_menu.decompose()

# Slider'ı bul
slider = soup.find("div", class_="slider")

# Ana menü container'ı oluştur
menu_container = soup.new_tag("div", id="menu-container")
menu_container["class"] = "flex flex-col gap-8 mt-8 px-4"
slider.insert_after(menu_container)

# Üniversite Menüsü kısmını oluştur
uni_menu_section = soup.new_tag("div", id="gunun-menusu")
uni_menu_section["class"] = "bg-white rounded-lg shadow-lg p-6 w-full"

# JavaScript kodunu ekle
script = soup.new_tag("script")
script.string = """
function updateLikes(menuId, action, type) {
    const likeCount = document.getElementById(`${type}-like-count-${menuId}`);
    const dislikeCount = document.getElementById(`${type}-dislike-count-${menuId}`);
    const likeBtn = document.getElementById(`${type}-like-btn-${menuId}`);
    const dislikeBtn = document.getElementById(`${type}-dislike-btn-${menuId}`);
    
    if (action === 'like') {
        if (likeBtn.classList.contains('bg-green-500')) {
            likeBtn.classList.remove('bg-green-500');
            likeCount.textContent = parseInt(likeCount.textContent) - 1;
        } else {
            likeBtn.classList.add('bg-green-500');
            likeCount.textContent = parseInt(likeCount.textContent) + 1;
            if (dislikeBtn.classList.contains('bg-red-500')) {
                dislikeBtn.classList.remove('bg-red-500');
                dislikeCount.textContent = parseInt(dislikeCount.textContent) - 1;
            }
        }
    } else {
        if (dislikeBtn.classList.contains('bg-red-500')) {
            dislikeBtn.classList.remove('bg-red-500');
            dislikeCount.textContent = parseInt(dislikeCount.textContent) - 1;
        } else {
            dislikeBtn.classList.add('bg-red-500');
            dislikeCount.textContent = parseInt(dislikeCount.textContent) + 1;
            if (likeBtn.classList.contains('bg-green-500')) {
                likeBtn.classList.remove('bg-green-500');
                likeCount.textContent = parseInt(likeCount.textContent) - 1;
            }
        }
    }
}
"""
uni_menu_section.append(script)

uni_menu_section.append(soup.new_tag("h2", **{"class": "text-2xl font-bold text-center text-gray-800 mb-4"}))
uni_menu_section.h2.string = "Üniversite Günün Menüsü"
uni_menu_section.append(soup.new_tag("p", **{"class": "text-center text-gray-600 mb-6"}))
uni_menu_section.p.string = menu_date

# Yatay menü listesi
menu_list = soup.new_tag("ul", **{"class": "flex flex-wrap justify-center gap-4"})

if menu_items:
    for index, item in enumerate(menu_items):
        li = soup.new_tag("li", **{"class": "bg-gray-100 p-4 rounded-lg shadow-md flex-1 min-w-[200px] max-w-[300px]"})
        
        # Menü içeriği
        menu_content = soup.new_tag("div", **{"class": "text-center font-medium text-gray-800 mb-2"})
        menu_content.string = item.text.strip()
        li.append(menu_content)
        
        # Beğeni butonları container
        buttons_container = soup.new_tag("div", **{"class": "flex justify-center space-x-4 mt-2"})
        
        # Beğen butonu
        like_btn = soup.new_tag("button", **{
            "class": "flex items-center space-x-1 px-3 py-1 rounded-full bg-gray-200 hover:bg-green-500 hover:text-white transition-colors",
            "onclick": f"updateLikes({index}, 'like', 'uni')",
            "id": f"uni-like-btn-{index}"
        })
        like_icon = soup.new_tag("span", **{"class": "text-lg"})
        like_icon.string = "👍"
        like_count = soup.new_tag("span", **{"id": f"uni-like-count-{index}"})
        like_count.string = "0"
        like_btn.append(like_icon)
        like_btn.append(like_count)
        
        # Beğenme butonu
        dislike_btn = soup.new_tag("button", **{
            "class": "flex items-center space-x-1 px-3 py-1 rounded-full bg-gray-200 hover:bg-red-500 hover:text-white transition-colors",
            "onclick": f"updateLikes({index}, 'dislike', 'uni')",
            "id": f"uni-dislike-btn-{index}"
        })
        dislike_icon = soup.new_tag("span", **{"class": "text-lg"})
        dislike_icon.string = "👎"
        dislike_count = soup.new_tag("span", **{"id": f"uni-dislike-count-{index}"})
        dislike_count.string = "0"
        dislike_btn.append(dislike_icon)
        dislike_btn.append(dislike_count)
        
        buttons_container.append(like_btn)
        buttons_container.append(dislike_btn)
        li.append(buttons_container)
        
        menu_list.append(li)
else:
    no_menu = soup.new_tag("li", **{"class": "bg-gray-100 p-4 rounded-lg shadow-md w-full"})
    no_menu_content = soup.new_tag("div", **{"class": "text-center font-medium text-gray-800"})
    no_menu_content.string = "Menü bilgisi alınamadı"
    no_menu.append(no_menu_content)
    menu_list.append(no_menu)

uni_menu_section.append(menu_list)
menu_container.append(uni_menu_section)

# KYK menüleri için container
kyk_container = soup.new_tag("div", id="kyk-container")
kyk_container["class"] = "flex flex-col md:flex-row gap-8"

# KYK Akşam Menüsü kısmını oluştur
kyk_menu_section = soup.new_tag("div", id="kyk-menu")
kyk_menu_section["class"] = "bg-white rounded-lg shadow-lg p-6 w-full md:w-1/2"

# KYK Menüsü başlığı
kyk_menu_section.append(soup.new_tag("h2", **{"class": "text-2xl font-bold text-center text-gray-800 mb-4"}))
kyk_menu_section.h2.string = "KYK Akşam Menüsü"

# Tarih bilgisi
today = datetime.now().strftime("%Y-%m-%d")
kyk_menu_section.append(soup.new_tag("p", **{"class": "text-center text-gray-600 mb-6"}))
kyk_menu_section.p.string = today

# Bugünün menüsünü bul
today_menu = None
for date, menu in kyk_menu.items():
    if date == today:
        today_menu = menu
        break

if today_menu:
    menu_list = soup.new_tag("ul", **{"class": "space-y-4"})
    for index, (category, item) in enumerate(today_menu.items()):
        li = soup.new_tag("li", **{"class": "bg-gray-100 p-4 rounded-lg shadow-md"})
        
        # Menü içeriği
        menu_content = soup.new_tag("div", **{"class": "text-center font-medium text-gray-800 mb-2"})
        menu_content.string = f"{category}: {item}"
        li.append(menu_content)
        
        # Beğeni butonları container
        buttons_container = soup.new_tag("div", **{"class": "flex justify-center space-x-4 mt-2"})
        
        # Beğen butonu
        like_btn = soup.new_tag("button", **{
            "class": "flex items-center space-x-1 px-3 py-1 rounded-full bg-gray-200 hover:bg-green-500 hover:text-white transition-colors",
            "onclick": f"updateLikes({index}, 'like', 'kyk')",
            "id": f"kyk-like-btn-{index}"
        })
        like_icon = soup.new_tag("span", **{"class": "text-lg"})
        like_icon.string = "👍"
        like_count = soup.new_tag("span", **{"id": f"kyk-like-count-{index}"})
        like_count.string = "0"
        like_btn.append(like_icon)
        like_btn.append(like_count)
        
        # Beğenme butonu
        dislike_btn = soup.new_tag("button", **{
            "class": "flex items-center space-x-1 px-3 py-1 rounded-full bg-gray-200 hover:bg-red-500 hover:text-white transition-colors",
            "onclick": f"updateLikes({index}, 'dislike', 'kyk')",
            "id": f"kyk-dislike-btn-{index}"
        })
        dislike_icon = soup.new_tag("span", **{"class": "text-lg"})
        dislike_icon.string = "👎"
        dislike_count = soup.new_tag("span", **{"id": f"kyk-dislike-count-{index}"})
        dislike_count.string = "0"
        dislike_btn.append(dislike_icon)
        dislike_btn.append(dislike_count)
        
        buttons_container.append(like_btn)
        buttons_container.append(dislike_btn)
        li.append(buttons_container)
        
        menu_list.append(li)
    kyk_menu_section.append(menu_list)
else:
    no_menu = soup.new_tag("p", **{"class": "text-center text-gray-600"})
    no_menu.string = "Bugün için menü bilgisi bulunamadı."
    kyk_menu_section.append(no_menu)

kyk_container.append(kyk_menu_section)

# KYK Kahvaltı Menüsü kısmını oluştur
kyk_sabah_menu_section = soup.new_tag("div", id="kyk-sabah-menu")
kyk_sabah_menu_section["class"] = "bg-white rounded-lg shadow-lg p-6 w-full md:w-1/2"

# KYK Kahvaltı Menüsü başlığı
kyk_sabah_menu_section.append(soup.new_tag("h2", **{"class": "text-2xl font-bold text-center text-gray-800 mb-4"}))
kyk_sabah_menu_section.h2.string = "KYK Kahvaltı Menüsü"

# Tarih bilgisi
kyk_sabah_menu_section.append(soup.new_tag("p", **{"class": "text-center text-gray-600 mb-6"}))
kyk_sabah_menu_section.p.string = today

# Bugünün kahvaltı menüsünü bul
today_sabah_menu = None
for date, menu in kyk_sabah_menu["Mayis_Ayi_Kahvalti_Menusu"].items():
    if date == today:
        today_sabah_menu = menu
        break

if today_sabah_menu:
    menu_list = soup.new_tag("ul", **{"class": "space-y-4"})
    for index, item in enumerate(today_sabah_menu["menü"]):
        li = soup.new_tag("li", **{"class": "bg-gray-100 p-4 rounded-lg shadow-md"})
        
        # Menü içeriği
        menu_content = soup.new_tag("div", **{"class": "text-center font-medium text-gray-800 mb-2"})
        menu_text = item["isim"]
        if "gramaj" in item:
            menu_text += f" ({item['gramaj']})"
        elif "adet" in item:
            menu_text += f" ({item['adet']} adet)"
        if "ek" in item:
            menu_text += f" - {item['ek']}"
        menu_content.string = menu_text
        li.append(menu_content)
        
        # Beğeni butonları container
        buttons_container = soup.new_tag("div", **{"class": "flex justify-center space-x-4 mt-2"})
        
        # Beğen butonu
        like_btn = soup.new_tag("button", **{
            "class": "flex items-center space-x-1 px-3 py-1 rounded-full bg-gray-200 hover:bg-green-500 hover:text-white transition-colors",
            "onclick": f"updateLikes({index}, 'like', 'kyk-sabah')",
            "id": f"kyk-sabah-like-btn-{index}"
        })
        like_icon = soup.new_tag("span", **{"class": "text-lg"})
        like_icon.string = "👍"
        like_count = soup.new_tag("span", **{"id": f"kyk-sabah-like-count-{index}"})
        like_count.string = "0"
        like_btn.append(like_icon)
        like_btn.append(like_count)
        
        # Beğenme butonu
        dislike_btn = soup.new_tag("button", **{
            "class": "flex items-center space-x-1 px-3 py-1 rounded-full bg-gray-200 hover:bg-red-500 hover:text-white transition-colors",
            "onclick": f"updateLikes({index}, 'dislike', 'kyk-sabah')",
            "id": f"kyk-sabah-dislike-btn-{index}"
        })
        dislike_icon = soup.new_tag("span", **{"class": "text-lg"})
        dislike_icon.string = "👎"
        dislike_count = soup.new_tag("span", **{"id": f"kyk-sabah-dislike-count-{index}"})
        dislike_count.string = "0"
        dislike_btn.append(dislike_icon)
        dislike_btn.append(dislike_count)
        
        buttons_container.append(like_btn)
        buttons_container.append(dislike_btn)
        li.append(buttons_container)
        
        menu_list.append(li)
    kyk_sabah_menu_section.append(menu_list)
else:
    no_menu = soup.new_tag("p", **{"class": "text-center text-gray-600"})
    no_menu.string = "Bugün için kahvaltı menüsü bilgisi bulunamadı."
    kyk_sabah_menu_section.append(no_menu)

kyk_container.append(kyk_sabah_menu_section)
menu_container.append(kyk_container)

# Güncellenmiş HTML'yi kaydet
with open("modules.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Günün menüsü ve tarihi başarıyla güncellendi.")

def send_to_server(local_file, remote_path, server_config):
    """
    Dosyayı sunucuya gönderir
    """
    try:
        # SSH bağlantısı oluştur
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            server_config['host'],
            username=server_config['username'],
            password=server_config['password']
        )
        
        # SFTP istemcisi oluştur
        sftp = ssh.open_sftp()
        
        # Dosyayı sunucuya gönder
        sftp.put(local_file, remote_path)
        
        # Bağlantıları kapat
        sftp.close()
        ssh.close()
        
        print(f"Dosya başarıyla sunucuya gönderildi: {remote_path}")
        return True
    except Exception as e:
        print(f"Sunucuya gönderme hatası: {str(e)}")
        return False

def push_to_github(file_path, commit_message):
    """
    Dosyayı GitHub'a push eder
    """
    try:
        # Git komutlarını çalıştır
        subprocess.run(['git', 'add', file_path], check=True)
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        subprocess.run(['git', 'push'], check=True)
        
        print(f"Dosya başarıyla GitHub'a push edildi: {file_path}")
        return True
    except Exception as e:
        print(f"GitHub'a push hatası: {str(e)}")
        return False

def update_menus():
    """
    Menüleri günceller ve hem GitHub'a hem de sunucuya gönderir
    """
    # Sunucu yapılandırması
    server_config = {
        'host': 'your_server_host',
        'username': 'your_username',
        'password': 'your_password'
    }
    
    # Sunucu dosya yolları
    remote_paths = {
        'kykmenusabah.json': '/var/www/html/kykmenusabah.json',
        'kykmenuaksam.json': '/var/www/html/kykmenuaksam.json',
        'unimenus.json': '/var/www/html/unimenus.json'
    }
    
    # KYK sabah menüsünü güncelle
    kyk_sabah_url = "https://www.kyk.gov.tr/kyk-yurtlari-yemek-listesi"
    kyk_sabah_response = requests.get(kyk_sabah_url)
    kyk_sabah_soup = BeautifulSoup(kyk_sabah_response.text, 'html.parser')
    
    # KYK akşam menüsünü güncelle
    kyk_aksam_url = "https://www.kyk.gov.tr/kyk-yurtlari-aksam-yemek-listesi"
    kyk_aksam_response = requests.get(kyk_aksam_url)
    kyk_aksam_soup = BeautifulSoup(kyk_aksam_response.text, 'html.parser')
    
    # Üniversite menüsünü güncelle
    uni_menu_url = "https://www.firat.edu.tr/yemek-listesi"
    uni_menu_response = requests.get(uni_menu_url)
    uni_menu_soup = BeautifulSoup(uni_menu_response.text, 'html.parser')
    
    # Menüleri JSON formatına dönüştür
    kyk_sabah_data = {
        "Mayis_Ayi_Kahvalti_Menusu": {
            datetime.now().strftime("%Y-%m-%d"): {
                "menü": [
                    {"isim": item.text.strip()} for item in kyk_sabah_soup.select(".menu-item")
                ]
            }
        }
    }
    
    kyk_aksam_data = {
        "Mayis_Ayi_Aksam_Menusu": {
            datetime.now().strftime("%Y-%m-%d"): {
                "menü": [
                    {"isim": item.text.strip()} for item in kyk_aksam_soup.select(".menu-item")
                ]
            }
        }
    }
    
    uni_menu_data = {
        datetime.now().strftime("%Y-%m-%d"): {
            "menü": [
                {"isim": item.text.strip()} for item in uni_menu_soup.select(".menu-item")
            ]
        }
    }
    
    # JSON dosyalarını kaydet
    with open("kykmenusabah.json", "w", encoding="utf-8") as f:
        json.dump(kyk_sabah_data, f, ensure_ascii=False, indent=4)
    
    with open("kykmenuaksam.json", "w", encoding="utf-8") as f:
        json.dump(kyk_aksam_data, f, ensure_ascii=False, indent=4)
    
    with open("unimenus.json", "w", encoding="utf-8") as f:
        json.dump(uni_menu_data, f, ensure_ascii=False, indent=4)
    
    # Dosyaları hem GitHub'a hem de sunucuya gönder
    commit_message = f"Menüler güncellendi: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    for file_name, remote_path in remote_paths.items():
        # GitHub'a push et
        push_to_github(file_name, commit_message)
        
        # Sunucuya gönder
        send_to_server(file_name, remote_path, server_config)

if __name__ == "__main__":
    update_menus()
