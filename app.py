import os

from flask import Flask, render_template
from flask.cli import load_dotenv

from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint

app = Flask(__name__)
app.secret_key = 'asddddddddddddddddddddddddddddd'

# to pobieramy z confidu ktory we flasku = .env
load_dotenv('.env')
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


# app.register_blueprint(learning_blueprint, url_prefix='/greetings')

@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(store_blueprint, url_prefix='/stores')

if __name__ == '__main__':
    app.run()
# from models.alert import Alert
# from models.item import Item
#
# url = 'https://www.johnlewis.com/john-lewis-partners-art-nouveau-gin-decanter-bauble-blue/p4973041'
# tag_name = 'p'
# query = {"class": "price price--large"}
#
# new_item = Item(url, tag_name, query)
# # new_item.load_price()
#
# price = new_item.load_price()
# print(price)
#
# new_item.save_to_mongo()
#
# items_all = Item.all()
# print(items_all)
# print(items_all[0].json())
#
#
# alert = Alert("2a002b09a1144c96a8003d91991433aa",2000)
# alert.save_to_mongo()
