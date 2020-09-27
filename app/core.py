from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator
from datetime import datetime, timedelta
import timeago
from app.models import Product
from app.settings import session
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying



def get_all_products():
    """
    return all product stored in the database
    #odo sorted by expiration date and stock
    """
    now = datetime.now()

    """
    en sql
    select * from products
    """
    res = []
    for product in session.query(Product).all():
        choice_text = '{num} {name} expires {date}'.format(
            name=product.name,
            num=product.stock,
            date=timeago.format(product.expire, now),
        )
        res.append({
            'name': choice_text,
            'value': product,
        })
    return res

def validate_number(num):
    return num.isdigit()

def validate_date(date):
    try:
        datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return 'The date format is invalid, please try the format : dd/mm/yyy'

def add_new_product():
    """
    add a new product in the database from the first line of questionning
    """
    questions = [
        {   
            'type': 'input',
            'name': 'name',
            'message': 'What product do you want to add?',
        },
        {   
            'type': 'input',
            'name': 'stock',
            'validate': validate_number,
            'message': 'How many would you like to add?',
        },
        {   
            'type': 'input',
            'name': 'expire',
            'validate': validate_date, # 02/09/2020
            'message': 'When does it expire?',
        },
    ]
    answers = prompt(questions)
        
    new_product = Product(
            name=answers['name'],
            stock=answers["stock"],
            expire=datetime.strptime(answers['expire'], '%d/%m/%Y')
    )
    session.add(new_product)
    print('{} has been added to the database'.format(new_product.name))
    start_app()

def add_existing_product(product):
    """
    add a new product from existind product found in database
    """
    questions = [
        {   
            'type': 'input',
            'name': 'stock',
            'validate': validate_number,
            'message': 'How many do you want to add?',
        },
        {   
            'type': 'input',
            'name': 'expire',
            'validate': validate_date, # 02/09/2020
            'message': 'When does it expire?',
        },
    ]
    
    answers = prompt(questions) 

    add_product = Product(
            name=product.name,
            stock=answers["stock"],
            expire=datetime.strptime(answers['expire'], '%d/%m/%Y')
    )
    session.add(add_product)
    
    print('Your product has been added to the database')
    
    start_app()
    
   

def add_product():
    """
    ask if the use wants to add a new product 
    or add an existing product to the database
    or go back to the menu
    """
    products = get_all_products()
    new = 'Not in the list'
    go_back = 'Go back to menu'
    questions = [
    {   
        'type': 'list',
        'name': 'add',
        'message': 'What product do you want to add ?',
        'choices': [
            new,
            *products,
            go_back,
        ]
    }
    ]
    answers = prompt(questions)
    if answers['add'] == new:
        add_new_product()
    elif answers['add'] == go_back:
        start_app()
    elif answers['add'] in [p['value'] for p in products]:
        add_existing_product(answers['add'])

def get_all_recipes():
    recipes=[
        {
            'id':1,
            'name':"Tarte aux pommes",
        },
        {
            'id':2,
            'name':"Tarte aux poires",
        }
    ]
    res=[]
    for recipe in recipes:
        res.append(recipe['name'])
    return res

def get_recipes():
    questions = [
        {
            'type': 'list',
            'name': 'name',
            'message': 'Those are the recipes available:',
            'choices': [
                *get_all_recipes()
            ]
        },
    ]
    # todo: remove products linked to the recipe


def start_app():
    """
    First line of questionning to the consumer
    """

    add_product_text = 'Add product'
    get_recipe_text = 'Get Recipes'
    questions = [
    {
        'type': 'list',
        'name': 'menu',
        'message': 'What do you want to do?',
        'choices': [
            add_product_text,
            get_recipe_text,
        ]
    }
    ]

    answers = prompt(questions)
    if answers['menu'] == add_product_text:
        add_product()
    elif answers['menu'] == get_recipe_text:
        get_recipes()

