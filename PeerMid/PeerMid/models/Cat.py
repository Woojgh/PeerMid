from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime
)

from .meta import Base


class Cat(Base):
    __tablename__ = 'cats'
    category = Column(Unicode)
    image = Column(Unicode)
    creation_date = Column(DateTime)
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)

    def to_json(self):
        output = {}
        output['category'] = self.category
        output['image'] = self.image
        output['creation_date'] = self.creation_date.strftime('%B %d, %Y')
        output['id'] = self.id
        output['title'] = self.title
        output['body'] = self.body
        return output