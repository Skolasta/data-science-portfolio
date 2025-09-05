# 📊 Data Analytics Portfolio

Bu repository, farklı sektörlerde gerçekleştirdiğim veri analizi projelerini içermektedir. Her proje, gerçek dünya verilerini kullanarak iş problemlerine çözüm odaklı yaklaşımlar sunmaktadır.

## 🚀 Projeler

### 1. 📞 Telco Customer Churn Analysis
**Dosya:** `telco-churn-analysis-insights/`
- **Amaç:** Telekomünikasyon şirketinde müşteri kaybını (churn) analiz etme ve önleme stratejileri geliştirme
- **Veri Seti:** Telco müşteri verileri (Excel formatında)
- **Teknikler:** 
  - Keşifsel Veri Analizi (EDA)
  - Churn Analysis
  - Feature Engineering
  - Müşteri segmentasyonu
- **Temel Fonksiyonlar:**
  - `data_inv()`: Veri seti genel inceleme fonksiyonu
- **Sonuç:** Fiber internet müşterileri için ek hizmet önerileri ve risk grupları belirlendi
- **Dosyalar:** Türkçe ve Kaggle versiyonları mevcut

### 2. 🎬 Movie Industry Profit Analysis  
**Dosya:** `movie-industry-profit-analysis/`
- **Amaç:** Film endüstrisi kar marjı analizi ve başarı faktörlerinin belirlenmesi
- **Teknikler:** 
  - JSON Parsing ve veri dönüştürme
  - Revenue Analysis
  - Genre-based profitability analysis
- **Temel Fonksiyonlar:**
  - `data_inv()`: Veri seti genel inceleme
  - `normalized_name()`: JSON verilerinden isim çıkarma
  - `find_director()`: Yönetmen bilgisi çıkarma
- **Sonuç:** Animasyon türü en karlı segment olarak belirlendi
- **Dosyalar:** Türkçe, İngilizce ve Kaggle versiyonları

### 3. 🛒 RFM Customer Segmentation (Retail)
**Dosya:** `rfm-customer-segmentation-retail/`
- **Amaç:** E-ticaret müşterilerinin RFM analizi ile segmentasyonu
- **Teknikler:** 
  - RFM Analysis (Recency, Frequency, Monetary)
  - Customer Segmentation
  - Behavioral Analysis
- **Temel Fonksiyonlar:**
  - `data_inv()`: Veri seti genel inceleme
- **Sonuç:** Best Customers, Loyal Customers, At Risk müşteri grupları tanımlandı
- **Dosyalar:** Türkçe ve İngilizce versiyonları

### 4. 🛒 E-commerce TV Price Scraper
**Dosya:** `ecommerce-price-scraper/`
- **Amaç:** Türkiye e-ticaret platformlarından (Trendyol, Hepsiburada) TV fiyatlarını otomatik çekme
- **Teknikler:**
  - Web Scraping (Selenium)
  - Anti-detection (undetected-chromedriver)
  - Automated scrolling ve lazy loading
  - Multi-platform data collection
- **Temel Fonksiyonlar:**
  - `scrape_site_data()`: Site-specific veri çekme
  - `scroll_to_load_all_products()`: Otomatik sayfa kaydırma
  - `save_data_to_csv()`: CSV export fonksiyonu
- **Çıktı:** Hepsiburada ve Trendyol TV verileri (CSV formatında)
- **Dosyalar:** Python scraper kodu, requirements.txt, README.md

### 5. 📺 E-commerce TV Price Analytics (Turkey)
**Dosya:** `ecommerce-price-analytics-turkey/`
- **Amaç:** Scraper ile toplanan verilerin analizi ve platform karşılaştırması
- **Veri Kaynağı:** Yukarıdaki scraper ile çekilen gerçek e-ticaret verileri
- **Teknikler:** 
  - Multi-platform Price Analysis
  - Feature Extraction from Product Names
  - Competitive Intelligence
