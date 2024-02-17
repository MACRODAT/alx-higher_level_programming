#!/usr/bin/python3

"""
    fetch all states
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    engine = create_engine(url=f""
                           f"mysql+mysqldb://{argv[1]}:{argv[2]}@"
                           f"localhost:3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    for state in session.query(State)\
                        .filter(State.name.like("%a%")).order_by(State.id):
        print(f"{state.id}: {state.name}")
    session.close()
