from requests import get
from bs4 import BeautifulSoup

class RPPController:
    def __init__(self):
        self.url = 'https://rpp.pe/noticias/coronavirus/'
        self.soup = None
        self.soup_articles = []
        self.limit = 5
        self.get_articles()

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
            subtitle = article.find('p')
            article_url = title.get('href')
            time = article.find('time').get('data-x')
            image_url = self.get_image_articles(article_url)
            response.append({
                'title': title.get_text(),
                'subtitle': subtitle.get_text(),
                'url': article_url,
                'time': time,
                'image_url': image_url
            })
        return response

    def get_image_articles(self, article_url):
        img = ''
        try:
            response = get(article_url)
            if response.status_code == 200:
                soup_image = BeautifulSoup(response.content, 'html.parser')
                picture = soup_image.find('div', {'class':'cover'})
                if picture:
                    img_container = picture.find('img')
                    img = img_container.get('src')
        except Exception as e:
            print(e)

        return img


    def get_articles(self):
        self.fetch_news()
        self.fetch_articles()
        response = self.get_data_articles()

        return {
            'articles': response
        }