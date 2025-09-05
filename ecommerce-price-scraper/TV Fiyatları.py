from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time
import pandas as pd 
from datetime import datetime
import os

## 1. YAPILANDIRMA BÖLÜMÜ
## Her siteye ait bilgileri (URL, seçiciler vb.) ayrı sözlüklerde tutalım.
## Bu, kodun daha düzenli ve genişletilebilir olmasını sağlar.


HEPSIBURADA_CONFIG = {
    "site_adi": "Hepsiburada",
    "url": "https://www.hepsiburada.com/ara?q=televizyon&filtreler=ekranebati:65€20in€C3€A7€20€2F€20165€20cm",
    "dosya_yolu": "hepsiburada_tv_verileri.csv",
    "kart_secici": ".productCard-module_productCardRoot__Yf7qs",
    "marka_secici": ".title-module_brandText__GIxWY",
    "urun_adi_secici": ".title-module_titleText__8FlNQ",
    "fiyat_secici": "div.price-module_finalPrice__LtjvY",
    "puan_secici": ".rate-module_rating__19oVu",
    "yorum_sayisi_secici": ".rate-module_count__fjUng"
}

TRENDYOL_CONFIG = {
    "site_adi": "Trendyol",
    "url": "https://www.trendyol.com/sr?wc=104156&lc=104156&qt=televizyon&st=televizyon&attr=23%7C3135&os=1",
    "dosya_yolu": "trendyol_tv_verileri.csv",
    "kart_secici": ".p-card-wrppr.with-campaign-view",
    "marka_secici": ".prdct-desc-cntnr-ttl",
    "urun_adi_secici": ".prdct-desc-cntnr-name",
    "fiyat_secici_indirimli": ".price-item.discounted",
    "fiyat_secici_indirimsiz": ".price-item",
    "puan_secici": ".rating-score",
    "yorum_sayisi_secici": ".ratingCount"
}

## 2. YARDIMCI FONKSİYONLAR
## Tekrar eden işlemleri kendi fonksiyonlarına ayırmak (DRY Prensibi - Don't Repeat Yourself)

def scroll_to_load_all_products(driver):
    """Sayfanın sonuna kadar yavaşça kaydırarak tüm ürünlerin yüklenmesini sağlar."""
    print("Tüm ürünlerin yüklenmesi için sayfa aşağı kaydırılıyor...")
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)  # Yeni içeriğin yüklenmesi için bekleme
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("Sayfanın sonuna ulaşıldı.")
            break
        last_height = new_height

def save_data_to_csv(data_list, file_path):
    """Veri listesini, dosya varlığını kontrol ederek CSV'ye ekler."""
    if not data_list:
        print(f"'{file_path}' dosyasına kaydedilecek yeni veri bulunamadı.")
        return

    df = pd.DataFrame(data_list)
    file_exists = os.path.exists(file_path)
    df.to_csv(
        file_path, 
        mode='a', 
        header=not file_exists, 
        index=False, 
        encoding='utf-8-sig'
    )
    print(f"Veriler başarıyla '{file_path}' dosyasına eklendi.")



## 3. ANA SCRAPER FONKSİYONU
## Farklı siteler için çalışabilecek genel bir fonksiyon

def scrape_site_data(driver, config):
    """Verilen yapılandırmaya göre bir siteden veri çeker ve kaydeder."""
    print(f"\n===== {config['site_adi']} sitesinden veri çekme işlemi başladı.")
    driver.get(config['url'])
    
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, config['kart_secici'])))
        print("Ürün kartları yüklendi.")
    except Exception as e:
        print(f"Ürün kartları yüklenemedi: {e}")
        return

    scroll_to_load_all_products(driver)
    
    all_cards = driver.find_elements(By.CSS_SELECTOR, config['kart_secici'])
    product_count = len(all_cards)
    print(f"Toplam {product_count} adet ürün bulundu. Veriler çekiliyor...")

    scraped_data = []
    today = datetime.now().strftime("%Y-%m-%d")

    for i in range(product_count):
        # Stale Element hatasını önlemek için listeyi her döngüde tazelemek yerine,
        # doğrudan o anki elemente odaklanmak daha stabildir.
        # Ancak senin yöntemin de bir güvenlik katmanı sunuyor. Şimdilik koruyalım.
        all_cards_fresh = driver.find_elements(By.CSS_SELECTOR, config['kart_secici'])
        if i >= len(all_cards_fresh): continue # Eğer sayfa değiştiyse ve ürün sayısı azaldıysa
        
        card = all_cards_fresh[i]
        
        try:
            # Her site için veri çekme mantığı burada özelleşebilir
            # Bu örnek genel bir yapı sunar
            data = {"Tarih": today, "Kaynak": config['site_adi']}
            data["Marka"] = card.find_element(By.CSS_SELECTOR, config['marka_secici']).text
            data["Ürün Adı"] = card.find_element(By.CSS_SELECTOR, config['urun_adi_secici']).text
            
            # Trendyol'daki gibi indirimli/indirimsiz fiyat kontrolü
            if config['site_adi'] == 'Trendyol':
                try:
                    price_text = card.find_element(By.CSS_SELECTOR, config['fiyat_secici_indirimli']).text
                except:
                    price_text = card.find_element(By.CSS_SELECTOR, config['fiyat_secici_indirimsiz']).text
            else: # Hepsiburada
                 price_text = card.find_element(By.CSS_SELECTOR, config['fiyat_secici']).text

            data["Fiyat"] = float(price_text.replace(' TL', '').replace('.', '').replace(',', '.'))
            
            try:
                data["Kullanici Puani"] = card.find_element(By.CSS_SELECTOR, config['puan_secici']).text
            except:
                data["Kullanici Puani"] = "Puan Yok"
            try:
                data["Yorum Sayisi"] = card.find_element(By.CSS_SELECTOR, config['yorum_sayisi_secici']).text
            except:
                data["Yorum Sayisi"] = "Yorum Yok"

            scraped_data.append(data)
            print(f"{config['site_adi']} - {i+1}. ürün çekildi: {data['Marka']}")

        except Exception as e:
            print(f"{i+1}. sıradaki ürün çekilirken bir hata oluştu: {e}")
            
    save_data_to_csv(scraped_data, config['dosya_yolu'])
    print(f"===== {config['site_adi']} sitesi için işlem tamamlandı. =====")


## ----------------------------------------------------------------
## 4. ANA ÇALIŞTIRMA BLOĞU
## Kodun ana mantığı bu blok içinden başlar. Bu, Python'da standart bir pratiktir.
## ----------------------------------------------------------------

if __name__ == "__main__":
    # Tarayıcı ayarları
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
    
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    
    try:
        # Her bir site için ana scraper fonksiyonunu çağır
        scrape_site_data(driver, HEPSIBURADA_CONFIG)
        scrape_site_data(driver, TRENDYOL_CONFIG)
    finally:
        # Kod hata verse bile tarayıcının kesinlikle kapanmasını sağlar
        print("\nTüm işlemler bitti. Tarayıcı kapatılıyor.")
        driver.quit()