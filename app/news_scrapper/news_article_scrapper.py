import requests
from bs4 import BeautifulSoup
def get_news_article(url):
    # Send a GET request to the article URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the article. Status code: {response.status_code}")
        return ""
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the article text
    article_body = soup.find('div', class_='content_wrapper arti-flow')
    if article_body:
        paragraphs = article_body.find_all(['p','ul'])
        article_text = ' '.join([para.text.strip() for para in paragraphs])
        return article_text
    
    return ""