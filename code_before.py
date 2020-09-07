
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
def add_prod():
    
    p = (input("Enter a product or type Next to continue:"))
    
    if p == "Next":
        search_prod(product)
    
    for l in p :
        if not l.isalpha():
            print('This name is not valid')
            add_prod()
    
    else:
        product.append(p.capitalize())
        return(print(product), add_prod())
    

def search_prod(list):
    
    print(product)
    
    x = input("What product are you looking for?")
    
    if x in product:
        return('This product is in stock!')
    
    else:
        r = input("I'm sorry, this product is unavailable. Would you like to add it to the list?")
        
        if r == "Yes":
            product.append(x)
        elif r == "No":
            return x

    
    
    
    
    
print(add_prod())
print("GG René")
