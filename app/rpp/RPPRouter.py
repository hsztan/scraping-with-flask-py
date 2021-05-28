from app import app
from app.rpp.RPPController import RPPController

@app.route('/scrapping/rpp')
def rpp():
    controller = RPPController()
    return 'RPP'