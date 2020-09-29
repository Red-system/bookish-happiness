# # import necessaires au bon fonctionnement:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# # Creer et comprendre l'Engine:

# Commencons par creer l'Engine, qui sera l'element par lequel SQLAlchemist va communiquer avec notre database. En creeant cet Engine on doit donc 
# fournir notre Databasa URL tel qu'ici: 
database_url = 'sqlite:///:memory:'
# l'url de la db est propre a chaque moteur de BDD SQL
# par exemple pour MySQL : 
engine = create_engine(database_url, echo=True)

# On trouve l'URL de la data base dans ...

# Avec cette commande on dirige seulement les actions effectuées vers un endroit precis, l'URL. Le parametre echo=True fera que SQLAlchemy appliquera les changements que les fonctions SQL appellents. Ce parametre ne doit pas etre activé en production.

# Une fois que l'Engine connait notre database URL il est pret pour executer les commandes en utilisant la methode "engine.execute()". 

# # Engine ou Connection:

# On peut egelement effectuer des commandes a travers l'Engine en creeant une Connenction de cette maniere:

# conn = engine.connect()
# conn.execute(...)

# Cela nous permet de creer une commence de transaction ce qui veut dire que toutes les commandes s'effectueront correctements ou s'annuleront en cas d'erreur.



