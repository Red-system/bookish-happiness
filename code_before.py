from datetime import datetime, timedelta


class Category:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    def __str__(self):
        return '{} -> {}'.format(self.id, self.name)
    
    def say_my_name(self):
        return 'Hi my category name is ' + self.name
    
    def i_refer_to(self):
        pass

class WtfClass:
    def say_wtf(self):
        return 'WTF man !!'

class ProductCategory(Category):
    
    def i_refer_to(self):
        return 'I refer to a product'

class RecipeCategory(Category, WtfClass):
    
    def i_refer_to(self):
        return 'I refer to a recipe'

parent_category = Category(1, 'Parent category')
product_caterogy = ProductCategory(2, 'Produit laitier')
recipe_category = RecipeCategory(3, 'Dessert')

print(parent_category.say_my_name())
print(parent_category.i_refer_to())
print(product_caterogy.say_my_name())
print(product_caterogy.i_refer_to())
print(recipe_category.say_my_name())
print(recipe_category.i_refer_to())
print(recipe_category.say_wtf())

class Product:

    def __init__(self, id=None, name=None, expire_date=None):
        """        constructor = __init__
        """
        # print('construit un object avec id = {} et name = {}'.format(id, name))
        self.id = id
        self.name = name
        self.expire_date = expire_date

    def __str__(self):
        return 'id: {} -> name {}'.format(self.id, self.name)

    def is_expired(self) -> bool:
        return self.expire_date <= datetime.now()

class Recipe:

    def __init__(self, products, name):
        self.products = products
        self.name = name

    def _counter_build(self):

        counter = {}

        for p in self.products:
            if p in counter:
                counter[p] += 1
            else:
                counter[p] = 1
        return counter

    def can_cook(self, product_names):
        
        counter = self._counter_build()

        for p in product_names:
            if p in self.products:
                counter[p] -= 1

        for name, count in counter.items():
            if count > 0:
                return False
        return True


class Frigo:

    def __init__(self, id, name, list_prod, recipes):
        self.id = id
        self.name = name
        self.list_prod = list_prod
        self.recipes = recipes

    def add_prod(self, prod):
        self.list_prod.append(prod)

    def del_prod(self, name):
        found_index = None
        for k, p in enumerate(self.list_prod):
            if p.name == name:
                found_index = k
        if found_index is None:
            print('Sorry but this product is not in the fridge')
        else:
            del self.list_prod[found_index]
            print('product {} has been deleted'.format(name))

    def bundle_expire(self):
        return [p for p in self.list_prod if p.expire_date < datetime.now()]
        # res= []
        # for p in self.list_prod:
        #     if p.expire_date < datetime.now():
        #         res.append(p)
        # return res

    def count_item(self, name):
        return len([n for n in self.list_prod if n.name == name])

    def get_recipes(self):
        
        product_names = [p.name for p in self.list_prod]

        return [r.name for r in self.recipes if r.can_cook(product_names)]
    
    def get_expire_soon_recipes(self):
        #check si la date est comprise entre odj et dans x jours//années/Secondes :  
        """ produit = self.list_prod[0]
      
        if now < produit.expire_date  < in_7_days:
            print('tagada') """
        
        now = datetime.now()
        in_7_days = now + timedelta(days= 7)
        # list_prod = []
        # for p in self.list_prod:
        #     if now < p.expire_date < in_7_days: 
        #         list_prod.append(p.name for p in self.list_prod)
        return [p.name for p in self.list_prod if now < p.expire_date < in_7_days]

p1 = Product(1, "patate", datetime(2020, 9, 10))
p2 = Product(2, "pasta", datetime(2020, 9, 13))
p4 = Product(5, "pesto", datetime(2020, 9, 14))
p3 = Product(3, "rutabaga", datetime(2020, 9, 19))
p5 = Product(4, "beurre", datetime(2020, 9, 14))

pate_au_pesto = Recipe(['pasta', 'pesto'], 'pate au pesto')
pate_au_beurre = Recipe(['pasta', 'beurre'], 'pate au beurre')
puree = Recipe(['patate', 'patate', 'beurre'], 'puree')

# print(pate_au_pesto.can_cook(["pasta", "beurre"]))
# print(pate_au_pesto.can_cook(["beurre", "pasta"]))
# print(pate_au_pesto.can_cook(["pesto", "pasta"]))
# print(pate_au_pesto.can_cook(["pasta", "pesto"]))
# print(puree.can_cook(["patate", "pesto"]))
# print(puree.can_cook(["patate", "patate"]))
# print(puree.can_cook(["patate", "patate","beurre"]))
recipes = [pate_au_beurre, pate_au_pesto, puree]
product_list  = [p1, p2, p3, p4, p1, p5]
frigo = Frigo(1, 'frigo de la cuisine', product_list, recipes)

# print(frigo.get_expire_soon_recipes())




# product1 = Product(1, 'Product 1')
# # product1 = { 'id': 1, 'name': 'product 1' }
# # print(product1['name'])
# # product1.name
# product2 = Product(2, 'Product 2')
# product3 = Product(name='Product 3')


# product_list = [
#     product1,
#     product2,
#     product3,
# ]


# product4 = Product(4, 'Salade')
# frigo.add_prod(product4)
# print(frigo.list_prod)
# frigo.del_prod(product4.name)
# print(frigo.list_prod)
# frigo.del_prod('tagada')
