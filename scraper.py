import feedparser
import pandas as pd
from datetime import datetime
from urllib.parse import quote  # додали цей імпорт

def fetch_news(company_name: str) -> list:
    """Збирає новини про компанію через Google News RSS"""
    
    # quote() замінює пробіли і спецсимволи на валідний URL-формат
    encoded_name = quote(company_name)
    url = f"https://news.google.com/rss/search?q={encoded_name}&hl=pl&gl=PL&ceid=PL:pl"
    
    feed = feedparser.parse(url)
    
    results = []
    for entry in feed.entries[:10]:
        results.append({
            "title":     entry.title,
            "link":      entry.link,
            "published": entry.published,
            "source":    entry.source.title if hasattr(entry, "source") else "невідомо"
        })
    
    return results


def display_news(news: list, company_name: str):
    print(f"\n{'='*60}")
    print(f"  Новини про: {company_name}")
    print(f"  Зібрано: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}\n")
    
    for i, item in enumerate(news, 1):
        print(f"{i}. {item['title']}")
        print(f"   Джерело:    {item['source']}")
        print(f"   Дата:       {item['published']}")
        print(f"   Посилання:  {item['link']}\n")


if __name__ == "__main__":
    company = "Warta ubezpieczenia"
    
    print("Збираю новини...")
    news = fetch_news(company)
    display_news(news, company)
    
    df = pd.DataFrame(news)
    print(df.head())