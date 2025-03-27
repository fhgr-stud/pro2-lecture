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

# Session erstellen
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Alle Zeilen der Tabelle sortiert nach der `id` ausgeben
for product in session.query(Product).order_by(Product.id):
    print(product.name, product.price)

id = 5
# Produkt mit `id = 5` ausgeben
print("Produkt mit id = 5")

# Hinweis: `.first()` gibt die erste Zeile des Resultats aus
print(session.query(Product).filter(Product.id == id).first())

# Alle Produkte mit einem Preis zwischen 2.00 und 3.00 holen 
# und ausgeben.
low = 2.00
high = 3.00
print("Alle Produkte zwischen 2.00 und 3.00")

# Filterkriterien werden durch "Anhängen" miteinander kombiniert.
resultat = session.query(Product).filter(
              Product.price >= low).filter(Product.price <= high)

for product in resultat:
    print(product.name, product.price)


# einzelnes Produkt ändern
id = 5
new_price = 2.99

# Produkt auswählen und aktualisieren
session.query(Product).filter(
          Product.id == id).update({"price": new_price})

# Änderung mittels `commit()` bestätigen
session.commit()

session.close()
