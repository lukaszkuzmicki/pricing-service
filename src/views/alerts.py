from flask import render_template, Blueprint, request, redirect, url_for, session

from src.models.alert import Alert
from src.models.item import Item
from src.models.store import Store
from src.models.user.decorators import requires_login

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
@requires_login
def index():
    print(session['email'])
    # alerts = Alert.all()
    alerts = Alert.find_many_by('user_email', session['email'])
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET','POST'])
@requires_login
def create_alert():
    if request.method == 'POST':
        item_url = request.form['item_url']
        alert_name = request.form['alert_name']
        price_limit = float(request.form['price_limit'])

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.load_price()
        item.save_to_mongo()


        Alert(alert_name, item._id, price_limit, session['email']).save_to_mongo()

        #return something like item added

    return render_template('alerts/new_alert.html')

@alert_blueprint.route('/edit/<string:alert_id>', methods=['GET','POST'])
@requires_login
def edit_alert(alert_id):
    alert = Alert.get_by_id(alert_id)

    if request.method =='POST':
        price_limit = float(request.form['price_limit'])
        alert.price_limit = price_limit
        alert.save_to_mongo()

        #URL FOR CALCULATE THE CURRENT INDEX METHOD "." MEANS CURRENT BLUEPRINT
        return redirect(url_for('.index'))
    return render_template('alerts/edit.html', alert=alert)


@alert_blueprint.route('/delete/<string:alert_id>')
@requires_login
def delete_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    if alert.user_email == session['email']:
        alert.remove_from_mongo()

    return redirect(url_for('.index'))




