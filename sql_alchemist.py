# # import necessaires au bon fonctionnement:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


# # Creer et comprendre l'Engine:

# Commencons par creer l'Engine, qui sera l'element par lequel SQLAlchemist va communiquer avec notre database. En creeant cet Engine on doit donc
# fournir notre Databasa URL tel qu'ici:
# l'url de la db est propre a chaque moteur de BDD SQL
# par exemple pour MySQL : mysql+mysqldb://{USERNAME}:@{HOST}/{DATABASE_NAME}
# https://docs.sqlalchemy.org/en/13/core/engines.html#sqlite
# pour sqllite : 'sqlite:///:memory:' pour creer une db dans la RAM, c'est super pour tester mais si tu eteint l'ordi tout est perdu
# pour sqllite : 'sqlite:///nom_du_fichier' pour creer une db dans la RAM, c'est super pour tester mais si tu eteint l'ordi tout est enregistré dans le fichier
database_url = 'sqlite:///db.db'
engine = create_engine(
    database_url,
    echo=True,  # pour debugger
)

# On est pret a exectuer des commandes en SQ vi le engine.execute(). Ce format ne prend pas le language python.
# engine.execute(
#     "INSERT INTO utilisateur (id, nom, email) values (1, 'thib', 'tagada@pouet.com')"
# )

# engine.execute(
#     "SELECT * FROM utilisateur"
# )

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    products = relationship('Product', backref="users")

    def __repr__(self):
        return f'User {self.name}'

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')


Base.metadata.create_all(engine)

# user = User(
#     name="perdo2",
#     password="tagada",
# )

# user2 = User(
#     name='pedro3',
#     password='ped',
# )

# session.add(user)
# session.add(user2)

# session.commit()

# all_users = session.query(User).all()
# pedro_users = session.query(User).filter(
#     User.name.like('%pedro%') | User.name.like('%perdo%')
# ).all()

# print(all_users)
# print(pedro_users)

user = User(name='John')
product = Product(name='wolf', user=user)

session.add_all([user, product])
session.commit()

