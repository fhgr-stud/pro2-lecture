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


print("Mitgliederliste:")

Session = sessionmaker(bind=engine)
session = Session()
for mitglied in session.query(Member):
    print(f"{mitglied.nr}: {mitglied.name}, Eintrittsdatum: {mitglied.eintrittsdatum}, "
          f"Geburtsdatum: {mitglied.geburtsdatum}, "
          f"Mitgliedsbeitrag: {'bezahlt' if mitglied.beitrag_bezahlt else 'nicht bezahlt'}")




