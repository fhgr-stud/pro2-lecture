# 1. Definition der Klasse mittels SQLAlchemy

Base = declartive_base()

class User(Base):
    __tablename__ = 'user'

    email = Column(String, primary_key=True)
    password = Column(String)

    # optional, aber empfohlen
    def __repr__(self):
        return f"<User(email={self.email}, password={self.password})>"

engine = create_engine("sqlite://benutzer.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#
# Schreiben in die Datenbank
#
ana = User('ana@kurz.ch', '1234')
jim = User('jim@fhgr.ch', '4321')
session.add_all([ana, jim])
session.commit()   # Notwendig bei jeder __Änderung__ in der Datenbank

#
# Aus der Datenbank lesen
# 
resultat = session.query(User)   # holt alle Benutzer in der Datenbank
for user in resultat:
    print(user.email, "hat passwort", user.password)

# sortieren
resultat_sortiert = session.query(User).order_by(User.email)

# filtern
resultat_gefiltert = session.query(User).filter(User.email = 'ana@kurz.ch')
resultat_gefiltert = session.query(User).filter(User.email = 'ana@kurz.ch').filter(
                           User.password='1234')

#
# Datenbank ändern
#

# Werte ändern
session.query(User).filter(User.email = 'ana@kurz.ch').update({'password': 'abc'})
session.commit()

# Einträge löschen
session.query(User).filter(User.email = 'ana@kurz.ch').delete()
session.commit()



