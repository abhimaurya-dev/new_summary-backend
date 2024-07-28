import requests
from bs4 import BeautifulSoup

def get_url_news(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all articles
    articles = soup.find_all('li', class_='clearfix')

    # Loop through the articles and extract the headline and link
    news = []
    for article in articles:
        a_tag = article.find('a')
        if a_tag and 'href' in a_tag.attrs and 'title' in a_tag.attrs:
            headline = a_tag['title']
            link = a_tag['href']
            news.append((headline, link))
    
    return news