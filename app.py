import streamlit as st
from database import save_news
from scraper import fetch_news
from analyzer import load_news, analyze
from visualizer import plot_sources, plot_timeline

st.title("Company Intelligence Dashboard")
st.write("Zbieraj, analizuj i wizualizuj dane o firmach w czasie rzeczywistym!")

company = st.text_input("Wprowadź nazwę firmy", "Warta ubezpieczenia")

if st.button("Zbierz dane"):
    if company:
        with st.spinner("Zbieranie danych..."):
            news = fetch_news(company)
            save_news(news, company)
            df = load_news(company)

        st.success(f"Zebrano {len(news)} artykułów dla {company}!")
        
        # tablica z danymi
        st.subheader("Artykuły:")
        st.dataframe(df[["title", "source", "published"]])

        st.subheader("Analiza:")
        fig1 = plot_sources(df, company)
        st.pyplot(fig1)

        st.subheader("Timeline:")
        fig2 =  plot_timeline(df, company)
        st.pyplot(fig2)
    else:
        st.error("Proszę wprowadzić nazwę firmy!")