- **Temel Fonksiyonlar:**
  - `ekran_teknolojisi_belirle()`: Ürün adından ekran teknolojisi çıkarma
  - `çözünürlük_belirle()`: Ürün adından çözünürlük bilgisi çıkarma
  - `smart_teknoloji_belirle()`: Smart TV teknolojisi belirleme
  - `yorum_duzenleme()`: Yorum sayısı veri temizleme
  - `puan_duzenleme()`: Kullanıcı puanı veri temizleme
- **Sonuç:** Platform bazlı fiyat karşılaştırması ve pazar analizi
- **Dosyalar:** Kaggle versiyonu ve örnek veri seti
- **Not:** Gerçek scraped veriler telif hakkı koruması nedeniyle repository'de bulunmamaktadır

## 🛠️ Kullanılan Teknolojiler

### Programlama ve Kütüphaneler
- **Python**: Ana programlama dili
- **Pandas**: Veri manipülasyonu ve analizi
- **NumPy**: Sayısal hesaplamalar
- **AST**: JSON veri parsing (film projesi)

### Veri Görselleştirme
- **Matplotlib**: Temel grafik oluşturma
- **Seaborn**: İstatistiksel veri görselleştirme

### Geliştirme Ortamı
- **Jupyter Notebook**: İnteraktif veri analizi
- **Selenium**: Web scraping ve automation
- **undetected-chromedriver**: Anti-detection web scraping

### Veri Formatları
- **CSV**: Yapılandırılmış veri depolama
- **Excel**: İş verilerinin analizi
- **JSON**: Karmaşık veri yapıları (film verileri)

## 📁 Proje Yapısı

```
data-analytics-portfolio/
├── ecommerce-price-scraper/
│   ├── TV Fiyatları.py
│   ├── requirements.txt
│   └── README.md
├── ecommerce-price-analytics-turkey/
│   ├── ecommerce-price-analytics-turkey_kaggle.ipynb
│   └── sample_tv_data.csv
├── telco-churn-analysis-insights/
│   ├── telco_churn_kaggle.ipynb
│   └── Telco_customer_churn.xlsx
├── movie-industry-profit-analysis/
│   └── movie-industry-profit-analysis_kaggle.ipynb
├── rfm-customer-segmentation-retail/
│   ├── rfm-customer-segmentation-retail.ipynb
│   └── rfm-customer-segmentation-retail_EN.ipynb
└── README.md
```

## 🔍 Ortak Fonksiyonlar

Projelerde kullanılan ortak yardımcı fonksiyonlar:

### `data_inv(df)` - Veri Seti İnceleme
Tüm projelerde kullanılan standart veri inceleme fonksiyonu:
- Satır ve sütun sayısı
- Sütun isimleri ve veri tipleri  
- Eksik değer analizi
- İlk ve son kayıtların görüntülenmesi

### Veri Temizleme Fonksiyonları
- **E-ticaret projesi**: Yorum sayısı ve puan temizleme
- **Film projesi**: JSON parsing ve director çıkarma
- **TV fiyat projesi**: Ürün özelliği çıkarma

## 📊 Analiz Metodolojisi

1. **Veri Keşfi**: Her projede `data_inv()` fonksiyonu ile başlangıç
2. **Veri Temizleme**: Proje özelinde temizleme fonksiyonları
3. **Feature Engineering**: Ürün adlarından özellik çıkarma
4. **Analiz**: Sektöre özel analiz teknikleri
5. **Görselleştirme**: Matplotlib/Seaborn ile insight'lar
6. **Sonuç**: Actionable business insights

## 🎯 İş Değeri

Her proje gerçek iş problemlerine odaklanmıştır:
- **Data Collection**: Otomatik veri toplama ve web scraping
- **Churn Prevention**: Müşteri kaybını önleme stratejileri
- **Market Intelligence**: Film endüstrisi yatırım kararları
- **Customer Segmentation**: Hedefli pazarlama stratejileri  
- **Competitive Analysis**: E-ticaret fiyat stratejileri

## 📧 İletişim
Bu projeler hakkında daha fazla bilgi için iletişime geçebilirsiniz.

---
*Bu portfolio, veri bilimi ve analitik yeteneklerimi sergileyen gerçek dünya projelerini içermektedir.*
