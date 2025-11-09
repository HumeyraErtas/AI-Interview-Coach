# 🧠 AI Interview Coach  
### Yapay Zekâ Destekli Mülakat Sorusu Analiz ve Yanıt Üretici  

**AI Interview Coach**, yapay zekâ destekli bir NLP projesidir.  
Kullanıcıdan gelen bir mülakat sorusunu alır, HuggingFace modeliyle örnek bir profesyonel cevap üretir  
ve cevabı analiz ederek güçlü ve zayıf yönleri değerlendirir.  

---

## 🚀 Özellikler

✅ Kullanıcının yazdığı mülakat sorusuna otomatik örnek cevap üretir  
✅ Cevap üzerinde duygu (pozitiflik), iletişim, yapı ve detay analizleri yapar  
✅ Güçlü yönler 💪 ve geliştirme alanlarını ⚙️ özetler  
✅ Streamlit arayüzü ile etkileşimli kullanım  
✅ HuggingFace `distilgpt2` modeli ile text-generation  
✅ HuggingFace sentiment modeli + NLTK + sklearn ile metin analizi  
✅ Kullanıcı dostu arayüz ve basit kurulum  

---

## 🧩 Kullanılan Teknolojiler

| Katman | Teknoloji |
|--------|------------|
| Backend / NLP | Python, Transformers (distilgpt2, sentiment-analysis) |
| NLP Toolkit | NLTK, scikit-learn |
| Frontend | Streamlit |
| Model | HuggingFace Transformers |
| Veri Analizi | PyTorch (CPU uyumlu) |

---

## 📂 Proje Yapısı

```bash
ai-interview-coach/
│
├─ app.py                  # Streamlit UI
├─ interview_analyzer.py   # NLP ve analiz fonksiyonları
└─ requirements.txt        # Gerekli bağımlılıklar
⚙️ Kurulum
1️⃣ Projeyi Klonla
bash
Kodu kopyala
git clone https://github.com/<kullanıcı-adın>/ai-interview-coach.git
cd ai-interview-coach
2️⃣ Gerekli Kütüphaneleri Yükle
bash
Kodu kopyala
pip install -r requirements.txt
3️⃣ Uygulamayı Çalıştır
bash
Kodu kopyala
streamlit run app.py
👉 Tarayıcıda aç: http://localhost:8501

💬 Kullanım
Uygulamayı başlat.

“Mülakat sorusunu yaz” alanına bir soru gir:

“How do you handle teamwork conflicts?”

“Tell me about a time you failed.”

“Why should we hire you?”

“Cevap Üret ve Analiz Et” butonuna bas.

AI tarafından üretilen cevap, skorlar ve analiz ekranda görüntülenir.

📊 Çıktı Örneği
Soru:

How do you handle teamwork conflicts?

AI Cevabı (kısaltılmış):

In a past project, we had a disagreement about deadlines. I initiated an open discussion to align expectations.
We identified priorities, distributed tasks more effectively, and met our goal on time.

Skorlar:

Ölçüt	Puan
Pozitiflik	86
İletişim	90
Yapı	84
Detay	78

Yapay Zekâ Analizi:
💪 Güçlü yön: Pozitif ve çözüm odaklı ton
⚙️ Geliştirme alanı: Daha fazla somut örnek ve sonuç detayı eklenebilir

🧠 NLP Mantığı
Model akışı şu adımlardan oluşur:

Text Generation (distilgpt2)
→ Prompt: “You are a senior engineer in an interview. Answer the question professionally using the STAR method.”
→ Model örnek bir yanıt üretir.

Sentiment Analysis (transformers pipeline)
→ Üretilen cevabın pozitiflik skoru çıkarılır.

Keyword & Structure Analysis (nltk + sklearn)
→ STAR yapısına, iletişim kelimelerine ve detay uzunluğuna göre skor hesaplanır.

Feedback Builder
→ Güçlü yönler ve geliştirme alanları listelenir.

🧪 Test
İlk kez çalıştırdığında NLTK otomatik olarak gerekli veri setlerini (punkt, punkt_tab) indirir.
Alternatif olarak manuel de yükleyebilirsin:

python
Kodu kopyala
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
🌱 Geliştirme Fikirleri
 Türkçe mülakat sorusu ve cevabı desteği

 OpenAI API entegrasyonu (GPT-4 / GPT-5)

 Kullanıcı oturumu & geçmiş analiz kayıtları

 PDF raporu oluşturma (ReportLab)

 Mülakat türüne göre ton ayarlama (teknik, davranışsal, liderlik)

🧑‍💻 Katkıda Bulunma
Fork yap

Yeni bir branch oluştur (feature/yeni-ozellik)

Kodlarını commit et

Pull request gönder 🎉

📜 Lisans
Bu proje MIT Lisansı ile yayınlanmıştır.
Detaylar için LICENSE dosyasına bakabilirsiniz.

✨ Geliştirici
Hümeyra Ertaş
💬 Yapay zekâ destekli kişisel gelişim ve NLP projeleri geliştiriyorum.

“Good interviews are not about memorized answers — they’re about reflection and clarity.”

— AI Interview Coach

yaml
Kodu kopyala

---

İstersen bir sonraki adımda bu README’ye:  
📸 *ekran görüntüsü alanı*, 🔗 *demo linki (Render/Railway deploy)* ve 🏆 *“Extra + Puan Özellikler”* bölümü ekleyebilirim.  
Bunlardan hangisini istersin ekleyeyim?
