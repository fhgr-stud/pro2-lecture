from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///beispiel.db', echo=True)

# Basisklasse für die Datenklassen
Base = declarative_base()

class Entry(Base):
    __tablename__ = 'beispiels_eintrag'

    key = Column(String, primary_key=True)
    value1 = Column(String)
    value2 = Column(Integer)
    value3 = Column(Float)

    # Optional: gibt einfach das Objekt "schön" aus.
    def __repr__(self):
        return f"<Entry(email={self.key}, name={self.value1}, firma={self.value2}, kanton={self.value3})>"

Base.metadata.create_all(engine)


def add_entry(key, value1, value2, value3):
    global engine
    Session = sessionmaker(bind=engine)
    session = Session()
    entry = Entry(key=key, value1=value1, value2=value2, value3=value3)
    session.add(entry)
    session.commit()

def get_entries():
    global engine
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(Entry).order_by(Entry.key)

def get_entry_for_key(key):
    global engine
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(Entry).filter(Entry.key=key).first()
