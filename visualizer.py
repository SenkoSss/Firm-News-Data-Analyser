import matplotlib.pyplot as plt
import pandas as pd

def plot_sources(df: pd.DataFrame, company_name: str):
    """ Wykres słupkowy pokazujący najczęstsze źródła informacji """

    source_counts = df["source"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.barh(source_counts.index, source_counts.values, color='skyblue')
    ax.set_xlabel("Liczba artykułów")
    ax.set_title(f"Top 10 źródeł informacji dla {company_name}")   
    ax.invert_yaxis() 

    plt.tight_layout()
    return fig

def plot_timeline(df: pd.DataFrame, company_name: str):
    """ Wykres liniowy pokazujący liczbę artykułów w czasie """

    df['published'] = pd.to_datetime(df['published'])
    df.set_index('published', inplace=True)
    daily_counts = df.resample('D').size()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(daily_counts.index, daily_counts.values, marker='o', linestyle='-')
    ax.set_xlabel("Data")
    ax.set_ylabel("Liczba artykułów")
    ax.set_title(f"Liczba artykułów w czasie dla {company_name}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig
