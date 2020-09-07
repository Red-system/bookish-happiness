from app.models import Product
from app.settings import session


def start_app():
    # product = Product(name='test') # create a product (in python code)
    # session.add(product) (convert product instance into SQL code)
    # session.commit() apply it to the database
    # products = session.query(Product).all() # select all the product in database
    # for p in products:
    #     print(p) # print the product
    #     print(p.name) # print the name of the product
    """
    type the name of the product ?
    - tagada
    oh I'm sorry this product already exists
    - 1234
    oh not a valid name
    - milk
    super ! the milk has been created !
    """
    product = []
    p = (input("Enter a product:"))
    for l in p :
        if l .isnumeric():
            return('This name is not valid')
        elif l not .isalpha():
            return('This name is not valid')

    
    print(product)
    x = input("What product are you looking for?")
        if x in product:

