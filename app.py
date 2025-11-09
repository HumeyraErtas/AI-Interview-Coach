# app.py
import streamlit as st

from interview_analyzer import coach


st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Interview Coach")
st.write(
    "Bu uygulama, girdiğin **mülakat sorusuna** yapay zekâ ile örnek bir cevap üretir "
    "ve cevap üzerinde küçük bir analiz yapar."
)

st.markdown(
    """
Örnek sorular:
- *"How do you handle teamwork conflicts?"*
- *"Tell me about a time you failed."*
- *"Why should we hire you?"*
"""
)

question = st.text_area(
    "Mülakat sorusunu yaz:",
    value="How do you handle teamwork conflicts?",
    height=120,
)

if st.button("Cevap Üret ve Analiz Et"):
    if not question.strip():
        st.warning("Lütfen önce bir mülakat sorusu yaz.")
    else:
        with st.spinner("Cevap üretiliyor ve analiz ediliyor..."):
            result = coach(question)

        st.subheader("💬 Önerilen Cevap")
        st.write(result.answer)

        st.subheader("📊 Yapay Zekâ Skorları")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Pozitiflik", f"{result.scores['positivity']} / 100")
            st.metric("İletişim", f"{result.scores['communication']} / 100")
        with col2:
            st.metric("Yapı", f"{result.scores['structure']} / 100")
            st.metric("Detay Seviyesi", f"{result.scores['detail']} / 100")

        # Basit bar chart
        st.bar_chart(
            {
                "Pozitiflik": result.scores["positivity"],
                "İletişim": result.scores["communication"],
                "Yapı": result.scores["structure"],
                "Detay": result.scores["detail"],
            }
        )

        st.subheader("🤖 Yapay Zekâ Analizi")

        st.markdown("### 💪 Güçlü Yönler")
        if result.strengths:
            for s in result.strengths:
                st.markdown(f"- {s}")
        else:
            st.write("Belirgin bir güçlü yön tespit edilemedi.")

        st.markdown("### ⚙️ Geliştirme Alanları")
        if result.improvements:
            for im in result.improvements:
                st.markdown(f"- {im}")
        else:
            st.write("Belirgin bir geliştirme alanı tespit edilemedi.")
