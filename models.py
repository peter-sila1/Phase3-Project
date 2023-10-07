from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///vms.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define your models
class Visitor(Base):
    __tablename__ = 'visitor'

    visitor_id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    visits = relationship('Visit', back_populates='visitor')


class Office(Base):
    __tablename__ = 'office'

    office_id = Column(Integer, primary_key=True)
    office_name = Column(String)
    visits = relationship('Visit', back_populates='office')


class Visit(Base):
    __tablename__ = 'visits'

    visit_id = Column(Integer, primary_key=True)
    visitor_id = Column(Integer, ForeignKey('visitor.visitor_id'))
    office_id = Column(Integer, ForeignKey('office.office_id'))
    person_visited = Column(String)
    visit_date = Column(Date)
    visitor = relationship('Visitor', back_populates='visits')
    office = relationship('Office', back_populates='visits')

Base.metadata.create_all(engine)