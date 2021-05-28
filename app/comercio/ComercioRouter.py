from app import app
from app.comercio.ComercioController import ComercioController

@app.route('/scrapping/comercio')
def comercio():
    controller = ComercioController()
    return controller.get_articles()