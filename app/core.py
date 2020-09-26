from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator
from datetime import datetime, timedelta
import timeago

# https://github.com/CITGuru/PyInquirer

def get_all_products():
    """
    return all product stored in the database
    sorted by expiration date and stock
    """
    now = datetime.now()
    # todo: fetch database
    products = [
        {
            'id': 0,
            'name': 'Carottes',
            'units': 3,
            'expires': now + timedelta(days=3)
        },
        {
            'id': 0,
            'name': 'Lait',
            'units': 1,
            'expires': now + timedelta(days=10)
        },
    ]
    res = []
    for product in products:
        res.append('{num} {name} expires {date}'.format(
            name=product['name'],
            num=product['units'],
            date=timeago.format(product['expires'], now),
        ))
    return res

def validate_number(num):
    return num.isdigit()

def add_product():
    """
    add product ?
     / - new
     - 2 carottes epires in 3 days
     - lait expires in 10 days
     - go back to menu
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
        questions = [
            {   
                'type': 'input',
                'name': 'name',
                'message': 'What product do you want to add?',
            },
            {   
                'type': 'input',
                'name': 'stock',
                'message': 'How many would you like to add?',
            },
            {   
                'type': 'input',
                'name': 'expire',
                'message': 'When does it expire?',
            },
        ]
        answers = prompt(questions)
        # todo: add product into the database
    elif answers['add'] == go_back:
        start_app()
    elif answers['add'] in products:
        questions = [
            {   
                'type': 'input',
                'name': 'stock',
                'validate': validate_number,
                'message': 'How many do you want to add?',
            }
        ]
        answers = prompt(questions)

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

