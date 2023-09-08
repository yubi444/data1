from flask import redirect, jsonify, render_template, request
import pandas as pd
from app.models import db, Fooditems
from flask import Blueprint

routes_bp = Blueprint(
    'routes_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@routes_bp.route('/')
def home():
    return render_template('table.html')


@routes_bp.route('/api/fooditems')
def get_fooditems():
    fooditems = Fooditems.query
    return {'data': [fooditem.to_dict() for fooditem in Fooditems.query]}


@routes_bp.route('/import')
def import_csv():
    title = 'Import Datasets'
    return render_template('import.html', title=title)


@routes_bp.route('/import/upload_file', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        parse_csv(uploaded_file.filename)
    return redirect('/import')


def parse_csv(file_path):
    csv_data = pd.read_csv(file_path)
    for i, row in csv_data.iterrows():
        fooditems = Fooditems(
            restaurant=row['restaurant'],
            item=row['item'],
            calories=row['calories']
        )
        db.session.add(fooditems)
    db.session.commit()
