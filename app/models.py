from app.database import get_db

class Product:
    #CONSTRUCTOR
    def __init__(self,id_product=None,product=None,category=None,price=None,banner=None):
        self.id_product = id_product
        self.product = product
        self.category = category
        self.price = price
        self.banner = banner

    @staticmethod
    def get_by_id(product_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM products WHERE id_product = %s", (product_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Product(id_product=row[0], product=row[1], category=row[2], price=row[3], banner=row[4])
        return None
    
    @staticmethod    
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        products = [Product(id_product=row[0], product=row[1], category=row[2], price=row[3], banner=row[4]) for row in rows]
        
        cursor.close()
        return products
    
    def save(self):
        #logica para INSERT/UPDATE en base datos
        db = get_db()
        cursor = db.cursor()
        if self.id_product:
            cursor.execute("""
                UPDATE products SET product = %s, category = %s, price = %s, banner = %s
                WHERE id_product = %s
            """, (self.product, self.category, self.price, self.banner, self.id_product))
        else:
            cursor.execute("""
                INSERT INTO products (product, category, price, banner) VALUES (%s, %s, %s, %s)
            """, (self.product, self.category, self.price, self.banner))
            self.id_product = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM products WHERE id_product = %s", (self.id_product,))
        db.commit()
        cursor.close()
    
    def serialize(self):
        return {
            'id_product': self.id_product,
            'product': self.product,
            'category': self.category,
            'price': "${:,.3f}".format(self.price),
            'banner': self.banner,
        }