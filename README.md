# Firm-News-Data-Analyser
# Company Intelligence Tool

A Python tool that automatically collects, stores, and analyzes 
news about any company using Google News RSS, PostgreSQL, and Streamlit.

## Features
- Collects latest news articles via Google News RSS
- Stores data in a PostgreSQL database
- Analyzes top sources and publishing activity over time
- Interactive web interface built with Streamlit

## Tech Stack
- **Python** — pandas, matplotlib, psycopg2, feedparser, streamlit
- **PostgreSQL** — data storage
- **Streamlit** — web interface

## Getting Started

### 1. Clone the repository
git clone https://github.com/SenkoSss/Firm-News-Data-Analyser.git
cd Firm-News-Data-Analyser

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure database
Create a `.env` file in the project root:
DB_HOST=localhost
DB_NAME=company_intel
DB_USER=postgres
DB_PASSWORD=your_password

### 4. Set up the database
Run the following SQL in PostgreSQL:
```sql
CREATE TABLE news (
    id         SERIAL PRIMARY KEY,
    company    VARCHAR(100),
    title      TEXT,
    source     VARCHAR(100),
    published  VARCHAR(100),
    link       TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 5. Run the app
python -m streamlit run app.py


## Screenshots
![alt text](image.png)
![alt text](image-1.png)

## Author
Osyp Sorokhtei — [linkedin.com/in/sorokhtei-osyp](https://linkedin.com/in/sorokhtei-osyp)