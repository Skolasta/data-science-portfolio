# 🛒 E-commerce TV Price Scraper

Bu proje, Türkiye'deki popüler e-ticaret platformlarından (Trendyol ve Hepsiburada) televizyon fiyatlarını otomatik olarak çeken bir web scraper'dır. Selenium ve undetected-chromedriver kullanarak gerçek zamanlı fiyat verilerini toplar.

## 🎯 Amaç

E-ticaret platformlarındaki TV fiyatlarını karşılaştırmak ve pazar analizi yapmak için veri toplama aracı.

## 🚀 Özellikler

- **Multi-platform scraping**: Trendyol ve Hepsiburada desteği
- **Otomatik scroll**: Tüm ürünlerin yüklenmesi için sayfa kaydırma
- **Veri temizleme**: Fiyat, puan ve yorum verilerinin otomatik temizlenmesi
- **CSV export**: Verilerin CSV formatında kaydedilmesi
- **Modüler yapı**: Yeni siteler için kolay genişletilebilirlik
- **Anti-detection**: undetected-chromedriver ile bot tespitini önleme

## 📁 Dosya Yapısı

```
ecommerce-price-scraper/
├── TV Fiyatları.py          # Ana scraper kodu
├── requirements.txt         # Python bağımlılıkları
├── .gitignore              # Git ignore kuralları
├── README.md               # Bu dosya
└── venv/                   # Virtual environment (git'te yok)
```

## 🛠️ Kurulum

### 1. Repository'yi klonlayın
```bash
git clone [repository-url]
cd ecommerce-price-scraper
```

### 2. Virtual environment oluşturun
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Bağımlılıkları yükleyin
```bash
pip install -r requirements.txt
```

### 4. Chrome tarayıcısının yüklü olduğundan emin olun
Selenium Chrome WebDriver kullanır, Chrome tarayıcısının sisteminizde yüklü olması gerekir.

## 🚀 Kullanım

### Basit Çalıştırma
```bash
python "TV Fiyatları.py"
```

### Kod Yapısı

#### Ana Fonksiyonlar

**`scrape_site_data(driver, config)`**
- Verilen yapılandırmaya göre bir siteden veri çeker
- Parametreler: WebDriver instance ve site konfigürasyonu
- Çıktı: CSV dosyasına kaydedilen ürün verileri

**`scroll_to_load_all_products(driver)`**
- Sayfanın sonuna kadar kaydırarak tüm ürünlerin yüklenmesini sağlar
- Lazy loading ile yüklenen içerikleri bekler

**`save_data_to_csv(data_list, file_path)`**
- Veri listesini CSV formatında kaydeder
- Dosya varsa append, yoksa yeni dosya oluşturur

#### Site Konfigürasyonları

**HEPSIBURADA_CONFIG**
```python
{
    "site_adi": "Hepsiburada",
    "url": "https://www.hepsiburada.com/ara?q=televizyon&filtreler=...",
    "dosya_yolu": "hepsiburada_tv_verileri.csv",
    "kart_secici": ".productCard-module_productCardRoot__Yf7qs",
    # ... diğer CSS seçiciler
}
```

**TRENDYOL_CONFIG**
```python
{
    "site_adi": "Trendyol", 
    "url": "https://www.trendyol.com/sr?wc=104156&lc=104156&qt=televizyon...",
    "dosya_yolu": "trendyol_tv_verileri.csv",
    "kart_secici": ".p-card-wrppr.with-campaign-view",
    # ... diğer CSS seçiciler
}
```

## 📊 Çıktı Verileri

Her ürün için toplanan veriler:
- **Tarih**: Veri çekme tarihi
- **Kaynak**: Platform adı (Hepsiburada/Trendyol)
- **Marka**: Ürün markası
- **Ürün Adı**: Tam ürün adı
- **Fiyat**: Ürün fiyatı (TL)
- **Kullanıcı Puanı**: Müşteri değerlendirme puanı
- **Yorum Sayısı**: Toplam yorum sayısı

## ⚙️ Teknik Detaylar

### Kullanılan Teknolojiler
- **Python 3.x**: Ana programlama dili
- **Selenium 4.35.0**: Web automation
- **undetected-chromedriver 3.5.5**: Anti-detection
- **Pandas 2.3.1**: Veri manipülasyonu
- **Chrome WebDriver**: Tarayıcı kontrolü

### Anti-Detection Özellikleri
- User-Agent spoofing
- undetected-chromedriver kullanımı
- Doğal scroll davranışı simülasyonu
- Sayfa yükleme beklemeleri

### Hata Yönetimi
- Stale element exception handling
- Network timeout koruması
- CSS selector değişikliklerine karşı try-catch blokları
- Graceful browser shutdown

## 🔧 Özelleştirme

### Yeni Site Ekleme
1. Yeni site konfigürasyonu oluşturun:
```python
YENI_SITE_CONFIG = {
    "site_adi": "YeniSite",
    "url": "https://yenisite.com/...",
    "dosya_yolu": "yenisite_verileri.csv",
    "kart_secici": ".product-card",
    # ... CSS seçiciler
}
```

2. Ana fonksiyonda çağırın:
```python
scrape_site_data(driver, YENI_SITE_CONFIG)
```

### Filtre Değiştirme
URL'lerdeki filtre parametrelerini değiştirerek farklı ürün kategorileri için kullanabilirsiniz.

## ⚠️ Önemli Notlar

### Yasal Uyarılar
- Bu scraper sadece eğitim ve araştırma amaçlıdır
- Sitelerin robots.txt ve kullanım şartlarına uygun kullanın
- Aşırı istek göndermeyin (rate limiting)
- Ticari kullanım için site sahiplerinden izin alın

### Teknik Sınırlamalar
- CSS seçiciler değişebilir (site güncellemeleri)
- Anti-bot sistemleri scraper'ı engelleyebilir
- Network bağlantı sorunları oluşabilir
- Büyük veri setleri için memory kullanımına dikkat edin

### Performans İpuçları
- Scraping işlemini gece saatlerinde çalıştırın
- Çok fazla concurrent request yapmayın
- Düzenli olarak CSS seçicileri kontrol edin
- Veri boyutu büyükse batch processing kullanın

## 🔗 İlgili Projeler

Bu scraper ile toplanan veriler şu analizlerde kullanılmıştır:
- **E-ticaret TV Fiyat Analizi**: Platform karşılaştırma analizi
- **Pazar Zekası Dashboard'u**: Fiyat trend analizi
- **Rekabet Analizi**: Marka pozisyonlama çalışması

## 📧 İletişim

Sorularınız için iletişime geçebilirsiniz.

---
*Bu proje eğitim amaçlıdır. Ticari kullanım için gerekli izinleri alınız.*