from requests import get
from bs4 import BeautifulSoup


class ComercioController:
    def __init__(self):
        self.url = "https://elcomercio.pe/noticias/coronavirus/"
        self.soup = None
        self.soup_articles = []
        self.limit = 5
        self.get_articles()

    def fetch_news(self):
        try:
            response = get(self.url)
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.content, "html.parser")
        except Exception as e:
            print(e)

    def fetch_articles(self):
        articles = self.soup.findAll("div", {"class": "story-item"})
        self.soup_articles = articles[: self.limit]

    def get_data_articles(self):
        articles = self.soup_articles
        response = []

        for article in articles:
            title = article.find("a", {"class": "story-item__title"})
            subtitle = article.find("p", {"class": "story-item__subtitle"})
            article_url = f"https://elcomercio.pe{title.get('href')}"
            # time = article.find('time').get('data-x')
            image_url, time = self.get_data_internal_article(article_url)
            response.append(
                {
                    "title": title.get_text(),
                    "subtitle": subtitle.get_text(),
                    "url": article_url,
                    "time": time,
                    "image_url": image_url,
                }
            )
        return response

    def get_data_internal_article(self, article_url):
        img = ""
        time = ""
        try:
            response = get(article_url)
            if response.status_code == 200:
                soup_data = BeautifulSoup(response.content, "html.parser")
                picture = soup_data.find("picture")
                img_container = picture.find("img", {"class": "s-multimedia__image"})
                img = img_container.get("src")

                time = soup_data.find("time", {"class": "story-contents__time"}).get(
                    "datetime"
                )
        except Exception as e:
            print(e)

        return img, time

    def get_articles(self):
        self.fetch_news()
        response = self.fetch_articles()
        response = self.get_data_articles()

        return {"articles": response}
