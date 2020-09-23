import json
from flask import render_template, Blueprint, request

from models.item import Item

item_blueprint = Blueprint('items', __name__)


@item_blueprint.route('/')
def index():
    items = Item.all()
    return render_template('items/index.html', items=items)


@item_blueprint.route('/new', methods=['GET','POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']
        tag_name = request.form['tag_name']
        #json.loads takes a string and turnin it into dictionary
        query = json.loads(request.form['query'])

        Item(url, tag_name, query).save_to_mongo()

        #return something like item added

    return render_template('items/new_item.html')