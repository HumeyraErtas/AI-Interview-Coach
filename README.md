# 🧠 AI Interview Coach
### Yapay Zekâ Destekli Mülakat Sorusu Analiz ve Yanıt Üretici

**AI Interview Coach**, kullanıcının girdiği mülakat sorusuna HuggingFace modelleriyle örnek cevap üreten ve bu cevabı çeşitli ölçütlere göre analiz ederek güçlü/geliştirme alanlarını özetleyen küçük bir NLP uygulamasıdır.
## 🧩 Kullanılan Teknolojiler

| Katman | Teknoloji |
|-------:|:---------|
| Backend / NLP | Python, Transformers (distilgpt2, sentiment-analysis) |
| NLP Toolkit | NLTK, scikit-learn |
| Frontend | Streamlit |
| Model | HuggingFace Transformers |
| Veri İşleme | PyTorch (CPU uyumlu) |

---

## 📂 Proje Yapısı

```
ai-interview-coach/
├─ app.py                  # Streamlit UI
├─ interview_analyzer.py   # NLP ve analiz fonksiyonları
└─ requirements.txt        # Gerekli bağımlılıklar
```

## ⚙️ Kurulum

1) Depoyu klonlayın:

```bash
git clone https://github.com/<kullanıcı-adın>/ai-interview-coach.git
cd ai-interview-coach
```

2) Bağımlılıkları kurun:

```bash
pip install -r requirements.txt
```

3) Uygulamayı çalıştırın:

```bash
streamlit run app.py
```

Tarayıcıda aç: http://localhost:8501

---

## 💬 Kullanım

1. Uygulamayı başlatın.
2. “Mülakat sorusunu yaz” alanına bir soru girin (ör. "How do you handle teamwork conflicts?").
3. "Cevap Üret ve Analiz Et" butonuna basın.
4. AI tarafından üretilen cevap, puanlar ve analiz ekran üzerinde gösterilecektir.

---

## 📊 Örnek Çıktı

Soru: How do you handle teamwork conflicts?

AI Cevabı (kısaltılmış):
> In a past project, we had a disagreement about deadlines. I initiated an open discussion to align expectations...

Skorlar (örnek): Pozitiflik 86, İletişim 90, Yapı 84, Detay 78

---

## 🧠 Teknik Notlar

- Projede `distilgpt2` text-generation pipeline'ı ve transformers'ın hazır sentiment pipeline'ı kullanılıyor.
- NLTK ilk kullanımda `punkt` tokenizer'ını indirir; eğer otomatik indirme sorun çıkartıyorsa elle yükleyebilirsiniz:

```python
import nltk
nltk.download('punkt')
```

---

## 🧪 Test & Geliştirme

- İyileştirme fikirleri:
	- Türkçe soru/cevap desteği eklemek
	- OpenAI API entegrasyonu (GPT-4/5) seçeneği sunmak
	- Kullanıcı oturumu ve geçmiş analiz kayıtları
	- PDF raporu oluşturma (ReportLab)

---

## 🧑‍💻 Katkıda Bulunma

1. Fork yapın
2. Yeni bir branch oluşturun (ör. `feature/yeni-ozellik`)
3. Değişiklikleri commit edin
4. Pull request gönderin

---

## 📜 Lisans

Bu proje MIT Lisansı ile yayınlanmıştır. Detaylar için `LICENSE` dosyasına bakın.

---

## ✨ Geliştirici

Hümeyra Ertaş — Yapay zekâ destekli kişisel gelişim ve NLP projeleri geliştiriyorum.

"Good interviews are not about memorized answers — they're about reflection and clarity."

---

İsterseniz README'ye ekran görüntüsü alanı, deploy demo linki (Render/Railway) ve "Extra + Puan Özellikler" bölümlerini ekleyebilirim. Hangi bölümleri eklememi istersiniz?
“Good interviews are not about memorized answers — they’re about reflection and clarity.”

— AI Interview Coach

yaml
Kodu kopyala

---

İstersen bir sonraki adımda bu README’ye:  
📸 *ekran görüntüsü alanı*, 🔗 *demo linki (Render/Railway deploy)* ve 🏆 *“Extra + Puan Özellikler”* bölümü ekleyebilirim.  
Bunlardan hangisini istersin ekleyeyim?
