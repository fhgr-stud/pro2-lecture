from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///person.db', echo=True)

# Basisklasse für die Datenklassen
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    email = Column(String, primary_key=True)
    name = Column(String)
    firma = Column(String)
    kanton = Column(String)
    ort = Column(String)
    plz = Column(Integer)
    
Base.metadata.create_all(engine)


def add_person(email, name, firma, kanton, ort, plz):
    global engine
    Session = sessionmaker(bind=engine)
    session = Session()
    person = Person(email=email, name=name, firma=firma, kanton=kanton, ort=ort, plz=plz)
    session.add(person)
    session.commit()

def get_persons():
    global engine
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(Person).order_by(Person.email)  # Alternativ: Person.name, um nach dem Namen zu sortieren, etc.

def get_person_for_key(email):
    global engine
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(Person).filter(Person.email == email).first()
