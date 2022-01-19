from flask import Flask, request, jsonify, render_template, request, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import csv
from io import StringIO


#initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize database
db = SQLAlchemy(app)

#initalize marshmallow
ma = Marshmallow(app)

#Each item structure
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) #auto increments when inserting
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    
    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty    
    
    #used abs() to make sure price and qty are positive
    def __repr__(self):
        str = f"{'Item: ' + self.name}{' Description:  ' + self.description} Price = ${abs(self.price)} Qty= {abs(self.qty)}"
        return str
    
#product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')
        
#init schema
product_schema = ProductSchema()
product_schemas = ProductSchema(many=True)

#Adding items to inventory
@app.route('/data/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("index.html")
    
    if request.method == 'POST':
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]
        qty = request.form["qty"]
        
        item = Product(name=name, description=description, price=price, qty=qty)
        db.session.add(item)
        db.session.commit()
        return redirect('/data')

#Getting all items from inventory
@app.route('/data')
def get_products():
    all_products = Product.query.all()
    return render_template('products.html', all_products=all_products)

#getting a certain item from inventory
@app.route('/data/<int:id>')
def get_product(id):
    product = Product.query.get(id)
    if product:
        return product_schema.jsonify(product)
    else:
        return "This id doesn't exist"
    
#updating an item from inventory
@app.route('/data/<int:id>/update', methods = ['GET', 'POST'])
def update_product(id):
    
    product = Product.query.get(id)
    if request.method == 'POST':
        if product:
            db.session.delete(product)
            db.session.commit()

            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            qty = request.form['qty']
            
            product = Product(name=name, description=description, price=price, qty=qty)
            db.session.add(product)
            db.session.commit()
            return redirect(f'/data/create')
    
    if request.method == 'GET':
        return render_template('update.html', product = product)
    
    return product_schema.jsonify(product)
    
#deleting an item from inventory
@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete_product(id):
    product = Product.query.get(id)
    if request.method == 'POST':
        if product:
            db.session.delete(product)
            db.session.commit()
            return redirect('/data')
        else:
            return redirect('/data')
    elif request.method == 'GET':
        return render_template('delete.html')

#csv download
@app.route('/data/download', methods = ['GET', 'POST'])
def reportGenerator():
    si = StringIO()
    cw = csv.writer(si)
    all_inventory = Product.query.all()
    cw.writerows([(product.name, product.description, product.price, product.qty) for product in all_inventory])
    response = make_response(si.getvalue())
    response.headers['All Inventory'] = 'attachment; filename=report.csv'
    response.headers["Content-type"] = "text/csv"
    return response

#to run server
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
