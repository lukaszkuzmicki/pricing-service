import json

from flask import Flask, render_template, request
from learning import learning_blueprint
from models.item import Item

from views.alerts import alert_blueprint
from views.stores import store_blueprint

app = Flask(__name__)

# app.register_blueprint(learning_blueprint, url_prefix='/greetings')


app.register_blueprint(alert_blueprint, url_prefix= '/alerts')
app.register_blueprint(user_blueprint, url_prefix= '/users')
app.register_blueprint(store_blueprint, url_prefix= '/stores')




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




