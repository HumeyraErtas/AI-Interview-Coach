# interview_analyzer.py
import re
from dataclasses import dataclass
from typing import Dict, List, Tuple

import nltk
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from transformers import pipeline

# GEREKLİ NLTK MODELLERİNİ İNDİR
def ensure_nltk_resources():
    for resource in ["punkt", "punkt_tab"]:
        try:
            nltk.data.find(f"tokenizers/{resource}")
        except LookupError:
            nltk.download(resource)

ensure_nltk_resources()

# --------------------------
# Modelleri yükle
# --------------------------
# Küçük bir text-generation modeli: distilgpt2
text_generator = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=200,
)

# Sentiment analizi için hazır pipeline
sentiment_analyzer = pipeline(
    "sentiment-analysis"
)


@dataclass
class AnalysisResult:
    answer: str
    scores: Dict[str, int]
    strengths: List[str]
    improvements: List[str]


# --------------------------
# Yardımcı fonksiyonlar
# --------------------------

def generate_answer(question: str) -> str:
    """
    Kullanıcının sorduğu mülakat sorusuna profesyonel örnek cevap üretir.
    İngilizce cevap üretir ve STAR (Situation, Task, Action, Result) yaklaşımına odaklanır.
    """
    base_prompt = (
        "You are a senior software engineer in a job interview.\n"
        f"Interview question: \"{question}\"\n\n"
        "Give a professional and structured answer in English using the STAR method "
        "(Situation, Task, Action, Result). Focus on clear communication, teamwork and self-reflection.\n\n"
        "Answer:\n"
    )

    raw_output = text_generator(
        base_prompt,
        do_sample=True,
        temperature=0.8,
        top_p=0.9,
        num_return_sequences=1,
    )[0]["generated_text"]

    # Prompt kısmını temizle, sadece cevabı al
    answer = raw_output.split("Answer:")[-1].strip()

    # Çok uzunsa biraz kırp (örnek olarak)
    sentences = nltk.sent_tokenize(answer)
    if len(sentences) > 8:
        answer = " ".join(sentences[:8])

    return answer


def compute_sentiment_score(text: str) -> Tuple[int, str]:
    """
    HuggingFace sentiment sonucu → 0-100 arası skor ve label döner.
    """
    res = sentiment_analyzer(text[:512])[0]  # çok uzunsa kes
    label = res["label"]  # POSITIVE / NEGATIVE
    score = float(res["score"])

    if label.upper() == "POSITIVE":
        # pozitifse 60-100 arası
        scaled = int(60 + score * 40)
    else:
        # negatifse 0-40 arası
        scaled = int((1 - score) * 40)

    return scaled, label


def compute_detail_score(text: str) -> int:
    """
    Kelime sayısına göre 0-100 arası detay skoru.
    Çok kısa cevaplar düşük puan alır.
    """
    words = text.split()
    n = len(words)

    if n < 40:
        return 30
    if n < 80:
        return 60
    if n < 150:
        return 85
    return 100


def compute_structure_score(text: str) -> int:
    """
    Yapısal anahtar kelimelere (first, then, finally vs.) bakarak 0-100 skoru.
    """
    text_lower = text.lower()
    structure_words = [
        "first", "then", "after that", "finally", "in the end",
        "situation", "task", "action", "result"
    ]
    hits = sum(1 for w in structure_words if w in text_lower)

    if hits == 0:
        return 40
    if hits <= 2:
        return 65
    if hits <= 4:
        return 80
    return 95


def compute_communication_score(text: str) -> int:
    """
    Basit bir iletişim skoru:
    - 'I', 'we', 'team', 'communicate', 'feedback' gibi kelimelere bakar.
    """
    text_lower = text.lower()
    comm_words = [
        "team", "we", "collaborate", "together", "communicate",
        "communication", "feedback", "listen", "listened", "empathy"
    ]
    hits = sum(1 for w in comm_words if w in text_lower)

    if hits == 0:
        return 50
    if hits <= 2:
        return 70
    if hits <= 4:
        return 85
    return 95


def extract_keywords(text: str, top_k: int = 8) -> List[str]:
    """
    Çok basit keyword extraction:
    - Noktalama silinir
    - Küçük harf yapılır
    - Stopword'ler atılır
    - En sık geçen kelimelerden top_k seçilir
    """
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = [t.lower() for t in text.split() if t.lower() not in ENGLISH_STOP_WORDS and len(t) > 3]

    freq: Dict[str, int] = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1

    # frekansa göre sırala
    sorted_tokens = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_tokens[:top_k]]


def build_feedback(
    sentiment_score: int,
    comm_score: int,
    structure_score: int,
    detail_score: int,
    keywords: List[str],
) -> Tuple[List[str], List[str]]:
    """
    Güçlü yönler ve geliştirme alanları listesi döner.
    """
    strengths = []
    improvements = []

    # Güçlü yönler
    if sentiment_score >= 70:
        strengths.append("Pozitif ve yapıcı bir ton kullanılmış.")
    if comm_score >= 75:
        strengths.append("İletişim ve ekip çalışması vurgusu güçlü.")
    if structure_score >= 75:
        strengths.append("Cevap iyi yapılandırılmış ve akışı anlaşılır.")
    if detail_score >= 80:
        strengths.append("Cevap yeterince detaylı ve somut örnekler içeriyor gibi görünüyor.")

    # Geliştirme alanları
    if sentiment_score < 60:
        improvements.append("Daha pozitif, çözüm odaklı bir dil kullanabilirsin.")
    if comm_score < 75:
        improvements.append("Ekip içi iletişim, işbirliği ve geri bildirim örneklerine daha fazla yer verebilirsin.")
    if structure_score < 70:
        improvements.append("Cevabı STAR (Situation, Task, Action, Result) yapısına göre düzenleyebilirsin.")
    if detail_score < 70:
        improvements.append("Cevabına daha somut detaylar, adımlar ve sonuçlar ekleyebilirsin (rakam, etki vb.).")

    if keywords:
        strengths.append(f"Cevapta öne çıkan temalar: {', '.join(keywords)}.")

    return strengths, improvements


# --------------------------
# Ana fonksiyon
# --------------------------

def coach(question: str) -> AnalysisResult:
    """
    Ana pipeline:
    1. Cevap üret
    2. Cevabı analiz et
    3. Skorlar + geri bildirim döndür
    """
    answer = generate_answer(question)

    sentiment_score, sentiment_label = compute_sentiment_score(answer)
    detail_score = compute_detail_score(answer)
    structure_score = compute_structure_score(answer)
    comm_score = compute_communication_score(answer)
    keywords = extract_keywords(answer)

    strengths, improvements = build_feedback(
        sentiment_score,
        comm_score,
        structure_score,
        detail_score,
        keywords,
    )

    scores = {
        "positivity": sentiment_score,
        "communication": comm_score,
        "structure": structure_score,
        "detail": detail_score,
    }

    # İletişim puanını özellikle sorunun yanında göstermek istiyorsan:
    if sentiment_label.upper() == "POSITIVE":
        strengths.append(f"Cevabın genel duygu tonu pozitif (model etiketi: {sentiment_label}).")
    else:
        improvements.append(f"Cevabın duygu tonu yeterince pozitif değil (model etiketi: {sentiment_label}).")

    return AnalysisResult(
        answer=answer,
        scores=scores,
        strengths=strengths,
        improvements=improvements,
    )
