import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="company_intel",
        user="postgres",
        password="200524"
    )

def save_news(news: list, company_name: str):
    conn = get_connection()
    cursor = conn.cursor()
    
    for item in news:
        cursor.execute("""
            INSERT INTO news (company, title, source, published, link)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            company_name,
            item["title"],
            item["source"],
            item["published"],
            item["link"]
        ))
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Збережено {len(news)} новин у базу даних.")