from flask import jsonify, request
from app.models import Product



#funcion que busca todo el listado de los productos
def get_all_products():
    products = Product.get_all()
    list_products = [product.serialize() for product in products]
    return jsonify(list_products)

#funcion que busca un producto
def get_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(product.serialize())

def create_product():
    data = request.json
    #agregar una logica de validacion de datos
    new_product = Product(None,data['product'],data['category'],data['price'],data['banner'])
    new_product.save()
    return jsonify({'message':'Producto creado con exito'}), 201
    

def update_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    data = request.json
    product.product = data['product']
    product.category = data['category']
    product.price = data['price']
    product.banner = data['banner']
    product.save()
    return jsonify({'message': 'Product updated successfully'})

def delete_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    product.delete()
    return jsonify({'message': 'Product deleted successfully'})