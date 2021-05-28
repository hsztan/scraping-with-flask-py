from requests import get
from bs4 import BeautifulSoup

class RPPController:
    def __init__(self):
        self.url = 'https://rpp.pe/noticias/coronavirus/'
        self.soup = None
        self.soup_articles = []
        self.limit = 3
        self.fetch_news()
        self.fetch_articles()
        self.get_data_articles()

    def fetch_news(self):
        try:
            response = get(self.url)
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            print(e)

    def fetch_articles(self):
        articles = self.soup.findAll('article')
        self.soup_articles = articles[:self.limit]

    def get_data_articles(self):
        articles = self.soup_articles
        response = []

        for article in articles:
            title = article.find('h2').find('a')
            response.append({
                'title': title.get_text()
            })
        print(response)
