import json
from flask import render_template, Blueprint, request

from models.alert import Alert
from models.item import Item
from models.store import Store

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    alerts = Alert.all()
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET','POST'])
def create_alert():
    if request.method == 'POST':
        item_url = request.form['item_url']

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.save_to_mongo()

        price_limit = float(request.form['price_limit'])
        Alert(item._id, price_limit).save_to_mongo()

        #return something like item added

    return render_template('alerts/new_alert.html')