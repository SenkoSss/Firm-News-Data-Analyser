from scraper import fetch_news
from database import save_news
from analyzer import load_news, analyze
from visualizer import plot_sources, plot_timeline 

if __name__ == "__main__":
    company = "Warta ubezpieczenia"


    print(f"Zbieranie danych dla firmy: {company}...")
    news = fetch_news(company)

    print(f"Zapis danych do bazy...")
    save_news(news, company)

    print(f"Ładowanie danych z bazy...")
    df = load_news(company)

    print(f"Analiza danych...")
    analyze(df, company)

    print(f"Tworzenie wizualizacji...")
    plot_sources(df, company)
    plot_timeline(df, company)