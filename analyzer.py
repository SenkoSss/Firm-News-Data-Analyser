import psycopg2
import pandas as pd 
from datetime import datetime

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="company_intel",
        user="postgres",
        password="200524"
    )

def load_news(company_name: str) -> pd.DataFrame:
    conn = get_connection()
    query = "SELECT title, source, published, link FROM news WHERE company = %s"
    df = pd.read_sql_query(query, conn, params=(company_name,))
    conn.close()
    return df

def analyze(df: pd.DataFrame, company_name: str):
    """ Prosta analiza """

    print(f"\n{'='* 60}")
    print(f" Analiza dla firmy: {company_name} ")
    print(f" Data zebrana: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ")
    print(f"{'='* 60}")

    # Liczba artykułów
    print(f"Liczba zebranych artykułów: {len(df)}")

    # Najczęstsze źródła
    print("\nTop 5 źródeł informacji:")
    top_sources = df['source'].value_counts().head(5)  
    for source, count in top_sources.items():
        print(f" - {source}: {count} artykułów")

    # Najnowsze artykuły
    print("\nNajnowsze artykuły:")
    latest_news = df.sort_values(by='published', ascending=False).head(5)
    for _, row in latest_news.iterrows():
        print(f" - {row['title']} ({row['source']})")

if __name__ == "__main__":
    company = "Warta ubezpieczenia"
    df = load_news(company)
    analyze(df, company)