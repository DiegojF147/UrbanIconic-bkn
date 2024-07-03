from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

#inicializacion de la apliacion con Flask
app = Flask(__name__)

init_app(app)
#permitir solicitudes desde cualquier origin
CORS(app)

#registrar una ruta asociada a una vista
app.route('/api/products/',methods=['GET'])(get_all_products)
app.route('/api/products/',methods=['POST'])(create_product)
app.route('/api/products/<int:product_id>', methods=['GET'])(get_product)
app.route('/api/products/<int:product_id>', methods=['PUT'])(update_product)
app.route('/api/products/<int:product_id>', methods=['DELETE'])(delete_product)

if __name__ == '__main__':
    #levanta servidor de desarrollo flask
    app.run(debug=True)

