from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float, Boolean, Date
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///members.db', echo=False)

# Basisklasse für die Datenklassen
Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'

    nr = Column(String, primary_key=True)
    name = Column(String)
    eintrittsdatum = Column(String)
    geburtsdatum = Column(String)
    beitrag_bezahlt = Column(Boolean)

    # Optional: gibt einfach das Objekt "schön" aus.
    def __repr__(self):
        return f"<Entry(email={self.key}, name={self.value1}, firma={self.value2}, kanton={self.value3})>"

Base.metadata.create_all(engine)


def add_member(nr, name, eintrittsdatum, geburtsdatum, beitrag_bezahlt):
    global engine
    Session = sessionmaker(bind=engine)
    session = Session()
    entry = Member(nr=nr, name=name, eintrittsdatum=eintrittsdatum, 
                   geburtsdatum=geburtsdatum, beitrag_bezahlt=beitrag_bezahlt)
    session.add(entry)
    session.commit()

while True:
    nr = input("Mitgliedernummer: ")
    if nr == 'x':
        break

    name = input("Name: ")
    eintrittsdatum = input("Eintrittsdatum: ")
    geburtsdatum = input("Geburtsdatum: ")
    beitrag_bezahlt = bool(input("Mitgliedsbeitrag bezahlt (True/False): "))

    # mitglied hinzufügen
    add_member(nr, name, eintrittsdatum, geburtsdatum, beitrag_bezahlt)
