from app.models import Product
from app.settings import session


def create_product(session, **kwargs):
    product = Product(**kwargs)
    session.add(product)
    session.commit()

def product_name_valid(name):
    for l in name.replace(' ', ''):
        if not l.isalpha():
            return False
    return True

def enter_product(session):
    product_name = input('Enter a product you want to add in the fridge :')
    if not product_name_valid(product_name):
        print('{} is not valid'.format(product_name))
        enter_product(session)
        return
    if not Product.exists(session, name=product_name):
        print("Product {} doesn't exist, do you want to add it ?".format(product_name))
    else:
        print( "{} has been added !".format(product_name))
        
def start_app():
    # product = Product(name='test') # create a product (in python code)
    # session.add(product) (convert product instance into SQL code)
    # session.commit() apply it to the database
    # products = session.query(Product).all() # select all the product in database
    # for p in products:
    #     print(p) # print the product
    #     print(p.name) # print the name of the product
    enter_product(session)

