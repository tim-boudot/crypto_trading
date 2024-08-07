from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base=declarative_base()

class Person(Base):
    __tablename__="people"
    ssn=Column("ssn", Integer, primary_key=True)
    firstname=Column("firstname",String)
    age=Column("age",Integer)

    def __init__(self, ssn, first, age):
        self.ssn=ssn
        self.firstname=first
        self.age=age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.age}"

engine=create_engine('sqlite:///data/mydb.db', echo=True)

Base.metadata.create_all(bind=engine)

Session=sessionmaker(bind=engine)
session=Session()

person = Person(12312, 'Tim', 35)
session.add(person)
session.commit()

p1=Person(31243, "Bart", 36)
p2=Person(31224, 'Amine', 37)

session.add(p1)
session.add(p2)
session.commit()

# Example: Querying all users from the database
all_users = session.query(Person).all()

# Example: Querying a specific user by their username
person = session.query(Person).filter_by(username='Tim').first()

# Step 7: Close the session
session.close()
