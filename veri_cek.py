from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_uni_menu():
    # Chrome seçeneklerini ayarla
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Chrome servisini ayarla
    service = Service('/usr/bin/chromedriver')

    menu_items = []
    menu_date = "Menü bilgisi alınamadı"

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://unievi.firat.edu.tr/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "box__content"))
        )

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        menu_items = [item.text.strip() for item in soup.find_all("div", class_="box__content")]
        date_element = soup.find("h4", class_="container mb-3 mb-md-4 food-date")
        menu_date = date_element.text.strip() if date_element else "Tarih bulunamadı"

    except Exception as e:
        print(f"Üniversite menüsü alınırken hata oluştu: {str(e)}")
        menu_items = []
        menu_date = "Menü bilgisi alınamadı"

    finally:
        try:
            driver.quit()
        except:
            pass

    return {
        "date": menu_date,
        "items": menu_items
    }

def get_kyk_menus():
    try:
        with open("kykmenuaksam.json", "r", encoding="utf-8") as f:
            kyk_menu = json.load(f)

        with open("kykmenusabah.json", "r", encoding="utf-8") as f:
            kyk_sabah_menu = json.load(f)

        today = datetime.now().strftime("%Y-%m-%d")
        
        # Akşam menüsünü bul
        today_menu = None
        for date, menu in kyk_menu.items():
            if date == today:
                today_menu = menu
                break

        # Kahvaltı menüsünü bul
        today_sabah_menu = None
        for date, menu in kyk_sabah_menu["Mayis_Ayi_Kahvalti_Menusu"].items():
            if date == today:
                today_sabah_menu = menu
                break

        return {
            "aksam": today_menu,
            "sabah": today_sabah_menu
        }
    except Exception as e:
        print(f"KYK menüleri alınırken hata oluştu: {str(e)}")
        return {
            "aksam": None,
            "sabah": None
        }

def update_menu_data():
    uni_menu = get_uni_menu()
    kyk_menus = get_kyk_menus()
    
    menu_data = {
        "uni_menu": uni_menu,
        "kyk_menus": kyk_menus,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open("menu_data.json", "w", encoding="utf-8") as f:
        json.dump(menu_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_menu_data()
