from app.news_scrapper.news_url_scrapper import get_url_news
from app.news_scrapper.news_article_scrapper import get_news_article
import pandas as pd

# Dictionary with news categories and URLs
news_urls = {
    'Budget News': 'https://www.moneycontrol.com/news/business/budget/',
    'Market News': 'https://www.moneycontrol.com/news/business/',
    'Markets News': 'https://www.moneycontrol.com/news/business/markets/',
    'World News': 'https://www.moneycontrol.com/news/world/',
    'Crypto News': 'https://www.moneycontrol.com/news/tags/cryptocurrency.html'
}

# Dictionary to store DataFrames
news_dataframes = {}

# Loop through the dictionary and scrape each URL
def news_scrapper():
    for category, url in news_urls.items():
        print(f"Scraping {category} from {url}")
        news_list = get_url_news(url)
        
        # Extract article texts
        news_data = []
        for headline, link in news_list:
            article_text = get_news_article(link)
            news_data.append({'headline': headline, 'link': link, 'text': article_text})
        # Create a DataFrame
        df = pd.DataFrame(news_data)
    news_dataframes[category] = df
    return news_dataframes

