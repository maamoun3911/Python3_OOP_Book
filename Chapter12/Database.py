# import sqlite3

# connection = sqlite3.connect("mydb.db")

# connection.execute(
#     "create table if not exists pet (type, breed, gender, name)"
# )

# connection.execute(
#     "INSERT INTO pet VALUES ('dog', 'spaniel', 'female', 'Esme')"
# )

# connection.execute(
#     "INSERT INTO pet VALUES ('cat', 'persian', 'male', 'Oscar')"
# )

# result = connection.execute(
#     "SELECT bread, name, from pet where type='dog'"
# )

# print(result)
# connection.close()

#####################################################

import sqlalchemy as sqa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pet(Base):
    __tablename__ = "pet"
    id = sqa.Column(sqa.Integer, primary_key=True)
    type = sqa.Column(sqa.String(16))
    bread = sqa.Column(sqa.String(32))
    gender = sqa.Column(sqa.Enum("Male", "Female"))
    name = sqa.Column(sqa.String(64))

engine = sqa.create_engine("sqlite3:///mydata.db")
Base.metadata.create_all(engine)


session = sqa.orm.sessiomaker(bind=engine)
session.add(Pet)
session.commit()
    