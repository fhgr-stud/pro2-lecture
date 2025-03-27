from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

# Datenbank-Verbindung herstellen
engine = create_engine('sqlite:///example.db', echo=True)

# Basisklasse für die Datenklassen
Base = declarative_base()

# Datenklasse für die Tabelle 'products' - Beschreibung der Tabelle
class Product(Base):
    # Tabellenname
    __tablename__ = 'products'

    # Spalten der Tabelle
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    # Hilfsfunktion für die Ausgabe
    def __repr__(self):
       return f"<Product(name='{self.name}', price='{self.price}')>" 

# Erzeugen der Tabelle, falls diese noch nicht existiert
Base.metadata.create_all(engine)

# Session erstellen
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Beispieldaten einfügen
session.add_all([Product(name='Apple', price=1.99),
                 Product(name='Banana', price=0.99),
                 Product(name='Orange', price=1.49),
                 Product(name='Pineapple', price=2.99),
                 Product(name='Pear', price=1.99) ])

# Beim Einfügen oder Ändern von Daten muss commit aufgerufen werden
session.commit()
